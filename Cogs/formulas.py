import discord
import math
import time
from discord.ext import commands

global bot
bot = commands.Bot(command_prefix = "math ", case_insensitive = True)

class Formulas(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  
    
    # Circle Circumference
    @bot.command(aliases=['cc'])
    async def circlecirc(self, ctx, radius: float):
        start = time.time()

        pi = math.pi
        res = 2 * pi
        ress = res * radius

        end = time.time()

        embed = discord.Embed(
            title = "Solved!",
            description = "Solution Steps:",
            colour = discord.Color.green()
        )

        embed.add_field(name="Formula:", value="c = 2πr")
        embed.add_field(name="Step 1:", value=f"2 * π = 6.28", inline = False)
        embed.add_field(name="Step 2:", value=f"6.28 * {radius} = {ress}", inline=False)
        embed.add_field(name="Result:", value=f"c = ``{ress}``")
  
        embed.set_author(name=ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_footer(text=f"Calculated in: {end - start} seconds")
  
        await ctx.send(embed=embed)

    # Triangle Area 
    @bot.command(aliases=['ta', 'aoft', 'triarea'])
    async def trianglearea(self, ctx, base: float, height: float):
        start = time.time()

        res = base * height
        final = res / 2

        end = time.time()

        embed = discord.Embed(
            title = "Solved!",
            description = "Solution Steps:",
            colour = discord.Color.green()
        )

        embed.add_field(name="Formula:", value="A = bh / 2")
        embed.add_field(name="Step 1:", value=f"{base} * {height} = {res}", inline = False)
        embed.add_field(name="Step 2:", value=f"{res} / 2 = {final}", inline=False)
        embed.add_field(name="Result:", value=f"A = ``{final}``")
  
        embed.set_author(name=ctx.author, icon_url = ctx.author.avatar_url)
        embed.set_footer(text=f"Calculated in: {end - start} seconds")
  
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Formulas(bot))