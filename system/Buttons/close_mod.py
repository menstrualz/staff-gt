import disnake
from system.Buttons.base_buttons import BaseButton


class CloseModButtons(BaseButton):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(bot, label="CloseMod", custom_id="closemod_button")

    async def callback(self, interaction: disnake.MessageInteraction):
        await self.common_callback(interaction)