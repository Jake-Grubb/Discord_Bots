import discord
import time
import logging
from sys import argv
from logging.handlers import RotatingFileHandler

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    logger.info("[" + str(time.ctime(time.time())) + "] [" + str(message.guild) + "] [" + str(message.channel) + "] [" + str(message.author) + "] \"" + str(message.content) + "\"")


@client.event
async def on_ready():
    logger.debug("[" + str(time.ctime(time.time())) + "] Logger is now online")
    pass


logger = logging.getLogger("loggerbot.log")
logger.setLevel(logging.INFO)
handler = RotatingFileHandler("./loggerbot.log", maxBytes=5000000)
logger.addHandler(handler)

client.run(argv[1])
