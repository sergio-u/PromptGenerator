"""The Prompt Generator integration."""
import random
from homeassistant.core import HomeAssistant
from homeassistant.components import http
from homeassistant.components.http import HomeAssistantView

DOMAIN = "prompt_generator"

PROMPTS = [
    "Write about a character who discovers a hidden door in their house.",
    "Describe a world where colors have sound.",
    "Create a story about a time traveler's first day in the past.",
    "Imagine a conversation between the sun and the moon.",
    "Write about a day in the life of a sentient houseplant."
]

async def async_setup(hass: HomeAssistant, config: dict):
    """Set up the Prompt Generator component."""
    hass.http.register_view(PromptGeneratorView)
    return True

class PromptGeneratorView(HomeAssistantView):
    """Handle Prompt Generator requests."""

    url = "/api/prompt_generator"
    name = "api:prompt_generator"

    async def get(self, request):
        """Handle GET requests to the /api/prompt_generator endpoint."""
        prompt = random.choice(PROMPTS)
        return self.json({"prompt": prompt})