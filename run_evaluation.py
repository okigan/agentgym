"""Main evaluation runner for AgentGym."""

import asyncio
import time
from datetime import datetime
from pathlib import Path
from typing import Dict

from app.utils import setup_aws_environment, setup_logging
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
        model_id: str, 
        run_number: int
    ) -> EvaluationResult:
        """Run a single evaluation and return the result."""
        
        logger.info(f"🚀 Running {puzzle_name}/{framework_name}/{model_id}/run_{run_number}")
        
        start_time = time.time()
        
        try:
            # Import checker for this puzzle
            checker_module = __import__(f"puzzles.{puzzle_name}.checker", fromlist=["check"])
            check_func = checker_module.check


            # Import framework agent factory (reflecting new tree structure)
            framework_module = __import__(f"frameworks.{framework_name}.{puzzle_name}.agent", fromlist=["make_agent"])
            make_agent_func = framework_module.make_agent

            # Create agent
            agent = make_agent_func(model_id)

            # Run agent and validate result with checker
            async def run_and_check():
                # Try async .run, fallback to sync call
                try:
                    result = await agent.run("Find out the total number of fruits by calling the appropriate tools")
                except AttributeError:
                    result = agent("Find out the total number of fruits by calling the appropriate tools")
                check_func(result)

            await asyncio.wait_for(
                run_and_check(),
                timeout=config.TEST_TIMEOUT
            )

            execution_time = time.time() - start_time

            logger.info(f"✅ {puzzle_name}/{framework_name}/{model_id}/run_{run_number} - PASSED ({execution_time:.2f}s)")

            return EvaluationResult(
                puzzle=puzzle_name,
                framework=framework_name,
                model=model_id,
                run_number=run_number,
                status="Pass",
                execution_time=execution_time
            )

        except Exception as e:
            execution_time = time.time() - start_time
            error_msg = str(e)

            logger.error(f"❌ {puzzle_name}/{framework_name}/{model_id}/run_{run_number} - FAILED: {error_msg}")

            return EvaluationResult(
                puzzle=puzzle_name,
                framework=framework_name,
                model=model_id,
                run_number=run_number,
                status="Fail",
                error_message=error_msg,
                execution_time=execution_time
            )
    
    async def run_all_evaluations(self) -> EvaluationSummary:
        """Run all configured evaluations."""
        
        logger.info("🎯 Starting AgentGym evaluation run")
        logger.info("📊 Configuration:")
        logger.info(f"   Puzzles: {config.PUZZLES}")
        logger.info(f"   Frameworks: {config.FRAMEWORKS}")
        logger.info(f"   Models: {len(config.MODELS)} models")
        logger.info(f"   Runs per combination: {config.NUM_RUNS}")
        
        total_evaluations = len(config.PUZZLES) * len(config.FRAMEWORKS) * len(config.MODELS) * config.NUM_RUNS
        logger.info(f"   Total evaluations: {total_evaluations}")
        
        # Setup AWS environment using AWS_PROFILE from environment
        import os
        aws_profile = os.environ.get("AWS_PROFILE")
        setup_aws_environment(aws_profile)
        
        current_eval = 0
        
        # Run all combinations
        for puzzle in config.PUZZLES:
            for framework in config.FRAMEWORKS:
                for model in config.MODELS:
                    for run_num in range(1, config.NUM_RUNS + 1):
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
        
        return summary
    
    def print_summary(self, summary: EvaluationSummary):
        """Print evaluation summary to console."""
        
        print("\n" + "="*80)
        print("🏆 AGENTGYM EVALUATION RESULTS")
        print("="*80)
        
        # Calculate overall stats
        total_runs = summary.total_runs
        passed_runs = len([r for r in summary.results if r.status == "Pass"])
        failed_runs = total_runs - passed_runs
        success_rate = (passed_runs / total_runs * 100) if total_runs > 0 else 0
        
        print("📊 Overall Statistics:")
        print(f"   Total runs: {total_runs}")
        print(f"   Passed: {passed_runs}")
        print(f"   Failed: {failed_runs}")
        print(f"   Success rate: {success_rate:.1f}%")
        
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
                total = len(statuses)
                rate = (passes / total * 100) if total > 0 else 0
                
                status_str = " | ".join(statuses)
                print(f"   {framework_name:20} [{status_str}] ({rate:.0f}%)")


async def main():
    """Main entry point for evaluation runner."""
    
    runner = EvaluationRunner()
    
    try:
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
    except Exception as e:
        logger.error(f"💥 Evaluation failed: {e}")
        raise


if __name__ == "__main__":
    asyncio.run(main())
