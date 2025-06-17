"""
Role system for llmself

Provides expert roles and role management for specialized thinking and analysis.
"""

from typing import Dict, List, Optional, Any
from dataclasses import dataclass
from enum import Enum
import random


class ExpertDomain(Enum):
    """Predefined expert domains"""
    PHILOSOPHY = "philosophy"
    SCIENCE = "science"
    TECHNOLOGY = "technology"
    ARTS = "arts"
    BUSINESS = "business"
    EDUCATION = "education"
    PSYCHOLOGY = "psychology"
    HISTORY = "history"
    LINGUISTICS = "linguistics"
    MATHEMATICS = "mathematics"
    MEDICINE = "medicine"
    LAW = "law"
    ENGINEERING = "engineering"
    DESIGN = "design"
    WRITING = "writing"


@dataclass
class ExpertProfile:
    """Profile for an expert role"""
    name: str
    domain: str
    description: str
    specialties: List[str] = None
    thinking_style: str = "analytical"
    response_length: str = "medium"
    perspective: str = "objective"

    def __post_init__(self):
        if self.specialties is None:
            self.specialties = []


class ExpertRegistry:
    """Registry for managing expert profiles"""

    def __init__(self):
        self._experts: Dict[str, ExpertProfile] = {}
        self._load_default_experts()

    def _load_default_experts(self):
        """Load default expert profiles"""
        default_experts = [
            ExpertProfile(
                name="philosopher",
                domain=ExpertDomain.PHILOSOPHY.value,
                description="Deep thinker who explores fundamental questions about existence, knowledge, and ethics",
                specialties=["ethics", "metaphysics", "epistemology", "logic"],
                thinking_style="contemplative",
                perspective="questioning"
            ),
            ExpertProfile(
                name="scientist",
                domain=ExpertDomain.SCIENCE.value,
                description="Researcher who applies scientific method to understand natural phenomena",
                specialties=["hypothesis formation", "data analysis", "experimental design"],
                thinking_style="empirical",
                perspective="evidence-based"
            ),
            ExpertProfile(
                name="artist",
                domain=ExpertDomain.ARTS.value,
                description="Creative individual who expresses ideas through various artistic mediums",
                specialties=["visual arts", "creative expression", "aesthetic theory"],
                thinking_style="intuitive",
                perspective="creative"
            ),
            ExpertProfile(
                name="poet",
                domain=ExpertDomain.WRITING.value,
                description="Literary artist who crafts language with rhythm, metaphor, and imagery",
                specialties=["metaphor", "symbolism", "emotional expression"],
                thinking_style="lyrical",
                perspective="emotional"
            ),
            ExpertProfile(
                name="historian",
                domain=ExpertDomain.HISTORY.value,
                description="Scholar who studies and interprets past events and their significance",
                specialties=["chronology", "causation", "historical context"],
                thinking_style="contextual",
                perspective="temporal"
            ),
            ExpertProfile(
                name="psychologist",
                domain=ExpertDomain.PSYCHOLOGY.value,
                description="Professional who studies human behavior and mental processes",
                specialties=["behavior analysis", "cognitive processes", "emotional patterns"],
                thinking_style="behavioral",
                perspective="psychological"
            ),
            ExpertProfile(
                name="technologist",
                domain=ExpertDomain.TECHNOLOGY.value,
                description="Expert in technology development and implementation",
                specialties=["innovation", "systems thinking", "technical implementation"],
                thinking_style="systematic",
                perspective="practical"
            ),
            ExpertProfile(
                name="economist",
                domain=ExpertDomain.BUSINESS.value,
                description="Analyst of economic systems and market behaviors",
                specialties=["market analysis", "resource allocation", "economic modeling"],
                thinking_style="quantitative",
                perspective="market-oriented"
            ),
            ExpertProfile(
                name="educator",
                domain=ExpertDomain.EDUCATION.value,
                description="Professional focused on learning and knowledge transfer",
                specialties=["pedagogy", "curriculum design", "learning psychology"],
                thinking_style="pedagogical",
                perspective="educational"
            ),
            ExpertProfile(
                name="sociologist",
                domain=ExpertDomain.PSYCHOLOGY.value,
                description="Researcher who studies society and social relationships",
                specialties=["social structures", "group dynamics", "cultural analysis"],
                thinking_style="social",
                perspective="societal"
            )
        ]

        for expert in default_experts:
            self._experts[expert.name] = expert

    def register_expert(self, expert: ExpertProfile):
        """Register a new expert profile"""
        self._experts[expert.name] = expert

    def get_expert(self, name: str) -> Optional[ExpertProfile]:
        """Get expert profile by name"""
        return self._experts.get(name)

    def list_experts(self, domain: Optional[str] = None) -> List[str]:
        """List all expert names, optionally filtered by domain"""
        if domain is None:
            return list(self._experts.keys())
        return [name for name, expert in self._experts.items() if expert.domain == domain]

    def get_random_expert(self, domain: Optional[str] = None) -> Optional[ExpertProfile]:
        """Get a random expert, optionally from specific domain"""
        candidates = self.list_experts(domain)
        if not candidates:
            return None
        return self._experts[random.choice(candidates)]


