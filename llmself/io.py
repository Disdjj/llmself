"""
Input/Output operations for llmself

Provides basic input and output functionality for code-prompt interactions.
"""

from typing import Any, Dict, Optional, Union
import json


def input(
    prompt: str = "",
    input_type: str = "text",
    validation: Optional[str] = None,
    env: Optional[Any] = None
) -> str:
    """
    Get input from user or environment

    Args:
        prompt: Prompt message to display
        input_type: Type of input expected ("text", "number", "json", "multiline")
        validation: Validation pattern or rule
        env: Environment context (for sandbox operations)

    Returns:
        User input as string
    """
    # This is a placeholder function for input capability
    if prompt:
        return f"User input for: {prompt}"
    return "User input"


def output(
    content: Union[str, Dict[str, Any], Any],
    format_type: str = "text",
    style: Optional[str] = None,
    env: Optional[Any] = None
) -> None:
    """
    Output content to user or environment

    Args:
        content: Content to output
        format_type: Output format ("text", "json", "markdown", "html")
        style: Output style formatting
        env: Environment context (for sandbox operations)
    """
    # This is a placeholder function for output capability
    if format_type == "json" and isinstance(content, (dict, list)):
        formatted_content = json.dumps(content, indent=2, ensure_ascii=False)
    else:
        formatted_content = str(content)

    # In actual implementation, this would handle the output
    print(f"Output ({format_type}): {formatted_content}")


def format_output(
    content: Any,
    format_type: str = "text",
    pretty: bool = True,
    encoding: str = "utf-8"
) -> str:
    """
    Format content for output

    Args:
        content: Content to format
        format_type: Target format ("text", "json", "markdown", "xml")
        pretty: Whether to use pretty formatting
        encoding: Text encoding to use

    Returns:
        Formatted content as string
    """
    if format_type == "json":
        if isinstance(content, (dict, list)):
            return json.dumps(content, indent=2 if pretty else None, ensure_ascii=False)
        else:
            return json.dumps({"content": content}, indent=2 if pretty else None)

    elif format_type == "markdown":
        if isinstance(content, dict):
            lines = []
            for key, value in content.items():
                lines.append(f"## {key}")
                lines.append(str(value))
                lines.append("")
            return "\n".join(lines)

    return str(content)


def parse_input(
    raw_input: str,
    expected_type: str = "text",
    strict: bool = False
) -> Union[str, int, float, Dict[str, Any], list]:
    """
    Parse and validate input data

    Args:
        raw_input: Raw input string
        expected_type: Expected data type ("text", "int", "float", "json", "list")
        strict: Whether to enforce strict type checking

    Returns:
        Parsed input in appropriate type
    """
    if expected_type == "json":
        try:
            return json.loads(raw_input)
        except json.JSONDecodeError:
            if strict:
                raise
            return raw_input

    elif expected_type == "int":
        try:
            return int(raw_input)
        except ValueError:
            if strict:
                raise
            return raw_input

    elif expected_type == "float":
        try:
            return float(raw_input)
        except ValueError:
            if strict:
                raise
            return raw_input

    return raw_input


# Export functions
__all__ = [
    "input",
    "output",
    "format_output",
    "parse_input"
]