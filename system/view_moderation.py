import disnake
from system.ModButtons.accept import AcceptButtons
from system.ModButtons.cancel import CancelButtons
from system.ModButtons.interview import InterviewButtons


class ButtonsView(disnake.ui.View):
    def __init__(self, bot, user, embed):
        self.bot = bot
        self.user = user
        self.embed = embed
        super().__init__(timeout=None)
        self.add_item(AcceptButtons(self.bot, self.user, self.embed))
        self.add_item(InterviewButtons(self.bot, self.user, self.embed))
        self.add_item(CancelButtons(self.bot, self.user, self.embed))