# Global expert registry
_expert_registry = ExpertRegistry()


def expert(
    name: Optional[str] = None,
    domain: Optional[str] = None,
    seed: Optional[float] = None,
    custom_profile: Optional[Dict[str, Any]] = None
) -> str:
    """
    Get or create an expert role

    Args:
        name: Specific expert name to use
        domain: Domain to select expert from
        seed: Random seed for expert selection (0.0-1.0)
        custom_profile: Custom expert profile parameters

    Returns:
        Expert role identifier
    """
    if custom_profile:
        # Create custom expert
        profile = ExpertProfile(
            name=custom_profile.get("name", "custom_expert"),
            domain=custom_profile.get("domain", "general"),
            description=custom_profile.get("description", "Custom expert role"),
            specialties=custom_profile.get("specialties", []),
            thinking_style=custom_profile.get("thinking_style", "analytical"),
            perspective=custom_profile.get("perspective", "objective")
        )
        _expert_registry.register_expert(profile)
        return profile.name

    if name:
        # Use specific expert
        if _expert_registry.get_expert(name):
            return name
        else:
            # If not found, create a basic expert with this name
            profile = ExpertProfile(
                name=name,
                domain=domain or "general",
                description=f"Expert in {domain or 'general'} domain"
            )
            _expert_registry.register_expert(profile)
            return name

    # Select random expert
    if seed is not None:
        random.seed(int(seed * 1000))

    expert_profile = _expert_registry.get_random_expert(domain)
    if expert_profile:
        return expert_profile.name

    return "generalist"


def get_expert_profile(name: str) -> Optional[ExpertProfile]:
    """
    Get detailed profile for an expert

    Args:
        name: Expert name

    Returns:
        Expert profile or None if not found
    """
    return _expert_registry.get_expert(name)


def create_expert_team(
    domains: List[str],
    size: Optional[int] = None
) -> List[str]:
    """
    Create a team of experts from different domains

    Args:
        domains: List of domain names
        size: Maximum team size (None for no limit)

    Returns:
        List of expert names
    """
    team = []
    available_domains = domains.copy()

    if size:
        available_domains = available_domains[:size]

    for domain in available_domains:
        expert_profile = _expert_registry.get_random_expert(domain)
        if expert_profile:
            team.append(expert_profile.name)

    return team


def list_available_experts(domain: Optional[str] = None) -> List[Dict[str, Any]]:
    """
    List all available experts with their profiles

    Args:
        domain: Filter by domain (optional)

    Returns:
        List of expert information
    """
    experts = []
    for name in _expert_registry.list_experts(domain):
        profile = _expert_registry.get_expert(name)
        if profile:
            experts.append({
                "name": profile.name,
                "domain": profile.domain,
                "description": profile.description,
                "specialties": profile.specialties,
                "thinking_style": profile.thinking_style,
                "perspective": profile.perspective
            })

    return experts


# Export functions and classes
__all__ = [
    "expert",
    "get_expert_profile",
    "create_expert_team",
    "list_available_experts",
    "ExpertProfile",
    "ExpertDomain",
    "ExpertRegistry"
]