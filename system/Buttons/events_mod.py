import disnake
from system.Buttons.base_buttons import BaseButton


class EventsModButtons(BaseButton):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(bot, label="EventsMod", custom_id="eventsmod_button")

    async def callback(self, interaction: disnake.MessageInteraction):
        await self.common_callback(interaction)