import discord
from discord.ext import commands

global bot
bot = commands.Bot(command_prefix = "math ", case_insensitive = True)

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Addition (+)
    @bot.command()
    async def add(self, ctx, num1: int, num2: int):
        result = num1 + num2
        await ctx.send(f"Result: {result}")

    # Subtraction (-)
    @bot.command(aliases=['sub', 'minus', 'ss'])
    async def subtract(self, ctx, num1: int, num2: int):
        the_result = num1 - num2
        await ctx.send(f"Result: {the_result}")

    # Division (/,÷)  
    @bot.command(aliases=['div', '/'])
    async def divide(self, ctx, num1: int, num2: int, *, rounded = False):
  
        if rounded == False:
            res = num1 / num2
            await ctx.send(f"Result: {res}")
  
        else:
            res = num1 // num2
            await ctx.send(f"Result: {res}")

    
    # Multiplication (x)  
    @bot.command(aliases=['times', 'x'])
    async def multiply(self, ctx, num1: int, num2: int):
        res = num1 * num2
        await ctx.send(f"Result: {res}")

    # Round  
    @bot.command(aliases=['rnd'])
    async def round(self, ctx, n: float, *, roundTo: int):
        res = round(n, roundTo)
        await ctx.send(f"Result: ``{res}``")
    

def setup(bot):
    bot.add_cog(Basic(bot))
