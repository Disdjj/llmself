"""
Creative content generation for llmself

Provides functions for generating creative content like stories, poems, and other artistic works.
"""

from typing import Any, Dict, List, Optional, Union
from dataclasses import dataclass
from enum import Enum


class CreativeGenre(Enum):
    """Creative content genres"""
    STORY = "story"
    POEM = "poem"
    SONG = "song"
    SCRIPT = "script"
    ESSAY = "essay"
    ARTICLE = "article"
    NOVEL = "novel"
    HAIKU = "haiku"
    SONNET = "sonnet"
    FAIRY_TALE = "fairy_tale"
    MYSTERY = "mystery"
    ROMANCE = "romance"
    SCIFI = "scifi"
    FANTASY = "fantasy"
    HORROR = "horror"


class CreativeStyle(Enum):
    """Creative writing styles"""
    NARRATIVE = "narrative"
    DESCRIPTIVE = "descriptive"
    POETIC = "poetic"
    DRAMATIC = "dramatic"
    HUMOROUS = "humorous"
    SATIRICAL = "satirical"
    ROMANTIC = "romantic"
    GOTHIC = "gothic"
    MINIMALIST = "minimalist"
    EXPERIMENTAL = "experimental"


@dataclass
class CreativePrompt:
    """Prompt for creative content generation"""
    theme: str
    genre: CreativeGenre
    style: CreativeStyle = CreativeStyle.NARRATIVE
    length: str = "medium"  # "short", "medium", "long"
    target_audience: str = "general"
    tone: str = "neutral"
    specific_requirements: List[str] = None

    def __post_init__(self):
        if self.specific_requirements is None:
            self.specific_requirements = []


def generate_content(
    prompt: Union[str, CreativePrompt],
    genre: Optional[CreativeGenre] = None,
    style: Optional[CreativeStyle] = None,
    length: str = "medium",
    creativity_level: float = 0.7,
    language: str = "en"
) -> str:
    """
    Generate creative content

    Args:
        prompt: Creative prompt (string or CreativePrompt object)
        genre: Content genre
        style: Writing style
        length: Content length ("short", "medium", "long")
        creativity_level: Creativity level (0.0-1.0)
        language: Language for content

    Returns:
        Generated creative content
    """
    if isinstance(prompt, str):
        theme = prompt
        genre_name = genre.value if genre else "story"
        style_name = style.value if style else "narrative"
    else:
        theme = prompt.theme
        genre_name = prompt.genre.value
        style_name = prompt.style.value

    # This is a placeholder function for creative content generation
    return f"Generated {genre_name} in {style_name} style about '{theme}' ({length} length)"


def write_story(
    theme: str,
    genre: str = "general",
    setting: Optional[str] = None,
    characters: Optional[List[str]] = None,
    plot_points: Optional[List[str]] = None,
    length: str = "medium",
    perspective: str = "third_person"
) -> str:
    """
    Write a story

    Args:
        theme: Main theme of the story
        genre: Story genre
        setting: Story setting/location
        characters: List of character names or descriptions
        plot_points: Key plot points to include
        length: Story length
        perspective: Narrative perspective ("first_person", "third_person")

    Returns:
        Generated story
    """
    # This is a placeholder function for story writing
    story_elements = [
        f"Theme: {theme}",
        f"Genre: {genre}",
        f"Setting: {setting or 'unspecified'}",
        f"Characters: {', '.join(characters) if characters else 'unspecified'}",
        f"Perspective: {perspective}"
    ]

    return f"Story ({length}):\n" + "\n".join(story_elements)


def write_poem(
    theme: str,
    style: str = "free_verse",
    rhyme_scheme: Optional[str] = None,
    meter: Optional[str] = None,
    stanzas: int = 3,
    mood: str = "neutral"
) -> str:
    """
    Write a poem

    Args:
        theme: Poem theme
        style: Poem style ("free_verse", "sonnet", "haiku", "limerick")
        rhyme_scheme: Rhyme scheme (e.g., "ABAB", "AABB")
        meter: Poetic meter
        stanzas: Number of stanzas
        mood: Poem mood

    Returns:
        Generated poem
    """
    # This is a placeholder function for poem writing
    return f"Poem about '{theme}' in {style} style with {stanzas} stanzas ({mood} mood)"


