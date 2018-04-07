import discord
import asyncio

import os #Read token variable from environment

from configuration import * #Read configuration

client = discord.Client()

@client.event
async def on_ready():
    print('Bot ready')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    if message.content.startswith(cc):
        words = message.content.split(cc)
        words = words[1].split(" ")
        for call,word,role in conf_call_roles:
            if (call == words[0] and word == words[1]):
                role = discord.utils.get(message.server.roles, name=role)
                await client.add_roles(message.author,role)
                if(logs):
                    print("Role "+role.name+" applied to user "+ message.author.name)


client.run(os.environ['TOKEN'])
