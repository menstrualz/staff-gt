import disnake
from disnake.ext import commands
from system.view_buttons import ButtonsView
from assets.enums import Color, RolesIds, EmojiIds


class NaborCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False

    @commands.slash_command(name="nabor")
    async def nabor(self, interaction):
        pass

    @nabor.sub_command(name="start")
    async def nabor_start(self, interaction: disnake.ApplicationCommandInteraction, channel: disnake.TextChannel = commands.Param(description="Канал для отправки сообщения о начале набора")):
        await interaction.response.defer(ephemeral=True)
        embed = disnake.Embed(color=Color.GRAY)
        roles_values = [role.value for role in (RolesIds.SUPPORT, RolesIds.HELPER, RolesIds.MODERATOR, RolesIds.CONTROL, RolesIds.CREATIVE, RolesIds.EVENTMAKER, RolesIds.TRIBUNEMOD, RolesIds.CLOSEMAKER, RolesIds.CONTENTMAKER)]
        support, helper, moderator, control, creative, event_maker, tribunemod, closemaker, contentmaker = roles_values
        emoji = EmojiIds.emoji1.value
        embed.title = "Открыт набор на стафф сервера"
        embed.description = "Множество людей хотели бы побывать на определенной\n" \
                            "должности на нашем сервере.\n" \
                            "Поэтому мы **открываем Набор** на следующие должности:\n" \
                            f"{emoji} <@&{support}> — занимаются верификацией участников.\n" \
                            f"{emoji} <@&{helper}> — занимаются бампами сервера.\n" \
                            f"{emoji} <@&{control}> — занимаются модерацией текстовых каналов на сервере.\n"\
                            f"{emoji} <@&{moderator}> — занимаются модерацией голосовых каналов на сервере.\n" \
                            f"{emoji} <@&{creative}> — творческие личности отвечающие за мини мероприятия.\n" \
                            f"{emoji} <@&{event_maker}> — занимаются проведением мероприятий.\n" \
                            f"{emoji} <@&{closemaker}> — организуют игровые клозы.\n" \
                            f"{emoji} <@&{tribunemod}> — организуют развлекательные трибуны.\n" \
                            f"{emoji} <@&{contentmaker}> — cоздают привлекательный контент.\n" \
                            "> **Что от вас требуется?**\n" \
                            f"{emoji} Быть готовым уделять серверу 2-3 часа в день\n" \
                            f"{emoji} 16 полных лет\n" \
                            f"{emoji} Знание и понимание правил сервера и дискорда\n" \
                            f"{emoji} Иметь опыт в выбранной должности\n"
        embed.set_footer(text="При неадекватном заполнении заявки, мы будем выдавать наказания")

        embed2 = disnake.Embed(title="Наборы обьявлены!",
                               description=f"{interaction.author.mention}, вы **успешно** отправили в канал сообщение набора.", color=Color.GRAY).set_thumbnail(url=interaction.author.display_avatar)
        await channel.send(embed=embed, view=ButtonsView(self.bot))
        await interaction.followup.send(embed=embed2)

    @commands.Cog.listener()
    async def on_ready(self):
        if self.persistent_views_added:
            return

        self.bot.add_view(view=ButtonsView(self.bot))