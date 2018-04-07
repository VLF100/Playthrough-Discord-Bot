import discord
import asyncio

import os # Read token variable from environment

import aux # Auxiliar functions

from configuration import * # Read configuration

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
        call_arguments = message.content.split(cc)
        call_arguments = call_arguments[1].split(" ")
        for comm,arg,role in conf_call_roles:
            if (comm == call_arguments[0] and arg == call_arguments[1]):
                role = discord.utils.get(message.server.roles, name=role)
                await client.add_roles(message.author,role)

                if(logs):
                    print("Role "+role.name+" applied to user "+ message.author.name)
                
                if(rm_prev):
                    rm_roles = []
                    index = 0
                    while conf_call_roles[index][2] != role.name:
                        rm_roles += discord.utils.get(message.server.roles, name=role)
                        index += 1
                    await client.remove_roles(message.author,rm_roles)
                    if(logs):
                        for rm_rol in rm_roles:
                            print("Role "+rm_rol+" removed from user "+ message.author.name)

                if(final_role):
                    if(role.name == conf_call_roles[-1][2]):
                        rm_roles = []
                        index = 0
                        while conf_call_roles[index][2] != role.name:
                            rm_roles += discord.utils.get(message.server.roles, name=role)
                            index += 1
                        await client.remove_roles(message.author,rm_roles)
                        if(logs):
                            print("Final Role "+role.name+" given to user "+ message.author.name)

client.run(os.environ['TOKEN'])
