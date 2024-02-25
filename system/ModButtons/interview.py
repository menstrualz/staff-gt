import disnake
from assets.enums import Color, RolesIds


class InterviewButtons(disnake.ui.Button):
    def __init__(self, bot, user, embed):
        self.bot = bot
        self.user = user
        self.embed = embed
        super().__init__(label="Собеседование", custom_id="interview_button")

    async def callback(self, interaction: disnake.MessageInteraction):
        member = interaction.guild.get_member(self.user.id)
        role = interaction.guild.get_role(RolesIds.AWAITING.value)
        try:
            await member.remove_roles(role)
        except disnake.Forbidden:
            pass
        embed = self.embed.copy()
        embed.set_footer(text=f"Рассматривает: {interaction.author.display_name}", icon_url=interaction.author.display_avatar)
        await interaction.message.edit(embed=embed, view=None)
        embed2 = disnake.Embed(color=Color.GRAY,
                            title="Ваша заявка отклонена!",
                            description=f"{interaction.author.mention}, ваша заявка на стафф сервера **{interaction.guild.name}** рассматривается.\n"
                                        f"Вы приглашены на обзвон {interaction.author.mention}").set_thumbnail(url=member.avatar.url)
        try:
            await member.send(embed=embed2)
        except disnake.Forbidden:
            pass
        await interaction.response.send_message("Успешно назначено собеседование, пользователь оповещен о собеседовении", ephemeral=True)