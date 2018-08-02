import discord # This is the only external library required, pip install discord.py
import asyncio
from recipe_retrieval import get_recipe


token_file = open("discord_token.key", "r")

token = token_file.read()

token_file.close()

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.lower().startswith('!soybean'):
        msg = get_recipe()
        await client.send_message(message.channel, msg)

client.run(token)