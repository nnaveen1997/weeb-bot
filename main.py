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

    if message.content.startswith('!hi'):
        await message.channel.send("Kon'nichiwa {0} san!".format(message.author.name))

    if message.content.startswith('!demonslayer'):
        msg = sc.checkNewEpisode()
        await message.channel.send(msg)

client.run(os.getenv('TOKEN'))



