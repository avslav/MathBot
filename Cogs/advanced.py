import discord
import math
from discord.ext import commands

global bot
bot = commands.Bot(command_prefix = "math ", case_insensitive = True)

class Advanced(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    
    # Powers (**, x^y)
    @bot.command(aliases=['^', '**', 'power','exponent'])
    async def powers(self, ctx, num: float, exp: int): 
        result = num ** exp
        await ctx.reply(f"Result: ``{result}``")

    
    # Factorial (!)
    @bot.command(aliases=['!'])
    async def factorial(self, ctx, num: int):
        if num > 800:
            return await ctx.reply(":x: ``Cannot factorial numbers above 800, sorry``")
       
        else:
            res = math.factorial(num)
            await ctx.send(f"Result: {res}")

def setup(bot):
    bot.add_cog(Advanced(bot))