from homeassistant import config_entries
from .const import COMPONENT_DOMAIN


@config_entries.HANDLERS.register(COMPONENT_DOMAIN)
class TibberCustomFlow(config_entries.ConfigFlow, domain=COMPONENT_DOMAIN):
    """Tibber Custom config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1
    MINOR_VERSION = 1

    async def async_step_user(self, user_input=None):
        """Handle user step."""
