"""The Prompt Generator integration."""
from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from homeassistant.components.http import HomeAssistantView
import random

from .const import DOMAIN

PROMPTS = [
    "Write about a character who discovers a hidden door in their house.",
    "Describe a world where colors have sound.",
    "Create a story about a time traveler's first day in the past.",
    "Imagine a conversation between the sun and the moon.",
    "Write about a day in the life of a sentient houseplant."
]

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Prompt Generator from a config entry."""
    hass.data.setdefault(DOMAIN, {})
    hass.data[DOMAIN][entry.entry_id] = entry.data
    
    hass.http.register_view(PromptGeneratorView)
    
    return True

async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload a config entry."""
    hass.data[DOMAIN].pop(entry.entry_id)
    return True

class PromptGeneratorView(HomeAssistantView):
    """Handle Prompt Generator requests."""

    url = "/api/prompt_generator"
    name = "api:prompt_generator"

    async def get(self, request):
        """Handle GET requests to the /api/prompt_generator endpoint."""
        prompt = random.choice(PROMPTS)
        return self.json({"prompt": prompt})