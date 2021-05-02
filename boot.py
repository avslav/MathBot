import discord
import math
import fractions
import os
import uuid
import time
import dotenv
from discord.ext import commands
from discord.ext.commands import Bot

global bot
bot = Bot(command_prefix = "math ", case_insensitive = True)
# Conn
@bot.event
async def on_ready():
    print('Successfully connected to discord as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='Solving your math problems!'))


# Auto Extension Load
for filename in os.listdir('./Cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'Cogs.{filename[:-3]}')
 
# Error Embed - Handlers
@bot.event
async def on_command_error(ctx, error):
  embed = discord.Embed(
    title = "Oh no! An Error Occured!",
    colour = discord.Color.red()
  )

  errid = uuid.uuid4()
  embed.add_field(name="Error Details:", value=error)
  embed.add_field(name="Error ID:", value=errid, inline=False)
  embed.set_footer(text=f"Error Logged at: {ctx.message.created_at}")
  
  print(f"Error in {ctx.guild.name}: {error}. Error Reference ID: {errid}")
  await ctx.reply(embed=embed)

# Extension Load:
@bot.command()
async def load(ctx, extension):
    if ctx.guild.id == 836961032961785866:
        bot.load_extension(f'Cogs.{extension}')
        await ctx.send(f'Cog "{extension}" successfully loaded.')
    else:
        await ctx.send("Sorry, this command is only for developers.")

# Extension Unload:
@bot.command()
async def unload(ctx, extension):
    if ctx.guild.id == 836961032961785866:
        bot.unload_extension(f'Cogs.{extension}')
        await ctx.send(f'Cog "{extension}" successfully unloaded.')
    else:
        await ctx.send("Sorry, this command is only for developers.")


# Extension Reload:
@bot.command()
async def reload(ctx, extension):
    if ctx.guild.id == 836961032961785866:
        try:
            bot.unload_extension(f'Cogs.{extension}')
            bot.load_extension(f'Cogs.{extension}')
            await ctx.send(f'Cog "{extension}" successfully reloaded.')
        except Exception as e:
            await ctx.send(f"Failed to reload cog. See below why. ```{e}```")
    else:
        await ctx.send("Sorry, this command is only for developers.")
   




# Mean Average
@bot.command()
async def average(ctx, nums: list = [2, 3, 4, 5,6]):
  res = sum(nums) / len(nums)
  await ctx.send(f"Mean Average: ``{res}``")



token = "Sorry, no token here"
bot.run(token) 