"""Main evaluation runner for AgentGym."""

import asyncio
import os
import time
from datetime import datetime
from pathlib import Path
from typing import Dict

import logfire
from app.utils import setup_aws_environment, setup_logging, setup_logfire
from app.reporting import EvaluationResult, EvaluationSummary, save_reports
import config

logger = setup_logging()


class EvaluationRunner:
    """Orchestrates evaluation runs across puzzles, frameworks, and models."""
    
    def __init__(self):
        self.results: list[EvaluationResult] = []
        
    async def run_single_evaluation(
        self,
        puzzle_name: str,
        framework_name: str,
        model_config,
        run_number: int
    ) -> EvaluationResult:
        """Run a single evaluation and return the result, including token usage."""

        # Extract model identifier for logging
        if isinstance(model_config, dict):
            model_id = model_config.get("name", "custom_endpoint")
        else:
            model_id = model_config

        logger.info(f"🚀 Running {puzzle_name}/{framework_name}/{model_id}/run_{run_number}")

        start_time = time.time()

        prompt_tokens = None
        prediction_tokens = None

        try:
            # Import checker for this puzzle
            checker_module = __import__(f"puzzles.{puzzle_name}.checker", fromlist=["check"])
            check_func = checker_module.check

            # Import framework agent factory (reflecting new tree structure)
            framework_module = __import__(f"frameworks.{framework_name}.{puzzle_name}.agent", fromlist=["run_agent"])
            run_agent_func = framework_module.run_agent

            # Create and run agent (await if coroutine)
            with logfire.span("agent_execution"):
                agent_result = await run_agent_func(model_config)

            # Only support new AgentGymAgentResult return type
            if isinstance(agent_result, dict):
                result = agent_result.get("result", agent_result)
                usage = agent_result.get("usage")
                prompt_tokens = usage.get("prompt_tokens") if usage else None
                prediction_tokens = usage.get("completion_tokens") if usage else None
            else:
                result = agent_result

            # Check result
            with logfire.span("result_validation"):
                check_func(result)

            execution_time = time.time() - start_time

            logger.info(f"✅ {puzzle_name}/{framework_name}/{model_id}/run_{run_number} - PASSED ({execution_time:.2f}s)")

            # Log success to Logfire
            logfire.info(
                "Evaluation completed successfully",
                puzzle=puzzle_name,
                framework=framework_name,
                model=model_id,
                run_number=run_number,
                execution_time=execution_time,
                status="Pass",
                prompt_tokens=prompt_tokens,
                prediction_tokens=prediction_tokens
            )

            return EvaluationResult(
                puzzle=puzzle_name,
                framework=framework_name,
                model=model_id,
                run_number=run_number,
                status="Pass",
                execution_time=execution_time,
                prompt_tokens=prompt_tokens,
                prediction_tokens=prediction_tokens
            )

        except ModuleNotFoundError as e:
            # Framework doesn't have implementation for this puzzle
            if f"frameworks.{framework_name}.{puzzle_name}" in str(e):
                execution_time = time.time() - start_time
                
                logger.info(f"⚪ {puzzle_name}/{framework_name}/{model_id}/run_{run_number} - NOT AVAILABLE (no implementation)")
                
                # Log as not available to Logfire
                logfire.info(
                    "Evaluation not available - no implementation",
                    puzzle=puzzle_name,
                    framework=framework_name,
                    model=model_id,
                    run_number=run_number,
                    execution_time=execution_time,
                    status="Not Available"
                )

                return EvaluationResult(
                    puzzle=puzzle_name,
                    framework=framework_name,
                    model=model_id,
                    run_number=run_number,
                    status="Not Available",
                    error_message=f"No implementation for {puzzle_name} puzzle",
                    execution_time=execution_time,
                    prompt_tokens=prompt_tokens,
                    prediction_tokens=prediction_tokens
                )
            else:
                # Different module not found error, treat as failure
                execution_time = time.time() - start_time
                error_msg = str(e)

                logger.error(f"❌ {puzzle_name}/{framework_name}/{model_id}/run_{run_number} - FAILED: {error_msg}")
                
                # Log error to Logfire
                logfire.error(
                    "Evaluation failed",
                    puzzle=puzzle_name,
                    framework=framework_name,
                    model=model_id,
                    run_number=run_number,
                    execution_time=execution_time,
                    error=error_msg,
                    status="Fail"
                )

                return EvaluationResult(
                    puzzle=puzzle_name,
                    framework=framework_name,
                    model=model_id,
                    run_number=run_number,
                    status="Fail",
                    error_message=error_msg,
                    execution_time=execution_time,
                    prompt_tokens=prompt_tokens,
                    prediction_tokens=prediction_tokens
                )

        except Exception as e:
                execution_time = time.time() - start_time
                error_msg = str(e)

                logger.error(f"❌ {puzzle_name}/{framework_name}/{model_id}/run_{run_number} - FAILED: {error_msg}")
                
                # Log error to Logfire
                logfire.error(
                    "Evaluation failed",
                    puzzle=puzzle_name,
                    framework=framework_name,
                    model=model_id,
                    run_number=run_number,
                    execution_time=execution_time,
                    error=error_msg,
                    status="Fail"
                )

                return EvaluationResult(
                    puzzle=puzzle_name,
                    framework=framework_name,
                    model=model_id,
                    run_number=run_number,
                    status="Fail",
                    error_message=error_msg,
                    execution_time=execution_time,
                    prompt_tokens=prompt_tokens,
                    prediction_tokens=prediction_tokens
                )
    
    async def run_all_evaluations(self) -> EvaluationSummary:
        """Run all configured evaluations."""
        
        logger.info("🎯 Starting AgentGym evaluation run")
        logger.info("📊 Configuration:")
        logger.info(f"   Puzzles: {config.PUZZLES}")
        logger.info(f"   Framework-model combinations: {len(config.FRAMEWORK_MODEL_COMBINATIONS)}")
        
        # Calculate total evaluations from explicit combinations
        total_evaluations = 0
        for puzzle in config.PUZZLES:
            for combo in config.FRAMEWORK_MODEL_COMBINATIONS:
                total_evaluations += len(combo["frameworks"]) * len(combo["models"]) * config.NUM_RUNS
        
        logger.info(f"   Total evaluations: {total_evaluations}")
        
        # Setup AWS environment using AWS_PROFILE from environment
        aws_profile = os.environ.get("AWS_PROFILE")
        setup_aws_environment(aws_profile)
        
        # Log evaluation start to Logfire
        logfire.info(
            "Starting AgentGym evaluation run",
            total_evaluations=total_evaluations,
            puzzles=config.PUZZLES,
            num_runs=config.NUM_RUNS,
            framework_combinations=len(config.FRAMEWORK_MODEL_COMBINATIONS)
        )
        
        current_eval = 0
        
        # Run all combinations with Logfire span
        with logfire.span("evaluation_batch", total_evaluations=total_evaluations):
            for puzzle in config.PUZZLES:
                with logfire.span(f"puzzle_{puzzle}"):
                    for combo in config.FRAMEWORK_MODEL_COMBINATIONS:
                        for framework in combo["frameworks"]:
                            with logfire.span(f"framework_{framework}"):
                                for model in combo["models"]:
                                    with logfire.span(f"model_{model}"):
                                        for run_num in range(1, config.NUM_RUNS + 1):
                                            with logfire.span(f"run_{run_num}"):
                                                current_eval += 1
                                                
                                                logger.info(f"📈 Progress: {current_eval}/{total_evaluations}")
                                                
                                                result = await self.run_single_evaluation(
                                                    puzzle, framework, model, run_num
                                                )
                                                
                                                self.results.append(result)
        
        # Create summary
        summary = EvaluationSummary(
            results=self.results,
            total_runs=len(self.results),
            timestamp=datetime.now()
        )
        
        # Log final summary to Logfire
        passed_runs = len([r for r in self.results if r.status == "Pass"])
        failed_runs = len(self.results) - passed_runs
        success_rate = (passed_runs / len(self.results) * 100) if self.results else 0
        
        # Calculate average execution time, handling None values
        execution_times = [r.execution_time for r in self.results if r.execution_time is not None]
        avg_execution_time = sum(execution_times) / len(execution_times) if execution_times else 0
        
        logfire.info(
            "AgentGym evaluation run completed",
            total_runs=len(self.results),
            passed_runs=passed_runs,
            failed_runs=failed_runs,
            success_rate=success_rate,
            avg_execution_time=avg_execution_time
        )
        
        return summary
    
    def print_summary(self, summary: EvaluationSummary):
        """Print evaluation summary to console."""
        
        print("\n" + "="*80)
        print("🏆 AGENTGYM EVALUATION RESULTS")
        print("="*80)
        
        # Calculate overall stats
        total_runs = summary.total_runs
        passed_runs = len([r for r in summary.results if r.status == "Pass"])
        failed_runs = len([r for r in summary.results if r.status == "Fail"])
        not_available_runs = len([r for r in summary.results if r.status == "Not Available"])
        success_rate = (passed_runs / (passed_runs + failed_runs) * 100) if (passed_runs + failed_runs) > 0 else 0
        
        print("📊 Overall Statistics:")
        print(f"   Total runs: {total_runs}")
        print(f"   Passed: {passed_runs}")
        print(f"   Failed: {failed_runs}")
        print(f"   Not Available: {not_available_runs}")
        print(f"   Success rate: {success_rate:.1f}% (excluding not available)")
        
        # Group by puzzle and framework
        puzzle_stats: Dict[str, Dict[str, list]] = {}
        
        for result in summary.results:
            puzzle_key = result.puzzle
            framework_key = f"{result.framework}"
            
            if puzzle_key not in puzzle_stats:
                puzzle_stats[puzzle_key] = {}
                
            if framework_key not in puzzle_stats[puzzle_key]:
                puzzle_stats[puzzle_key][framework_key] = []
                
            puzzle_stats[puzzle_key][framework_key].append(result.status)
        
        # Print by puzzle
        for puzzle_name, frameworks in puzzle_stats.items():
            print(f"\n🧩 {puzzle_name.upper()}:")
            
            for framework_name, statuses in frameworks.items():
                passes = statuses.count("Pass")
                fails = statuses.count("Fail")
                testable_runs = passes + fails
                rate = (passes / testable_runs * 100) if testable_runs > 0 else 0

                # Create status display with emoji
                status_display = []
                for status in statuses:
                    if status == "Pass":
                        status_display.append("✅")
                    elif status == "Fail":
                        status_display.append("❌")
                    elif status == "Not Available":
                        status_display.append("⚪")
                    else:
                        status_display.append("?")

                status_str = " | ".join(status_display)
                rate_str = f"{rate:.0f}%" if testable_runs > 0 else "N/A"
                print(f"   {framework_name:20} [{status_str}] ({rate_str})")


async def main():
    """Main entry point for evaluation runner."""
    
    # Initialize Logfire monitoring
    setup_logfire()
    
    runner = EvaluationRunner()
    
    try:
        with logfire.span("agentgym_evaluation"):
            summary = await runner.run_all_evaluations()
            
            # Print results to console
            runner.print_summary(summary)
            
            # Save reports
            reports_dir = Path("reports")
            save_reports(summary, reports_dir)
            
            logger.info("🎉 Evaluation complete!")
            logger.info(f"📄 Reports saved to: {reports_dir.absolute()}")
            
    except KeyboardInterrupt:
        logger.info("⚠️  Evaluation interrupted by user")
        logfire.warning("Evaluation interrupted by user")
    except Exception as e:
        logger.error(f"💥 Evaluation failed: {e}")
        logfire.error("Evaluation failed with exception", error=str(e))
        raise


if __name__ == "__main__":
    asyncio.run(main())
