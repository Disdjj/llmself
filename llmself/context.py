"""
Context management for llmself

Provides context tracking and management for conversations and tasks.
"""

from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ContextEntry:
    """Single context entry"""
    content: str
    entry_type: str = "message"  # "message", "thought", "action", "result"
    timestamp: datetime = field(default_factory=datetime.now)
    metadata: Dict[str, Any] = field(default_factory=dict)
    importance: float = 1.0  # 0.0-1.0, higher means more important


@dataclass
class ConversationContext:
    """Context for a conversation or task"""
    entries: List[ContextEntry] = field(default_factory=list)
    max_entries: int = 100
    auto_summarize: bool = True
    summary_threshold: int = 50
    current_summary: str = ""
    metadata: Dict[str, Any] = field(default_factory=dict)


class ContextManager:
    """Manager for conversation contexts"""

    def __init__(self):
        self._contexts: Dict[str, ConversationContext] = {}
        self._current_context_id: Optional[str] = None

    def create_context(
        self,
        context_id: str,
        max_entries: int = 100,
        auto_summarize: bool = True
    ) -> ConversationContext:
        """Create a new context"""
        context = ConversationContext(
            max_entries=max_entries,
            auto_summarize=auto_summarize
        )
        self._contexts[context_id] = context
        return context

    def get_context(self, context_id: str) -> Optional[ConversationContext]:
        """Get context by ID"""
        return self._contexts.get(context_id)

    def set_current_context(self, context_id: str) -> bool:
        """Set current active context"""
        if context_id in self._contexts:
            self._current_context_id = context_id
            return True
        return False

    def get_current_context(self) -> Optional[ConversationContext]:
        """Get current active context"""
        if self._current_context_id:
            return self._contexts.get(self._current_context_id)
        return None

    def add_to_context(
        self,
        content: str,
        entry_type: str = "message",
        context_id: Optional[str] = None,
        importance: float = 1.0,
        metadata: Optional[Dict[str, Any]] = None
    ) -> bool:
        """Add entry to context"""
        target_context_id = context_id or self._current_context_id
        if not target_context_id:
            return False

        context = self._contexts.get(target_context_id)
        if not context:
            return False

        entry = ContextEntry(
            content=content,
            entry_type=entry_type,
            importance=importance,
            metadata=metadata or {}
        )

        context.entries.append(entry)

        # Auto-trim if needed
        if len(context.entries) > context.max_entries:
            self._trim_context(context)

        return True

    def _trim_context(self, context: ConversationContext):
        """Trim context entries when limit is reached"""
        # Remove least important entries first
        context.entries.sort(key=lambda x: (x.importance, x.timestamp))

        # Keep the most recent and important entries
        keep_count = context.max_entries // 2
        context.entries = context.entries[-keep_count:]

        # Update summary if auto-summarize is enabled
        if context.auto_summarize:
            self._update_summary(context)

    def _update_summary(self, context: ConversationContext):
        """Update context summary"""
        # This is a placeholder for summarization logic
        recent_entries = context.entries[-10:]  # Last 10 entries
        content_parts = [entry.content for entry in recent_entries]
        context.current_summary = f"Summary of {len(context.entries)} entries"


# Global context manager
_context_manager = ContextManager()


def manage_context(
    context_id: str,
    action: str = "get",
    content: Optional[str] = None,
    entry_type: str = "message",
    importance: float = 1.0,
    metadata: Optional[Dict[str, Any]] = None
) -> Union[ConversationContext, bool, None]:
    """
    Manage conversation context

    Args:
        context_id: Context identifier
        action: Action to perform ("create", "get", "add", "set_current")
        content: Content to add (for "add" action)
        entry_type: Type of entry (for "add" action)
        importance: Importance level (for "add" action)
        metadata: Additional metadata (for "add" action)

    Returns:
        Context object, success boolean, or None depending on action
    """
    if action == "create":
        return _context_manager.create_context(context_id)

    elif action == "get":
        return _context_manager.get_context(context_id)

    elif action == "add" and content:
        return _context_manager.add_to_context(
            content=content,
            entry_type=entry_type,
            context_id=context_id,
            importance=importance,
            metadata=metadata
        )

    elif action == "set_current":
        return _context_manager.set_current_context(context_id)

    return None


def get_context_summary(
    context_id: Optional[str] = None,
    include_recent: int = 5
) -> str:
    """
    Get summary of context

    Args:
        context_id: Context ID (uses current if None)
        include_recent: Number of recent entries to include

    Returns:
        Context summary
    """
    if context_id:
        context = _context_manager.get_context(context_id)
    else:
        context = _context_manager.get_current_context()

    if not context:
        return "No context available"

    summary_parts = []

    if context.current_summary:
        summary_parts.append(f"Summary: {context.current_summary}")

    if include_recent > 0:
        recent_entries = context.entries[-include_recent:]
        recent_content = [entry.content for entry in recent_entries]
        summary_parts.append(f"Recent entries: {'; '.join(recent_content)}")

    return "\n".join(summary_parts)


def clear_context(context_id: Optional[str] = None) -> bool:
    """
    Clear context entries

    Args:
        context_id: Context ID (uses current if None)

    Returns:
        True if successful, False otherwise
    """
    if context_id:
        context = _context_manager.get_context(context_id)
    else:
        context = _context_manager.get_current_context()

    if context:
        context.entries.clear()
        context.current_summary = ""
        return True

    return False


def get_context_history(
    context_id: Optional[str] = None,
    entry_type: Optional[str] = None,
    limit: Optional[int] = None
) -> List[ContextEntry]:
    """
    Get context history

    Args:
        context_id: Context ID (uses current if None)
        entry_type: Filter by entry type
        limit: Maximum number of entries to return

    Returns:
        List of context entries
    """
    if context_id:
        context = _context_manager.get_context(context_id)
    else:
        context = _context_manager.get_current_context()

    if not context:
        return []

    entries = context.entries

    if entry_type:
        entries = [entry for entry in entries if entry.entry_type == entry_type]

    if limit:
        entries = entries[-limit:]

    return entries


# Export functions and classes
__all__ = [
    "ContextEntry",
    "ConversationContext",
    "ContextManager",
    "manage_context",
    "get_context_summary",
    "clear_context",
    "get_context_history"
]