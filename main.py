import discord
import asyncio

import os # Read token variable from environment

from configuration import * # Read configuration

import copy

client = discord.Client()

@client.event
async def on_ready():
    print('Bot ready')
    print(client.user.name)
    print(client.user.id)
    print('------')


def get_max_role(roles):
    max_role = -1
    for role in conf_call_roles:
        for r in roles:
            if(r.name==role[2]):
                max_role = conf_call_roles.index(role)
    return max_role


@client.event
async def on_message(message):
    if message.content.startswith(cc):
        call_arguments = message.content.split(cc)
        call_arguments = call_arguments[1].split(" ")
        for role in conf_call_roles:
            comm = role[0]
            arg = role[1]
            role_name = role[2]
            linearity = not(role[3])
            if (comm == call_arguments[0] and arg == call_arguments[1]):
                add_role = discord.utils.get(message.server.roles, name=role_name)
                role_list = copy.deepcopy(message.author.roles)
                user_max_role = get_max_role(role_list)
                if((not(linearity) and user_max_role != (len(conf_call_roles)-1)) or 
                    (linearity and user_max_role < conf_call_roles.index(role))):
                    
                    await client.add_roles(message.author,add_role)
                    if(logs):
                        print("Role "+add_role.name+" applied to user "+ message.author.name)
                
                    if(linearity or (final_role and role_name == conf_call_roles[-1][2])):
                        index = 0
                        while conf_call_roles[index][2] != add_role.name:
                            for r in role_list:
                                if r.name == conf_call_roles[index][2]:
                                    role_list.remove(r)
                                    break
                            index += 1
                        role_list.append(add_role)
                        await client.replace_roles(message.author,*role_list)

client.run(os.environ['TOKEN'])
