import time
import discord
from discord.ext import commands
import asyncio
import random

bot = commands.Bot(command_prefix="do ", self_bot=True)

@bot.event
async def on_ready():
    print("Online")


@bot.command()
async def magic(ctx, *, args):
    await ctx.message.delete()
    try:
        name = args
        while True:
            async with ctx.typing():
                loop = ""
                for n in name:
                    loop = loop + n
                    await ctx.message.author.edit(nick=loop)
                    asyncio.sleep(2)
                    time.sleep(1)
    except Exception as e:
        print(e)    
    
    except:
        await ctx.send("lol")


bot.run("NTU3Mzk3NTg3Njk5Njk1NjE2.D33tkg.lYj8GTCIUClY0MwvImGnw0Ltkx8", bot=False)