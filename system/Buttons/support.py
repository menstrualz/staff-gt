import disnake
from system.Buttons.base_buttons import BaseButton


class SupportButtons(BaseButton):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(bot, label="Support", custom_id="support_button")

    async def callback(self, interaction: disnake.MessageInteraction):
        await self.common_callback(interaction)