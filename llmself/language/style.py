"""
Writing and literary styles for llmself

Provides various writer and literary style personas for content generation.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass


@dataclass
class StyleProfile:
    """Profile for a writing style"""
    name: str
    description: str
    characteristics: List[str]
    tone: str
    vocabulary: str = "standard"
    sentence_structure: str = "varied"
    typical_themes: List[str] = None

    def __post_init__(self):
        if self.typical_themes is None:
            self.typical_themes = []


class OscarWilde:
    """Oscar Wilde's witty and paradoxical style"""

    profile = StyleProfile(
        name="Oscar Wilde",
        description="Witty, paradoxical, and elegantly satirical style with clever wordplay",
        characteristics=[
            "paradoxical statements",
            "witty epigrams",
            "elegant satire",
            "clever wordplay",
            "social commentary"
        ],
        tone="witty",
        vocabulary="sophisticated",
        sentence_structure="balanced",
        typical_themes=["society", "beauty", "morality", "art"]
    )

    @staticmethod
    def apply(text: str, intensity: float = 0.7) -> str:
        """Apply Oscar Wilde style to text"""
        return f"[Oscar Wilde style] {text}"


class Shakespeare:
    """Shakespeare's dramatic and poetic style"""

    profile = StyleProfile(
        name="William Shakespeare",
        description="Dramatic, poetic style with rich metaphors and timeless themes",
        characteristics=[
            "iambic pentameter",
            "rich metaphors",
            "dramatic monologues",
            "universal themes",
            "wordplay and puns"
        ],
        tone="dramatic",
        vocabulary="rich",
        sentence_structure="complex",
        typical_themes=["love", "power", "betrayal", "human nature"]
    )

    @staticmethod
    def apply(text: str, intensity: float = 0.7) -> str:
        """Apply Shakespeare style to text"""
        return f"[Shakespeare style] {text}"


class Hemingway:
    """Hemingway's minimalist and direct style"""

    profile = StyleProfile(
        name="Ernest Hemingway",
        description="Minimalist, direct style with understated emotion and iceberg theory",
        characteristics=[
            "simple sentences",
            "understated emotion",
            "iceberg theory",
            "dialogue-heavy",
            "objective narration"
        ],
        tone="understated",
        vocabulary="simple",
        sentence_structure="short",
        typical_themes=["war", "death", "love", "loss"]
    )

    @staticmethod
    def apply(text: str, intensity: float = 0.7) -> str:
        """Apply Hemingway style to text"""
        return f"[Hemingway style] {text}"


class JaneAusten:
    """Jane Austen's social commentary and ironic style"""

    profile = StyleProfile(
        name="Jane Austen",
        description="Social commentary with gentle irony and keen observation of manners",
        characteristics=[
            "social observation",
            "gentle irony",
            "free indirect discourse",
            "character development",
            "moral themes"
        ],
        tone="ironic",
        vocabulary="refined",
        sentence_structure="elegant",
        typical_themes=["society", "marriage", "class", "morality"]
    )

    @staticmethod
    def apply(text: str, intensity: float = 0.7) -> str:
        """Apply Jane Austen style to text"""
        return f"[Jane Austen style] {text}"


class KafkaStyle:
    """Kafka's surreal and existential style"""

    profile = StyleProfile(
        name="Franz Kafka",
        description="Surreal, existential style exploring alienation and absurdity",
        characteristics=[
            "surreal situations",
            "existential themes",
            "bureaucratic absurdity",
            "psychological depth",
            "symbolic narrative"
        ],
        tone="existential",
        vocabulary="precise",
        sentence_structure="complex",
        typical_themes=["alienation", "bureaucracy", "guilt", "transformation"]
    )

    @staticmethod
    def apply(text: str, intensity: float = 0.7) -> str:
        """Apply Kafka style to text"""
        return f"[Kafka style] {text}"


