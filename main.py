import keep_alive
import discord
import os
import time
import discord.ext
from discord.utils import get
from discord.ext import commands, tasks
from discord.ext.commands import has_permissions,  CheckFailure, check
import random
#^ basic imports for other features of discord.py and python ^

client = discord.Client()

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("bot online")
    
    
@client.command()
async def carti(ctx, the_input: str):
  def getCartiChar(lex, ch) -> str:
      """This function will select a random choice from the key tuple."""
      return random.choice(lex[ch])

  lex = {
    'a': ('a', 'A'),
    'b': ('b', 'B', '8'),
    'c': ('c', 'C'),
    'd': ('d', 'D'),
    'e': ('e', 'E', '3'),
    'f': ('f', 'F'),
    'g': ('g', 'G'),
    'h': ('h', 'H'),
    'i': ('i', 'I', '1'),
    'j': ('j', 'J'),
    'k': ('k', 'K'),
    'l': ('l', 'L'),
    'm': ('m', 'M'),
    'n': ('n', 'N'),
    'o': ('o', 'O', '0'),
    'p': ('p', 'P'),
    'q': ('q', 'Q'),
    'r': ('r', 'R'),
    's': ('s', 'S', '5'),
    't': ('t', 'T'),
    'u': ('u', 'U'),
    'v': ('v', 'V'),
    'w': ('w', 'W'),
    'x': ('x', 'X'),
    'y': ('y', 'Y'),
    'z': ('z', 'Z'),
    ' ': (' ', ' < ', ' > ', ' * ')
  }
  inp = the_input.lower()
  fin = ''
  for x in inp:
    if x not in lex:
      fin += x
    else:
      fin += getCartiChar(lex, x)
  await ctx.send(fin)


async def kick(ctx, member : discord.Member):
    try:
        await member.kick(reason=None)
        await ctx.send("kicked "+member.mention) #simple kick command to demonstrate how to get and use member mentions
    except:
        await ctx.send("bot does not have the kick members permission!")



keep_alive.keep_alive()
client.run(os.getenv("TOKEN"))