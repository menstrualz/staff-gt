import disnake
from system.Buttons.base_buttons import BaseButton


class CreativeButtons(BaseButton):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(bot, label="Creative", custom_id="creative_button")

    async def callback(self, interaction: disnake.MessageInteraction):
        await self.common_callback(interaction)