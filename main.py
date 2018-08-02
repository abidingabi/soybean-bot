import discord # This is the only external library required, pip install discord.py
import asyncio
from recipe_retrieval import get_recipe
from data_retrieval import get_recipe_from_query

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

    if message.content.lower() == "!soybean":
        msg = get_recipe()
    elif message.content.lower().startswith("!soybean"):
        try:
            query = message.content.lower().split(" ")[1]
            msg = get_recipe_from_query(query)
        except IndexError:
           msg = get_recipe() 
    else:
        return
    
    await client.send_message(message.channel, msg)

client.run(token)