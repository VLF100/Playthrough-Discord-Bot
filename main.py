import discord
import asyncio

import os # Read token variable from environment

from configuration import * # Read configuration

import copy

from threading import Thread

client = discord.Client()

from platform   import system as system_name  # Returns the system/OS name
from subprocess import call   as system_call  # Execute a shell command

import threading

#------------------------------------------------------------MUSIC MODULE

class Music_service(object):
    voice_client = -1
    music_player = -1
    queue = []

    start_playing = -1

music_service = Music_service()

import threading
music_lock = threading.Lock()

def next_song():
    global music_service
    global music_lock
    music_lock.acquire()
    try:
        if(music_service.queue):
            player = music_service.queue.pop(0)
            music_service.music_player = player
            player.start()
        music_service.start_playing = -1
    finally:
        music_lock.release()



def has_to_play():
    global music_service
    global music_lock
    music_lock.acquire()
    try:
        if(music_service.queue):
            music_service.start_playing = 1
        else:
            music_service.start_playing = -1
    finally:
        music_lock.release()
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

    if message.content.startswith(cc):
        call_arguments = message.content.split(" ")
        if(call_arguments[0] == cc+'finished'):
            for role in conf_call_roles:
                comm = role[0]
                arg = role[1]
                role_name = role[2]
                delete_prev = role[3]
                if (cc+comm == call_arguments[0] and arg == call_arguments[1]):
                    add_role = discord.utils.get(message.server.roles, name=role_name)
                    role_list = copy.deepcopy(message.author.roles)
                    user_max_role = get_max_role(role_list)
                    if((user_max_role < conf_call_roles.index(role))):
                        
                        if(delete_prev or (final_role and role_name == conf_call_roles[-1][2])):
                            index = 0
                            while conf_call_roles[index][2] != add_role.name:
                                for r in role_list:
                                    if r.name == conf_call_roles[index][2]:
                                        role_list.remove(r)
                                        break
                                index += 1

                        role_list.append(add_role)
                        await client.replace_roles(message.author,*role_list)
                        if(logs):
                            await client.send_message(message.channel, "Role "+add_role.name+" applied to user "+ message.author.name)
                            print("Role "+add_role.name+" applied to user "+ message.author.name)

        if(call_arguments[0] == cc+'play'):
            if(music_service.voice_client == -1):
                voice_channel = discord.utils.get(message.server.channels,name='General')
                music_service.voice_client = await client.join_voice_channel(voice_channel)
            
            new_song = await music_service.voice_client.create_ytdl_player(call_arguments[1],after = has_to_play)
            music_service.queue.append(new_song)
            print("Song "+new_song.title+" added to queue by "+ message.author.name +" <"+call_arguments[1]+">")
            await client.send_message(message.channel, "Song "+new_song.title+" added to queue by "+ message.author.name +" <"+call_arguments[1]+">")

            if(not(music_service.music_player != -1 and music_service.music_player.is_playing())):
                has_to_play()

#            if(music_service.music_player!=-1 and music_service.music_player.is_playing()):
#               new_song = await music_service.voice_client.create_ytdl_player(call_arguments[1],after = has_to_play)
#                music_service.queue.append(new_song)
#                await client.send_message(message.channel, "Song "+new_song.title+" added to queue by "+ message.author.name +" <"+call_arguments[1]+">")
#            else:
#                music_service.music_player = await music_service.voice_client.create_ytdl_player(call_arguments[1],after = next_song)
#                music_service.music_player.start()
#                await client.send_message(message.channel, "Now playing "+music_service.music_player.title+" <"+call_arguments[1]+">")

            #print(dir(music_service.music_player)) #DEBUG
            
        if(call_arguments[0] == cc+'music'):  
            if(call_arguments[1]=='stop'):
                music_service.music_player.stop()
                print( "Music stopped by "+ message.author.name)
                await client.send_message(message.channel, "Music stopped by "+ message.author.name)
            if(call_arguments[1]=='pause'):
                music_service.music_player.pause()
                print( "Music paused by "+ message.author.name)
                await client.send_message(message.channel, "Music paused by "+ message.author.name)
            if(call_arguments[1]=='resume'):
                music_service.music_player.resume()
                print( "Music resumed by "+ message.author.name)
                await client.send_message(message.channel, "Music resumed by "+ message.author.name)
            if(call_arguments[1]=='skip'):
                music_service.music_player.stop()
                music_service.music_player = -1
                has_to_play()
                print( "Song skipped by "+ message.author.name)
                await client.send_message(message.channel, "Song skipped by "+ message.author.name)


def dirty_check():
    while(1):
        if(music_service.start_playing==1):
            next_song()

thread = Thread(target = dirty_check, args = ())
thread.start()

client.run(os.environ['TOKEN'])

