"""Enhanced Bedrock model for Llama 4 models with pythonic tool calling support."""

import json
import re
from typing import List

from pydantic_ai import usage
from pydantic_ai.messages import ModelResponse, ModelResponsePart, TextPart, ToolCallPart
from pydantic_ai.models.bedrock import BedrockConverseModel


class EnhancedBedrockModel(BedrockConverseModel):
    """Enhanced Bedrock model that supports pythonic tool calling for Llama 4 models.

    This class extends the standard BedrockConverseModel to support parsing of multiple
    tool call formats from Llama 4 models:

    1. Pythonic format: <|python_start|>{"name": "tool_name", "parameters": {...}}<|python_end|>
    2. Plain JSON format: {"type": "function", "name": "tool_name", "parameters": {...}}

    This class automatically detects and parses these into proper ToolCallPart objects
    so they can be executed by the pydantic_ai framework.

    For non-Llama4 models, this class behaves identically to BedrockConverseModel.
    """

    def _is_llama4_model(self) -> bool:
        """Check if this is a Llama4 model that supports pythonic tool calling."""
        model_name_lower = self._model_name.lower()
        return "llama3-3" in model_name_lower or "llama4" in model_name_lower

    def _parse_pythonic_tool_calls(self, text: str) -> List[ModelResponsePart]:
        """Parse pythonic tool calls from text content.

        Looks for patterns like:
        1. <|python_start|>{"name": "tool_name", "parameters": {...}}<|python_end|>
        2. Plain JSON function calls: {"type": "function", "name": "tool_name", "parameters": {...}}

        Args:
            text: The text content to parse

        Returns:
            List of ModelResponsePart objects (TextPart or ToolCallPart)
        """
        if not self._is_llama4_model():
            return [TextPart(content=text)]

        # First try to parse as plain JSON function call
        plain_json_part = self._try_parse_plain_json_function_call(text)
        if plain_json_part:
            return [plain_json_part]

        # Then try pythonic tool calls with delimiters
        return self._parse_delimited_tool_calls(text)

    def _try_parse_plain_json_function_call(self, text: str) -> ModelResponsePart | None:
        """Try to parse text as a plain JSON function call.

        Handles formats like:
        {"type": "function", "name": "tool_name", "parameters": {...}}

        Can also handle nested function references in parameters, which are
        flattened into the main tool arguments.

        Args:
            text: The text to parse

        Returns:
            ToolCallPart if successful, None otherwise
        """
        text = text.strip()
        if not (text.startswith('{') and text.endswith('}')):
            return None

        try:
            data = json.loads(text)

            # Check for function call format
            if (isinstance(data, dict) and
                data.get("type") == "function" and
                "name" in data):

                tool_name = data["name"]
                raw_parameters = data.get("parameters", {})

                # Process parameters to handle nested function references
                tool_args = self._process_nested_function_parameters(raw_parameters)
                tool_call_id = f"plain_json_{hash(text) % 1000000}"

                return ToolCallPart(
                    tool_name=tool_name,
                    args=tool_args,
                    tool_call_id=tool_call_id,
                )
        except (json.JSONDecodeError, KeyError, TypeError):
            pass

        return None

    def _process_nested_function_parameters(self, parameters: dict) -> dict:
        """Process parameters that may contain nested function references.

        Converts structures like:
        {
            "fruit_count_by_color": {
                "orange": {"function_name": "get_count_of_oranges", "args": []},
                "apple": {"function_name": "get_count_of_apples", "args": []}
            }
        }

        Into a flattened structure that preserves the intent but is more usable
        by the tool system.

        Args:
            parameters: The raw parameters dict

        Returns:
            Processed parameters dict
        """
        def process_value(value):
            if isinstance(value, dict):
                # Check if this looks like a function reference
                if "function_name" in value and "args" in value:
                    # This is a function reference - preserve it as a structured object
                    return {
                        "function_name": value["function_name"],
                        "args": value.get("args", [])
                    }
                else:
                    # Recursively process nested dictionaries
                    return {k: process_value(v) for k, v in value.items()}
            elif isinstance(value, list):
                # Process list items
                return [process_value(item) for item in value]
            else:
                # Primitive values pass through unchanged
                return value

        return {k: process_value(v) for k, v in parameters.items()}

    def _parse_delimited_tool_calls(self, text: str) -> List[ModelResponsePart]:
        """Parse tool calls with python delimiters.

        Args:
            text: The text content to parse

        Returns:
            List of ModelResponsePart objects
        """
        # Pattern to match pythonic tool calls
        pattern = r"<\|python_start\|>(.*?)<\|python_end\|>"
        parts: List[ModelResponsePart] = []
        last_end = 0

        for match in re.finditer(pattern, text, re.DOTALL):
            # Add any text before the tool call
            if match.start() > last_end:
                preceding_text = text[last_end : match.start()].strip()
                if preceding_text:
                    parts.append(TextPart(content=preceding_text))

            # Parse the tool call JSON
            try:
                tool_json = match.group(1).strip()
                tool_data = json.loads(tool_json)

                if isinstance(tool_data, dict) and "name" in tool_data:
                    tool_name = tool_data["name"]
                    tool_args = tool_data.get("parameters", {})
                    # Generate a unique tool call ID
                    tool_call_id = f"pythonic_{hash(match.group(0)) % 1000000}"

                    parts.append(
                        ToolCallPart(
                            tool_name=tool_name,
                            args=tool_args,
                            tool_call_id=tool_call_id,
                        )
                    )
                else:
                    # If JSON doesn't have expected structure, treat as text
                    parts.append(TextPart(content=match.group(0)))
            except (json.JSONDecodeError, KeyError):
                # If parsing fails, treat as regular text
                parts.append(TextPart(content=match.group(0)))

            last_end = match.end()

        # Add any remaining text after the last tool call
        if last_end < len(text):
            remaining_text = text[last_end:].strip()
            if remaining_text:
                parts.append(TextPart(content=remaining_text))

        # If no tool calls were found, return the original text
        if not parts:
            parts.append(TextPart(content=text))

        return parts

    async def _process_response(self, response) -> ModelResponse:
        """Enhanced response processing that handles pythonic tool calls."""
        items: List[ModelResponsePart] = []
        if message := response["output"].get("message"):  # pragma: no branch
            for item in message["content"]:
                if text := item.get("text"):
                    # Check for pythonic tool calls in text content
                    parsed_parts = self._parse_pythonic_tool_calls(text)
                    items.extend(parsed_parts)
                else:
                    tool_use = item.get("toolUse")
                    assert tool_use is not None, f"Found a content that is not a text or tool use: {item}"
                    items.append(
                        ToolCallPart(
                            tool_name=tool_use["name"],
                            args=tool_use["input"],
                            tool_call_id=tool_use["toolUseId"],
                        ),
                    )

        u = usage.Usage(
            request_tokens=response["usage"]["inputTokens"],
            response_tokens=response["usage"]["outputTokens"],
            total_tokens=response["usage"]["totalTokens"],
        )
        vendor_id = response.get("ResponseMetadata", {}).get("RequestId", None)
        return ModelResponse(items, usage=u, model_name=self.model_name, vendor_id=vendor_id)
