import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    activity = discord.Activity(type=discord.ActivityType.listening, name="Bacon Cooking!")
    await bot.change_presence(status=discord.Status.online, activity=activity)
    print(f"Bot is online as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.send("Hi there! 👋")

bot.run(TOKEN)
