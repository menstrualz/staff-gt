from system.nabor import NaborCog
from system.listener import ListenerCog


cogs = (
    NaborCog,
    ListenerCog
)

def setup(bot):
    for cog in cogs:
        bot.add_cog(cog(bot)) 