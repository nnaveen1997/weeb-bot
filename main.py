import discord 
import os
from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0}'.format(client.user))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$weeb'):
        await message.channel.send('Ohayo Gozaimasu {0} san!'.format(message.author.name))


client.run(os.getenv('TOKEN'))



