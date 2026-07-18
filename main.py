import discord
from discord.ext import commands
import config, database

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix=config.PREFIX, intents=intents)

@bot.event
async def on_ready():
    database.init_db()
    print(f'Thầy Pháp đã sẵn sàng!')

@bot.command()
async def chao(ctx):
    await ctx.send("Bần đạo đã đến!")

@bot.command()
async def batma(ctx):
    await ctx.send("Bát ma đến đây!")

bot.run(config.TOKEN)
