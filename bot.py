import asyncio
import os
from discord import Intents
from discord.ext.commands import Bot, ExtensionError
from dotenv import load_dotenv

load_dotenv()

COMMAND_PREFIX = "cowin "
intents = Intents.default()
intents.message_content = True

bot = Bot(command_prefix=COMMAND_PREFIX, intents=intents)


async def load_cogs():
    try:
        await bot.load_extension("cowin")
        print(f"Loaded extension 'cowin'")
    except ExtensionError as e:
        print("Failed to load extension 'cowin'\n", e)

asyncio.run(load_cogs())


@bot.event
async def on_ready():
    print("Bot:", bot.user.name)
    print("-----------------------------------------------------")


@bot.event
async def on_message(message):
    if message.author == bot.user or message.author.bot:
        return

    await bot.process_commands(message)

bot.run(os.getenv("TOKEN"))