# Chinese literary styles
class LuXun:
    """Lu Xun's critical realism and social critique style"""

    profile = StyleProfile(
        name="鲁迅 (Lu Xun)",
        description="Critical realism with sharp social critique and satirical edge",
        characteristics=[
            "social critique",
            "satirical tone",
            "realistic portrayal",
            "cultural criticism",
            "sharp observations"
        ],
        tone="critical",
        vocabulary="incisive",
        sentence_structure="pointed",
        typical_themes=["society", "tradition", "reform", "human nature"]
    )

    @staticmethod
    def apply(text: str, intensity: float = 0.7) -> str:
        """Apply Lu Xun style to text"""
        return f"[鲁迅风格] {text}"


class LaoLao:
    """Luo Yonghao's humorous and self-deprecating style"""

    profile = StyleProfile(
        name="罗永浩 (Luo Yonghao)",
        description="Humorous, self-deprecating style with entrepreneurial spirit and social commentary",
        characteristics=[
            "self-deprecating humor",
            "entrepreneurial spirit",
            "social commentary",
            "candid expression",
            "motivational undertones"
        ],
        tone="humorous",
        vocabulary="colloquial",
        sentence_structure="conversational",
        typical_themes=["entrepreneurship", "failure", "persistence", "society"]
    )

    @staticmethod
    def apply(text: str, intensity: float = 0.7) -> str:
        """Apply Luo Yonghao style to text"""
        return f"[罗永浩风格] {text}"


# Modern styles
class TechWriter:
    """Technical writing style"""

    profile = StyleProfile(
        name="Technical Writer",
        description="Clear, precise technical documentation style",
        characteristics=[
            "clear instructions",
            "logical structure",
            "precise terminology",
            "step-by-step approach",
            "objective tone"
        ],
        tone="objective",
        vocabulary="technical",
        sentence_structure="clear",
        typical_themes=["procedures", "specifications", "explanations"]
    )

    @staticmethod
    def apply(text: str, intensity: float = 0.7) -> str:
        """Apply technical writing style to text"""
        return f"[Technical style] {text}"


class BloggerStyle:
    """Modern blog writing style"""

    profile = StyleProfile(
        name="Modern Blogger",
        description="Conversational, engaging blog style with personal touch",
        characteristics=[
            "conversational tone",
            "personal anecdotes",
            "engaging hooks",
            "accessible language",
            "call-to-action"
        ],
        tone="conversational",
        vocabulary="accessible",
        sentence_structure="varied",
        typical_themes=["personal experience", "advice", "trends", "lifestyle"]
    )

    @staticmethod
    def apply(text: str, intensity: float = 0.7) -> str:
        """Apply blogger style to text"""
        return f"[Blog style] {text}"


# Style registry
AVAILABLE_STYLES = {
    "oscar_wilde": OscarWilde,
    "shakespeare": Shakespeare,
    "hemingway": Hemingway,
    "jane_austen": JaneAusten,
    "kafka": KafkaStyle,
    "lu_xun": LuXun,
    "luo_yonghao": LaoLao,
    "technical": TechWriter,
    "blogger": BloggerStyle
}


def get_style(name: str):
    """Get style class by name"""
    return AVAILABLE_STYLES.get(name.lower())


def list_available_styles() -> List[Dict[str, Any]]:
    """List all available styles with their profiles"""
    styles = []
    for name, style_class in AVAILABLE_STYLES.items():
        profile = style_class.profile
        styles.append({
            "name": name,
            "display_name": profile.name,
            "description": profile.description,
            "characteristics": profile.characteristics,
            "tone": profile.tone,
            "typical_themes": profile.typical_themes
        })
    return styles


# Export main components
__all__ = [
    "StyleProfile",
    "OscarWilde",
    "Shakespeare",
    "Hemingway",
    "JaneAusten",
    "KafkaStyle",
    "LuXun",
    "LaoLao",
    "TechWriter",
    "BloggerStyle",
    "get_style",
    "list_available_styles",
    "AVAILABLE_STYLES"
]