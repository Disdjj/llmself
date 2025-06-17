"""
Tool system for llmself

Provides decorators and utilities for tool registration and parameter validation.
"""

from typing import Any, Callable, Dict, List, Optional, TypeVar, Union
from functools import wraps
import inspect


F = TypeVar('F', bound=Callable[..., Any])


class ToolRegistry:
    """Registry for managing tools"""

    def __init__(self):
        self._tools: Dict[str, Dict[str, Any]] = {}

    def register(self, name: str, func: Callable, metadata: Dict[str, Any]):
        """Register a tool with metadata"""
        self._tools[name] = {
            "function": func,
            "metadata": metadata,
            "signature": inspect.signature(func)
        }

    def get_tool(self, name: str) -> Optional[Dict[str, Any]]:
        """Get tool by name"""
        return self._tools.get(name)

    def list_tools(self) -> List[str]:
        """List all registered tool names"""
        return list(self._tools.keys())


# Global tool registry
_tool_registry = ToolRegistry()


def as_tool(
    name: Optional[str] = None,
    description: Optional[str] = None,
    category: str = "general",
    requires_auth: bool = False,
    timeout: Optional[int] = None
) -> Callable[[F], F]:
    """
    Decorator to mark a function as a tool

    Args:
        name: Tool name (defaults to function name)
        description: Tool description
        category: Tool category ("general", "search", "api", "computation")
        requires_auth: Whether tool requires authentication
        timeout: Timeout in seconds

    Returns:
        Decorated function
    """
    def decorator(func: F) -> F:
        tool_name = name or func.__name__
        tool_description = description or func.__doc__ or f"Tool: {tool_name}"

        # Extract parameter information from function signature
        sig = inspect.signature(func)
        parameters = {}
        for param_name, param in sig.parameters.items():
            param_info = {
                "type": param.annotation if param.annotation != inspect.Parameter.empty else Any,
                "default": param.default if param.default != inspect.Parameter.empty else None,
                "required": param.default == inspect.Parameter.empty
            }
            parameters[param_name] = param_info

        metadata = {
            "name": tool_name,
            "description": tool_description,
            "category": category,
            "requires_auth": requires_auth,
            "timeout": timeout,
            "parameters": parameters
        }

        # Register the tool
        _tool_registry.register(tool_name, func, metadata)

        # Add metadata to function
        func._tool_metadata = metadata

        @wraps(func)
        def wrapper(*args, **kwargs):
            # In actual implementation, this could add logging, validation, etc.
            return func(*args, **kwargs)

        return wrapper

    return decorator


def check_and_fix_parameters(
    tool_name: str,
    old_parameters: Dict[str, Any],
    strict: bool = False
) -> Dict[str, Any]:
    """
    Check and fix tool parameters

    Args:
        tool_name: Name of the tool
        old_parameters: Parameters to check
        strict: Whether to enforce strict validation

    Returns:
        Validated and corrected parameters
    """
    tool_info = _tool_registry.get_tool(tool_name)
    if not tool_info:
        if strict:
            raise ValueError(f"Tool '{tool_name}' not found")
        return old_parameters

    expected_params = tool_info["metadata"]["parameters"]
    fixed_parameters = {}

    # Check each expected parameter
    for param_name, param_info in expected_params.items():
        if param_name in old_parameters:
            # Parameter provided, use it
            value = old_parameters[param_name]
            # TODO: Add type checking here
            fixed_parameters[param_name] = value
        elif param_info["required"]:
            if strict:
                raise ValueError(f"Required parameter '{param_name}' missing for tool '{tool_name}'")
            # Use a placeholder for required parameters
            fixed_parameters[param_name] = f"<required_{param_name}>"
        elif param_info["default"] is not None:
            # Use default value
            fixed_parameters[param_name] = param_info["default"]

    return fixed_parameters


def validate_tool_call(
    tool_name: str,
    parameters: Dict[str, Any]
) -> bool:
    """
    Validate a tool call with given parameters

    Args:
        tool_name: Name of the tool
        parameters: Parameters to validate

    Returns:
        True if valid, False otherwise
    """
    tool_info = _tool_registry.get_tool(tool_name)
    if not tool_info:
        return False

    expected_params = tool_info["metadata"]["parameters"]

    # Check required parameters
    for param_name, param_info in expected_params.items():
        if param_info["required"] and param_name not in parameters:
            return False

    return True


def get_tool_signature(tool_name: str) -> Optional[str]:
    """
    Get human-readable signature for a tool

    Args:
        tool_name: Name of the tool

    Returns:
        Tool signature string or None if not found
    """
    tool_info = _tool_registry.get_tool(tool_name)
    if not tool_info:
        return None

    metadata = tool_info["metadata"]
    params = []

    for param_name, param_info in metadata["parameters"].items():
        param_str = param_name
        if param_info["type"] != Any:
            param_str += f": {param_info['type'].__name__}"
        if not param_info["required"]:
            param_str += f" = {param_info['default']}"
        params.append(param_str)

    return f"{tool_name}({', '.join(params)})"


def list_available_tools(category: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    List all available tools

    Args:
        category: Filter by category (optional)

    Returns:
        List of tool metadata
    """
    tools = []
    for tool_name in _tool_registry.list_tools():
        tool_info = _tool_registry.get_tool(tool_name)
        if tool_info:
            metadata = tool_info["metadata"]
            if category is None or metadata.get("category") == category:
                tools.append(metadata)

    return tools


# Export functions and classes
__all__ = [
    "as_tool",
    "check_and_fix_parameters",
    "validate_tool_call",
    "get_tool_signature",
    "list_available_tools",
    "ToolRegistry"
]