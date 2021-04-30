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

    print("\nBot is ready")
    print("--------------------------------")
    print("Powered by: avslav & Vergo")

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

# Addition (+)
@bot.command()
async def add(ctx, num1: int, num2: int):
    result = num1 + num2
    await ctx.send(f"Result: {result}")

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

# Subtraction (-)
@bot.command(aliases=['sub', 'minus', 'ss'])
async def subtract(ctx, num1: int, num2: int):
  the_result = num1 - num2
  await ctx.send(f"Result: {the_result}")

# Multiplication (x)  
@bot.command(aliases=['times', 'x'])
async def multiply(ctx, num1: int, num2: int):
  res = num1 * num2
  await ctx.send(f"Result: {res}")

# Division (/,÷)  
@bot.command(aliases=['div', '/'])
async def divide(ctx, num1: int, num2: int, *, rounded = False):
  
  if rounded == False:
    res = num1 / num2
    await ctx.send(f"Result: {res}")
  
  else:
    res = num1 // num2
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



bot.run(os.getenv("TOKEN")) 
