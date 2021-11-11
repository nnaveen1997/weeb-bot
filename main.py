import discord 
import os
from dotenv import find_dotenv, load_dotenv
import scraper

load_dotenv(find_dotenv())

sc = scraper

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0}'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!weeb hi'):
        await message.channel.send("Kon'nichiwa {0} san!".format(message.author.name))

    if message.content.startswith('!weeb status'):
        anime_name = message.content.split()[-1]
        msg = sc.checkNewEpisode(anime_name)
        await message.channel.send(msg)

client.run(os.getenv('TOKEN'))



