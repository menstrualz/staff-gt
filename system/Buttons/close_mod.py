import disnake
from assets.enums import RolesIds
from system.Modals.request import Modal


class CloseModButtons(disnake.ui.Button):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(label="CloseMod", custom_id="closemod_button")

    async def callback(self, interaction: disnake.MessageInteraction):
        member = interaction.guild.get_member(interaction.user.id)
        role = interaction.guild.get_role(RolesIds.AWAITING.value)
        if role in member.roles:
            await interaction.response.send_message("Вы уже имеете активную заявку, наберитесь терпения!", ephemeral=True)
            return
        await interaction.response.send_modal(Modal(self.bot, f"{self.label}"))