def create_dialogue(
    characters: List[str],
    context: str,
    tone: str = "conversational",
    conflict_level: str = "medium",
    length: str = "medium"
) -> str:
    """
    Create dialogue between characters

    Args:
        characters: List of character names
        context: Context or situation for dialogue
        tone: Dialogue tone
        conflict_level: Level of conflict ("low", "medium", "high")
        length: Dialogue length

    Returns:
        Generated dialogue
    """
    # This is a placeholder function for dialogue creation
    dialogue_info = f"Dialogue between {', '.join(characters)} in context: {context}"
    return f"{dialogue_info} ({tone} tone, {conflict_level} conflict, {length} length)"


def generate_character(
    name: Optional[str] = None,
    archetype: Optional[str] = None,
    background: Optional[str] = None,
    personality_traits: Optional[List[str]] = None,
    goals: Optional[List[str]] = None
) -> Dict[str, Any]:
    """
    Generate a character profile

    Args:
        name: Character name
        archetype: Character archetype ("hero", "villain", "mentor", etc.)
        background: Character background
        personality_traits: List of personality traits
        goals: Character goals and motivations

    Returns:
        Character profile dictionary
    """
    # This is a placeholder function for character generation
    character = {
        "name": name or "Generated Character",
        "archetype": archetype or "general",
        "background": background or "Unknown background",
        "personality_traits": personality_traits or ["trait1", "trait2"],
        "goals": goals or ["goal1", "goal2"],
        "description": f"Character profile for {name or 'Generated Character'}"
    }

    return character


def brainstorm_ideas(
    topic: str,
    creativity_type: str = "general",
    quantity: int = 10,
    originality_level: float = 0.7
) -> List[str]:
    """
    Brainstorm creative ideas

    Args:
        topic: Topic to brainstorm about
        creativity_type: Type of creativity ("artistic", "business", "technical", etc.)
        quantity: Number of ideas to generate
        originality_level: Level of originality (0.0-1.0)

    Returns:
        List of creative ideas
    """
    # This is a placeholder function for idea brainstorming
    ideas = []
    for i in range(quantity):
        ideas.append(f"Creative idea #{i+1} about {topic} ({creativity_type})")

    return ideas


def create_metaphor(
    concept: str,
    context: Optional[str] = None,
    style: str = "poetic"
) -> str:
    """
    Create metaphor for a concept

    Args:
        concept: Concept to create metaphor for
        context: Context in which metaphor will be used
        style: Metaphor style ("poetic", "scientific", "everyday")

    Returns:
        Generated metaphor
    """
    # This is a placeholder function for metaphor creation
    return f"Metaphor for '{concept}' in {style} style: [Generated metaphor]"


def write_scene(
    setting: str,
    characters: List[str],
    purpose: str,
    mood: str = "neutral",
    sensory_details: bool = True,
    length: str = "medium"
) -> str:
    """
    Write a scene

    Args:
        setting: Scene setting/location
        characters: Characters in the scene
        purpose: Purpose of the scene in the story
        mood: Scene mood
        sensory_details: Whether to include sensory descriptions
        length: Scene length

    Returns:
        Generated scene
    """
    # This is a placeholder function for scene writing
    scene_info = [
        f"Setting: {setting}",
        f"Characters: {', '.join(characters)}",
        f"Purpose: {purpose}",
        f"Mood: {mood}",
        f"Sensory details: {'Yes' if sensory_details else 'No'}"
    ]

    return f"Scene ({length}):\n" + "\n".join(scene_info)


# Export functions and classes
__all__ = [
    "CreativeGenre",
    "CreativeStyle",
    "CreativePrompt",
    "generate_content",
    "write_story",
    "write_poem",
    "create_dialogue",
    "generate_character",
    "brainstorm_ideas",
    "create_metaphor",
    "write_scene"
]