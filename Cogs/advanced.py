import discord
import math
import numpy as np
from discord.ext import commands

global bot
bot = commands.Bot(command_prefix = "math ", case_insensitive = True)

class Advanced(commands.Cog):
    def __init__(self, bot, sin):
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

    @bot.command()
    async def sin(self, ctx, num: int):
        await ctx.send(np.sin(num))

    @bot.command()
    async def cos(self, ctx, num: int):
        await ctx.send(np.cos(num))

    @bot.command()
    async def tan(self, ctx, num: int):
        await ctx.send(np.tan(num))

    @bot.command()
    async def hypot(self, ctx, num1: int, num2: int):
        await ctx.send(np.hypot(num1, num2))

    @bot.command()
    async def lcm(self, ctx, num1: int, num2: int):
        await ctx.send(np.lcm(num1, num2))

    @bot.command()
    async def gcd(self, ctx, num1: int, num2: int):
        await ctx.send(np.gcd(num1, num2))

    @bot.command()
    async def sqrt(self, ctx, num: int):
        await ctx.send(np.sqrt(num))

def setup(bot):
    bot.add_cog(Advanced(bot))
