import disnake
from system.Buttons.moderator import ModeratorButtons
from system.Buttons.broadcaster import BroadcasterButtons
from system.Buttons.control import ControlButtons
from system.Buttons.events_mod import EventsModButtons
from system.Buttons.close_mod import CloseModButtons
from system.Buttons.creative import CreativeButtons
from system.Buttons.support import SupportButtons
from system.Buttons.content_maker import ContentMakerButtons
from system.Buttons.helper import HelperButtons


class ButtonsView(disnake.ui.View):
    def __init__(self, bot):
        self.bot = bot
        super().__init__(timeout=None)
        self.add_item(ModeratorButtons(self.bot))
        self.add_item(SupportButtons(self.bot))
        self.add_item(ControlButtons(self.bot))
        self.add_item(HelperButtons(self.bot))
        self.add_item(CreativeButtons(self.bot))
        self.add_item(EventsModButtons(self.bot))
        self.add_item(CloseModButtons(self.bot))
        self.add_item(BroadcasterButtons(self.bot))
        self.add_item(ContentMakerButtons(self.bot))