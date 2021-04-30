import discord
import math
import fractions
import os
import uuid
import time
import dotenv
from discord.ext import commands
from discord.ext.commands import Bot

bot = Bot(command_prefix = "math ", case_insensitive = True)
# Conn
@bot.event
async def on_ready():
    print('Successfully connected to discord as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name='Solving your math problems!'))

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
        client.unload_extension(f'Cogs.{extension}')
        await ctx.send(f'Cog "{extension}" successfully unloaded.')
    else:
        await ctx.send("Sorry, this command is only for developers.")


# Extension Reload:
@bot.command()
async def reload(ctx, extension):
    if ctx.guild.id == 836961032961785866:
        try:
            client.unload_extension(f'Cogs.{extension}')
            client.load_extension(f'Cogs.{extension}')
            await ctx.send(f'Cog "{extension}" successfully reloaded.')
        except Exception as e:
            await ctx.send(f"Failed to reload cog. See below why. ```{e}```")
    else:
        await ctx.send("Sorry, this command is only for developers.")


# Factorial (!)
@bot.command(aliases=['!'])
async def factorial(ctx, num: int):
  if num > 800:
      return await ctx.reply(":x: ``Cannot factorial numbers above 800, sorry``")
       
  
  else:
    res = math.factorial(num)
    await ctx.send(f"Result: {res}")
   

# Decimal - Fraction (0.5 - 1/2)
@bot.command(aliases=['dtof', 'd2f'])
async def decimalToFraction(ctx, n: float):
    res = n.as_integer_ratio()
    await ctx.send(f"Result: {res}")


# Circle Circumference
@bot.command(aliases=['cc'])
async def circlecirc(ctx, radius: float):
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
async def trianglearea(ctx, base: float, height: float):
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

# Powers (**, x^y)
@bot.command(aliases=['^', '**', 'power','exponent'])
async def powers(ctx, num: float, exp: int): 
  result = num ** exp
  await ctx.reply(f"Result: ``{result}``")


# Mean Average
@bot.command()
async def average(ctx, nums: list = [2, 3, 4, 5,6]):
  res = sum(nums) / len(nums)
  await ctx.send(f"Mean Average: ``{res}``")



token = os.getenv("TOKEN")
bot.run(token) 
