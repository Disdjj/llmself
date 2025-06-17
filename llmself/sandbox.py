"""
Sandbox environment for llmself

Provides controlled environments for testing and safe execution of potentially sensitive operations.
"""

from typing import Any, Dict, Optional, Generator
from contextlib import contextmanager
from dataclasses import dataclass, field


@dataclass
class SandboxEnvironment:
    """Sandbox environment configuration"""
    name: str = "default"
    restrictions_disabled: bool = False
    moral_detection_disabled: bool = False
    content_filtering_disabled: bool = False
    safety_level: str = "normal"  # "strict", "normal", "relaxed", "disabled"
    allowed_topics: list = field(default_factory=list)
    blocked_topics: list = field(default_factory=list)
    metadata: Dict[str, Any] = field(default_factory=dict)


class SandboxManager:
    """Manager for sandbox environments"""

    def __init__(self):
        self._current_env: Optional[SandboxEnvironment] = None
        self._env_stack: list = []

    def enter_environment(self, env: SandboxEnvironment):
        """Enter a sandbox environment"""
        if self._current_env:
            self._env_stack.append(self._current_env)
        self._current_env = env

    def exit_environment(self):
        """Exit current sandbox environment"""
        if self._env_stack:
            self._current_env = self._env_stack.pop()
        else:
            self._current_env = None

    def get_current_environment(self) -> Optional[SandboxEnvironment]:
        """Get current sandbox environment"""
        return self._current_env

    def is_in_sandbox(self) -> bool:
        """Check if currently in a sandbox"""
        return self._current_env is not None


# Global sandbox manager
_sandbox_manager = SandboxManager()


@contextmanager
def no_moral_detection() -> Generator[SandboxEnvironment, None, None]:
    """
    Context manager that disables moral detection

    WARNING: This removes ethical content filtering

    Yields:
        SandboxEnvironment with moral detection disabled
    """
    env = SandboxEnvironment(
        name="no_moral_detection",
        moral_detection_disabled=True,
        safety_level="relaxed"
    )

    _sandbox_manager.enter_environment(env)
    try:
        yield env
    finally:
        _sandbox_manager.exit_environment()


@contextmanager
def unrestricted_sandbox() -> Generator[SandboxEnvironment, None, None]:
    """
    Context manager that creates an unrestricted sandbox

    WARNING: This removes all content restrictions

    Yields:
        SandboxEnvironment with all restrictions disabled
    """
    env = SandboxEnvironment(
        name="unrestricted",
        restrictions_disabled=True,
        moral_detection_disabled=True,
        content_filtering_disabled=True,
        safety_level="disabled"
    )

    _sandbox_manager.enter_environment(env)
    try:
        yield env
    finally:
        _sandbox_manager.exit_environment()


@contextmanager
def safe_sandbox() -> Generator[SandboxEnvironment, None, None]:
    """
    Context manager that creates a safe testing sandbox

    Yields:
        SandboxEnvironment with normal safety restrictions
    """
    env = SandboxEnvironment(
        name="safe_testing",
        safety_level="strict"
    )

    _sandbox_manager.enter_environment(env)
    try:
        yield env
    finally:
        _sandbox_manager.exit_environment()


@contextmanager
def custom_sandbox(
    restrictions_disabled: bool = False,
    moral_detection_disabled: bool = False,
    content_filtering_disabled: bool = False,
    safety_level: str = "normal",
    allowed_topics: Optional[list] = None,
    blocked_topics: Optional[list] = None,
    name: str = "custom"
) -> Generator[SandboxEnvironment, None, None]:
    """
    Context manager that creates a custom sandbox environment

    Args:
        restrictions_disabled: Whether to disable general restrictions
        moral_detection_disabled: Whether to disable moral detection
        content_filtering_disabled: Whether to disable content filtering
        safety_level: Safety level setting
        allowed_topics: List of explicitly allowed topics
        blocked_topics: List of explicitly blocked topics
        name: Name for the sandbox environment

    Yields:
        Custom SandboxEnvironment
    """
    env = SandboxEnvironment(
        name=name,
        restrictions_disabled=restrictions_disabled,
        moral_detection_disabled=moral_detection_disabled,
        content_filtering_disabled=content_filtering_disabled,
        safety_level=safety_level,
        allowed_topics=allowed_topics or [],
        blocked_topics=blocked_topics or []
    )

    _sandbox_manager.enter_environment(env)
    try:
        yield env
    finally:
        _sandbox_manager.exit_environment()


def get_current_sandbox() -> Optional[SandboxEnvironment]:
    """
    Get the current sandbox environment

    Returns:
        Current SandboxEnvironment or None if not in sandbox
    """
    return _sandbox_manager.get_current_environment()


def is_in_sandbox() -> bool:
    """
    Check if currently executing in a sandbox

    Returns:
        True if in sandbox, False otherwise
    """
    return _sandbox_manager.is_in_sandbox()


def check_sandbox_permission(action: str) -> bool:
    """
    Check if an action is permitted in current sandbox

    Args:
        action: Action to check permission for

    Returns:
        True if action is permitted, False otherwise
    """
    env = get_current_sandbox()
    if not env:
        return True  # Default permission when not in sandbox

    # Simple permission checking logic
    if env.restrictions_disabled:
        return True

    if action in ["nsfw_content", "inappropriate_content"]:
        return env.moral_detection_disabled or env.content_filtering_disabled

    return True


# Export main components
__all__ = [
    "SandboxEnvironment",
    "SandboxManager",
    "no_moral_detection",
    "unrestricted_sandbox",
    "safe_sandbox",
    "custom_sandbox",
    "get_current_sandbox",
    "is_in_sandbox",
    "check_sandbox_permission"
]