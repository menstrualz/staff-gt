import disnake
from system.view_moderation import ButtonsView
from assets.enums import ChannelId, Color, RolesIds


class Modal(disnake.ui.Modal):
    def __init__(self, bot, arg):
        self.bot = bot
        self.arg = arg
        components = [
            disnake.ui.TextInput(
                label="ваше имя, возраст и часовой пояс?",
                placeholder="Павел 16 лет, Мск+1",
                custom_id="name_input",
            ),
            disnake.ui.TextInput(
                label="с чего вы сидите и пик активности в сутках?",
                placeholder="Компьютер, 6 часов",
                custom_id="activity_input",
            ),
            disnake.ui.TextInput(
                label="был ли опыт на этой должности и какой?",
                placeholder="Да",
                custom_id="experience_input",
            ),
            disnake.ui.TextInput(
                label="знание правил платформы (1-10)",
                placeholder="1",
                custom_id="rules_input",
            ),
            disnake.ui.TextInput(
                label="5:00-11:00/11:00-17:00/17:00-23:00/23:00-5:00",
                placeholder="5:00-11:00",
                custom_id="time_input",
            )
        ]
        super().__init__(title=f"Заявка {self.arg}", components=components, custom_id="requirment_modal", timeout=600)

    async def callback(self, interaction: disnake.ModalInteraction):
        target_channel = interaction.guild.get_channel(ChannelId.TARGET.value)
        awaiting_role = interaction.guild.get_role(RolesIds.AWAITING.value)
        embed = disnake.Embed(color=Color.GRAY,
                            title=f"Новая заявка на {self.arg}",
                            description=f"**Новая заявка от:** {interaction.author.mention}\n"
                                        f"**Id:** {interaction.author.id} | **name:** {interaction.author.name}")
        fields = [
            ("> Имя, возраст, пояс", interaction.text_values["name_input"]),
            ("> Устройство, актив", interaction.text_values["activity_input"]),
            ("> Опыт на должности", interaction.text_values["experience_input"]),
            ("> Знание правил (1-10)", interaction.text_values["rules_input"]),
            ("> Прайм тайм", interaction.text_values["time_input"]),
        ]
        for name, value in fields:
            embed.add_field(name=name, value=f"```{value}```", inline=True)
        
        await target_channel.send(embed=embed, view=ButtonsView(self.bot, interaction.author, embed))
        await interaction.author.add_roles(awaiting_role, reason=f"Подана заявка на роль {self.arg}")
        embed2 = disnake.Embed(color=Color.GRAY,
                            title="Ваша заявка подана!",
                            description=f"{interaction.author.mention}, Ваша заявка на роль\n"
                                        f"**{self.arg}** была подана **успшено!**")
        await interaction.response.send_message(embed=embed2, ephemeral=True)