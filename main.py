import discord
import asyncio

import os # Read token variable from environment

from configuration import * # Read configuration

import copy
from random import randint

client = discord.Client()

#import threading

#------------------------------------------------------------MUSIC MODULE

#class Music_service(object):
#    voice_client = -1
#    music_player = -1
#    queue = []
#
#    start_playing = -1
#
#music_service = Music_service()
#
#import threading
#music_lock = threading.Lock()
#
#def next_song():
#    global music_service
#    global music_lock
#    music_lock.acquire()
#    try:
#        if(music_service.queue):
#            player = music_service.queue.pop(0)
#            music_service.music_player = player
#            player.start()
#        music_service.start_playing = -1
#    finally:
#        music_lock.release()



#def has_to_play():
#    global music_service
#    global music_lock
#    music_lock.acquire()
#    try:
#        if(music_service.queue):
#            music_service.start_playing = 1
#        else:
#            music_service.start_playing = -1
#    finally:
#        music_lock.release()
#------------------------------------------------------------

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
    global music_service
    global music_lock

    if message.content.startswith("-random"):
    	split_random = message.content.split(" ")
    	try:
    		maxnumber_random = int(split_random[1])
    		result_random = randint(1,maxnumber_random)
    		await message.channel.send("Number is: "+str(result_random))
    	except Exception as e:
    		print("Number not valid: "+split_random[1])

    if message.content.startswith(cc):
        call_arguments = message.content.split(" ")
        for role in conf_call_roles:
            comm = role[0]
            arg = role[1]
            role_name = role[2]
            if (cc+comm == call_arguments[0] and arg == call_arguments[1]):
                add_role = discord.utils.get(message.guild.roles, name=role_name)
                role_list = copy.copy(message.author.roles)
                if role_name == "Fata Morgana":
                	door_roles = []
                	door_roles.append(discord.utils.get(message.guild.roles, name="Rose Manor"))
                	door_roles.append(discord.utils.get(message.guild.roles, name="Weeping Manor"))
                	door_roles.append(discord.utils.get(message.guild.roles, name="Pig Iron Manor"))
                	door_roles.append(discord.utils.get(message.guild.roles, name="Misty Manor"))
                	door_roles.append(discord.utils.get(message.guild.roles, name="Fifth Door"))
                	door_roles.append(discord.utils.get(message.guild.roles, name="Sixth Door"))
                	door_roles.append(discord.utils.get(message.guild.roles, name="Seventh Door"))
                	door_roles.append(discord.utils.get(message.guild.roles, name="Final Door"))
                	await message.author.remove_roles(*door_roles)
                await message.author.add_roles(add_role)
                if(logs):
                    await message.channel.send("Role "+add_role.name+" applied to user "+ message.author.name)
                    print("Role "+add_role.name+" applied to user "+ message.author.name)

#        if(call_arguments[0] == cc+'play'):
#            if(music_service.voice_client == -1):
#                voice_channel = discord.utils.get(message.server.channels,name='General')
#                music_service.voice_client = await client.join_voice_channel(voice_channel)
#            
#            new_song = await music_service.voice_client.create_ytdl_player(call_arguments[1],after = has_to_play)
#            music_service.queue.append(new_song)
#            print("Song "+new_song.title+" added to queue by "+ message.author.name +" <"+call_arguments[1]+">")
#            await client.send_message(message.channel, "Song "+new_song.title+" added to queue by "+ message.author.name +" <"+call_arguments[1]+">")
#
#            if(not(music_service.music_player != -1 and music_service.music_player.is_playing())):
#                has_to_play()

#            if(music_service.music_player!=-1 and music_service.music_player.is_playing()):
#               new_song = await music_service.voice_client.create_ytdl_player(call_arguments[1],after = has_to_play)
#                music_service.queue.append(new_song)
#                await client.send_message(message.channel, "Song "+new_song.title+" added to queue by "+ message.author.name +" <"+call_arguments[1]+">")
#            else:
#                music_service.music_player = await music_service.voice_client.create_ytdl_player(call_arguments[1],after = next_song)
#                music_service.music_player.start()
#                await client.send_message(message.channel, "Now playing "+music_service.music_player.title+" <"+call_arguments[1]+">")

            #print(dir(music_service.music_player)) #DEBUG
            
#        if(call_arguments[0] == cc+'music'):  
#            if(call_arguments[1]=='stop'):
#                music_service.music_player.stop()
#                print( "Music stopped by "+ message.author.name)
#                await client.send_message(message.channel, "Music stopped by "+ message.author.name)
#            if(call_arguments[1]=='pause'):
#                music_service.music_player.pause()
#                print( "Music paused by "+ message.author.name)
#                await client.send_message(message.channel, "Music paused by "+ message.author.name)
#            if(call_arguments[1]=='resume'):
#                music_service.music_player.resume()
#                print( "Music resumed by "+ message.author.name)
#                await client.send_message(message.channel, "Music resumed by "+ message.author.name)
#            if(call_arguments[1]=='skip'):
#                music_service.music_player.stop()
#                music_service.music_player = -1
#                has_to_play()
#                print( "Song skipped by "+ message.author.name)
#                await client.send_message(message.channel, "Song skipped by "+ message.author.name)


#def dirty_check():
#    while(1):
#        if(music_service.start_playing==1):
#            next_song()

#thread = Thread(target = dirty_check, args = ())
#thread.start()

client.run(os.environ['TOKEN'])

