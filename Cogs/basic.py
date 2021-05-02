import discord
from discord.ext import commands

global bot
bot = commands.Bot(command_prefix = "math ", case_insensitive = True)

class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    # Basic operations
    @commands.command(aliases = ['quick'])
    async def basic(self, ctx, *, equation):
      allOperators = ['+', '-', '*', '/', '^', '%', '=', '>=', '<=', '>', '<']
      operator = ''

      for x in allOperators:
        if x in equation:
          operator = x
      
      equation = equation.split(operator)
      num1, num2 = float(equation[0]), float(equation[1])

      result = {'+':lambda x,y:x+y,'-':lambda x,y:x-y,'*':lambda x,y:x*y,'/':lambda x,y:x/y,'^':lambda x,y:x**y,'%':lambda x,y:x%y,'=':lambda x,y:x==y,'>':lambda x,y:x>y,'<':lambda x,y:x<y,'>=':lambda x,y:x>=y,'<=':lambda x,y:x<=y}[operator](num1,num2)
      
      if result % 1 == 0:
        result = int(result)

      await ctx.send(f"{ctx.author.mention}, **Result:** ``{result}``")


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