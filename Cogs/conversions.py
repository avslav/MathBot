import discord
import fractions
from fractions import Fraction
from discord.ext import commands

global bot
bot = commands.Bot(command_prefix = "math ", case_insensitive = True)

class Conversions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    # Decimal - Fraction (0.5 - 1/2)
    @bot.command(aliases=['dtof', 'd2f'])
    async def decimalToFraction(self, ctx, n: float):
        res = Fraction(n)
        await ctx.send(f"Result: ``{res}``")


def setup(bot):
    bot.add_cog(Conversions(bot))
