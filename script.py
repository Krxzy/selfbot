from __future__ import unicode_literals
import discord
from discord.ext import commands
import aiohttp
import json
import os
import re
import traceback
import cursor
from colorama import Fore, init
import sys
import requests
import datetime
import time
import asyncio
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc
import youtube_dl
import urllib
import shutil
import dumper
from pypresence import Presence

ydl_opts = {}

init(autoreset=True)




text1 = f"""
    {Fore.RED}
            ───────────────────────────────────────────────────────────────────────────────────────────────────
            ─██████████████─██████──██████─████████████████───██████████████─████████████████───██████████████─
            ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░████████░░██───██░░██████░░██─██░░████████░░██───██░░██████░░██─
            ─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░████████░░██───██░░██──██░░██─██░░████████░░██───██░░██████░░██─
            ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░██████░░████───██░░██──██░░██─██░░██████░░████───██░░██████░░██─
            ─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─
            ─██░░██──██░░██─██░░██████░░██─██░░██──██░░██████─██░░██████░░██─██░░██──██░░██████─██░░██──██░░██─
            ─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░██──██░░██─
            ─██████──██████─██████████████─██████──██████████─██████████████─██████──██████████─██████──██████─
            ───────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
"""

text2 = f"""
    {Fore.CYAN}
            ───────────────────────────────────────────────────────────────────────────────────────────────────
            ─██████████████─██████──██████─████████████████───██████████████─████████████████───██████████████─
            ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░████████░░██───██░░██████░░██─██░░████████░░██───██░░██████░░██─
            ─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░████████░░██───██░░██──██░░██─██░░████████░░██───██░░██████░░██─
            ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░██████░░████───██░░██──██░░██─██░░██████░░████───██░░██████░░██─
            ─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─
            ─██░░██──██░░██─██░░██████░░██─██░░██──██░░██████─██░░██████░░██─██░░██──██░░██████─██░░██──██░░██─
            ─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░██──██░░██─
            ─██████──██████─██████████████─██████──██████████─██████████████─██████──██████████─██████──██████─
            ───────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
"""

text3 = f"""
    {Fore.MAGENTA}
            ───────────────────────────────────────────────────────────────────────────────────────────────────
            ─██████████████─██████──██████─████████████████───██████████████─████████████████───██████████████─
            ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░████████░░██───██░░██████░░██─██░░████████░░██───██░░██████░░██─
            ─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░████████░░██───██░░██──██░░██─██░░████████░░██───██░░██████░░██─
            ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░██████░░████───██░░██──██░░██─██░░██████░░████───██░░██████░░██─
            ─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─
            ─██░░██──██░░██─██░░██████░░██─██░░██──██░░██████─██░░██████░░██─██░░██──██░░██████─██░░██──██░░██─
            ─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░██──██░░██─
            ─██████──██████─██████████████─██████──██████████─██████████████─██████──██████████─██████──██████─
            ───────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
"""

text4 = f"""
    {Fore.GREEN}
            ───────────────────────────────────────────────────────────────────────────────────────────────────
            ─██████████████─██████──██████─████████████████───██████████████─████████████████───██████████████─
            ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░████████░░██───██░░██████░░██─██░░████████░░██───██░░██████░░██─
            ─██░░██──██░░██─██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─██░░██────██░░██───██░░██──██░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░████████░░██───██░░██──██░░██─██░░████████░░██───██░░██████░░██─
            ─██░░░░░░░░░░██─██░░██──██░░██─██░░░░░░░░░░░░██───██░░██──██░░██─██░░░░░░░░░░░░██───██░░░░░░░░░░██─
            ─██░░██████░░██─██░░██──██░░██─██░░██████░░████───██░░██──██░░██─██░░██████░░████───██░░██████░░██─
            ─██░░██──██░░██─██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─██░░██──██░░██─────██░░██──██░░██─
            ─██░░██──██░░██─██░░██████░░██─██░░██──██░░██████─██░░██████░░██─██░░██──██░░██████─██░░██──██░░██─
            ─██░░██──██░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░░░░░░░░░██─██░░██──██░░░░░░██─██░░██──██░░██─
            ─██████──██████─██████████████─██████──██████████─██████████████─██████──██████████─██████──██████─
            ───────────────────────────────────────────────────────────────────────────────────────────────────{Fore.RESET}
"""


error = f"""{Fore.RED}
                ████████████████████████████████████████████████████████████████████████████████████████
                █░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░░░███░░░░░░░░░░░░░░█░░░░░░░░░░░░░░░░███
                █░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███
                █░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███
                █░░▄▀░░█████████░░▄▀░░████░░▄▀░░███░░▄▀░░████░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░████░░▄▀░░███
                █░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░▄▀░░███░░▄▀░░░░░░░░▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░▄▀░░███
                █░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀▄▀▄▀▄▀▄▀▄▀░░███░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀▄▀░░███
                █░░▄▀░░░░░░░░░░█░░▄▀░░░░░░▄▀░░░░███░░▄▀░░░░░░▄▀░░░░███░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░▄▀░░░░███
                █░░▄▀░░█████████░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█████░░▄▀░░██░░▄▀░░█░░▄▀░░██░░▄▀░░█████
                █░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░██░░▄▀░░░░░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░░░░░█
                █░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀▄▀▄▀░░█
                █░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░██░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░██░░░░░░░░░░█
                ████████████████████████████████████████████████████████████████████████████████████████
{Fore.RESET}

"""

success = f"""{Fore.GREEN}

        ██████████████████████████████████████████████████████████████████████████████████████████████████████████
        █░░░░░░░░░░░░░░█░░░░░░██░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
        █░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
        █░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
        █░░▄▀░░█████████░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████
        █░░▄▀░░░░░░░░░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█
        █░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
        █░░░░░░░░░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
        █████████░░▄▀░░█░░▄▀░░██░░▄▀░░█░░▄▀░░█████████░░▄▀░░█████████░░▄▀░░█████████████████░░▄▀░░█████████░░▄▀░░█
        █░░░░░░░░░░▄▀░░█░░▄▀░░░░░░▄▀░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░▄▀░░░░░░░░░░█░░░░░░░░░░▄▀░░█░░░░░░░░░░▄▀░░█
        █░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█░░▄▀▄▀▄▀▄▀▄▀░░█
        █░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█░░░░░░░░░░░░░░█
        ██████████████████████████████████████████████████████████████████████████████████████████████████████████
{Fore.RESET}

"""




def initial_setup():
    with open('./config.json', 'w') as preconfig:
        print(text2)
        print()
        print()
        print(f"{Fore.CYAN}  [Aurora Setup]{Fore.RESET} Enter your Discord token: ", end='')
        pre_token = input()
        print()
        print(f"{Fore.CYAN}  [Aurora Setup]{Fore.RESET} Enter your Discord password: ", end='')
        pre_password = input()
        print()
        print(f"{Fore.CYAN}  [Aurora Setup]{Fore.RESET} Enter desired prefix: ", end='')
        pre_prf = input()
        print()
        print(f"{Fore.CYAN}  [Aurora Setup]{Fore.RESET} Enter the amount of time before your message embed deletes (Amount is in seconds by default) ", end='')
        pre_delaft= input()
        print()
        data = {
            "token": pre_token,
            "password": pre_password,
            "richpresence": bool(True),
            "mentionlogger": bool(True),
            "slotbotsnipe": bool(True),
            "prefix": pre_prf,
            "deleteafter": pre_delaft
        }
        json.dump(data, preconfig, indent=4)


if not os.path.exists('./config.json'):
    initial_setup()
else:
    if os.stat("./config.json").st_size == 0:
        initial_setup()

# config file
with open("config.json") as ff:
    config = json.load(ff)

token = config.get("token")
prefix = config.get("prefix")
val = config.get("deleteafter")
slotbot_sniper = config.get("slotbotsnipe")
mention_logger = config.get("mentionlogger")
password = config.get("password")
rpc = config.get("richpresence")
dv = int(val)

Aurora = commands.Bot(
    description='Aurora',
    command_prefix=prefix,
    self_bot=True,
    help_command=None)




# bot classes | functions
def clear():
  if os.name != 'nt':
    os.system('clear')
  else:
    os.system('cls')



def Init():
    try:
        print(text2)
        Aurora.run(token, bot=False, reconnect=True)
    except Exception as e:
        clear()
        print(error)
        print(Fore.RED + "  [Aurora Login Failure] " + Fore.RESET + str(e))
        time.sleep(20)


class AuroraSelfbot:
    def start():
        for i in range(3):
            print(text1)
            time.sleep(.4)
            clear()
            print(text2)
            time.sleep(.4)
            clear()
            print(text3)
            time.sleep(.4)
            clear()
            print(text4)
            time.sleep(.4)
            clear()
        Init()
        


@Aurora.event
async def on_connect():
    clear()
    print(success)
    time.sleep(1.5)
    clear()
    print(text2)
    print("Connected")



# Other Things
Aurora.msgsniper = True
Aurora.snipe_history_dict = {}
Aurora.sniped_message_dict = {}
Aurora.sniped_edited_message_dict = {}


#events



@Aurora.event
async def on_message_delete(message):
    if message.author.id == Aurora.user.id:
        return
    if Aurora.msgsniper:
        # if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.GroupChannel): \\ removed so people cant get you disabled
        if isinstance(message.channel, discord.DMChannel):
            attachments = message.attachments
            if len(attachments) == 0:
                message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(
                    message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
                await message.channel.send(message_content)
            else:
                links = ""
                for attachment in attachments:
                    links += attachment.proxy_url + "\n"
                message_content = "`" + str(
                    discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(
                    message.content) + "\n\n**Attachments:**\n" + links
                await message.channel.send(message_content)
    if len(Aurora.sniped_message_dict) > 1000:
        Aurora.sniped_message_dict.clear()
    if len(Aurora.snipe_history_dict) > 1000:
        Aurora.snipe_history_dict.clear()
    attachments = message.attachments
    if len(attachments) == 0:
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
        Aurora.sniped_message_dict.update({channel_id: message_content})
        if channel_id in Aurora.snipe_history_dict:
            pre = Aurora.snipe_history_dict[channel_id]
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            Aurora.snipe_history_dict.update({channel_id: pre[:-3] + post + "\n```"})
        else:
            post = str(message.author) + ": " + str(message.content).replace("@everyone", "@\u200beveryone").replace("@here", "@\u200bhere")
            Aurora.snipe_history_dict.update({channel_id: "```\n" + post + "\n```"})
    else:
        links = ""
        for attachment in attachments:
            links += attachment.proxy_url + "\n"
        channel_id = message.channel.id
        message_content = "`" + str(discord.utils.escape_markdown(str(message.author))) + "`: " + discord.utils.escape_mentions(message.content) + "\n\n**Attachments:**\n" + links
        Aurora.sniped_message_dict.update({channel_id: message_content})





@Aurora.event
async def on_message_edit(before, after):
    await Aurora.process_commands(after)

# Commands


@Aurora.command()
async def snipe(ctx):
    await ctx.message.delete()
    currentChannel = ctx.channel.id
    if currentChannel in Aurora.sniped_message_dict:
        await ctx.send(Aurora.sniped_message_dict[currentChannel])
    else:
        await ctx.send("There is nothing to snipe!", delete_after=3)

@Aurora.command()
async def help(ctx, cate=None):
    if cate is None:
        await ctx.message.delete()
        embed=discord.Embed(title="ðﾝﾓﾐðﾝﾓﾾðﾝﾓﾻðﾝﾓﾸðﾝﾓﾻðﾝﾓﾪ ðﾝﾓﾢðﾝﾓﾮðﾝﾓﾵðﾝﾓﾯ ðﾝﾓﾑðﾝﾓﾸðﾝﾓﾽ", description=f"**Hello {Aurora.user.name}#{Aurora.user.discriminator}, All command categories are showed below, type {Aurora.command_prefix}help category_name to show the categorized commands!**", color=0xfc03f0)
        embed.set_thumbnail(url=Aurora.user.avatar_url)
        embed.set_image(url="https://media.discordapp.net/attachments/771190694978125834/788827657231400970/image_2.png")
        embed.add_field(name=f"{Aurora.command_prefix}help general", value="Lists all the general commands", inline=True)
        embed.add_field(name=f"{Aurora.command_prefix}help fun", value="Lists all the fun commands", inline=False)
        embed.add_field(name=f"{Aurora.command_prefix}help nsfw", value="Lists all the nsfw commands", inline=False)
        embed.add_field(name=f"{Aurora.command_prefix}help nuke", value="Lists all the nuke commands", inline=False)
        embed.add_field(name=f"{Aurora.command_prefix}help image", value="Lists all the image commands", inline=False)
        embed.set_footer(text="Created by gay boy jonah")
        await ctx.send(embed=embed, delete_after=dv) 


@Aurora.command()
async def purge(ctx, amount: int):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == Aurora.user).map(
            lambda m: m):
        try:
            await message.delete()
        except:
            pass

@Aurora.command()
async def copy(ctx): 
    await ctx.message.delete()
    await Aurora.create_guild(f'backup-{ctx.guild.name}')
    await asyncio.sleep(4)
    for g in Aurora.guilds:
        if f'backup-{ctx.guild.name}' in g.name:
            for c in g.channels:
                await c.delete()
            for cate in ctx.guild.categories:
                x = await g.create_category(f"{cate.name}")
                for chann in cate.channels:
                    if isinstance(chann, discord.VoiceChannel):
                        await x.create_voice_channel(f"{chann}")
                    if isinstance(chann, discord.TextChannel):
                        await x.create_text_channel(f"{chann}")
            for role in ctx.guild.roles:
                name = role.name
                color = role.colour
                p = role.permissions
                await g.create_role(name=name, permissions=p, colour=color)


@Aurora.command()
async def dmall(ctx, *, c: str):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in guild.members:
        try:
            await member.create_dm()
            await member.send(c)
            print(
                f"{Fore.GREEN}[DM All]{Fore.RESET} Sent a dm to {member.name}")
        except:
            pass


@Aurora.command()
async def youtubetomp4(ctx, url):
    await ctx.message.delete()
    embed=discord.Embed(title="Youtube To Mp4 Command", description=f"Video Downloading: [Link]({url})", color=0xff0000,timestamp=ctx.message.created_at)
    embed.set_footer(text="Aurora Selfbot")
    await ctx.send(embed=embed, delete_after=30)
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    await ctx.send(f"```Youtube Video Downloaded... ({url})```")

@Aurora.command()
async def nick(ctx, *, name):
    await ctx.message.delete()
    await ctx.author.edit(nick=name)


@Aurora.command(aliases=['guildpfp', 'serverpfp', 'servericon'])
async def guildicon(ctx):
    await ctx.message.delete()
    em = discord.Embed(title=ctx.guild.name)
    em.set_image(url=ctx.guild.icon_url)
    await ctx.send(embed=em, delete_after=dv)


@Aurora.command()
async def spam(ctx, amount: int, *, m):
    await ctx.message.delete()
    for _i in range(amount):
        await ctx.send(f'{m}')
    
@Aurora.command(aliases=['rep'])
async def spamreport(ctx, member: discord.Member = None):
    await ctx.message.delete()
    for i in range(15):
        await ctx.send(f"Report sent to Discord for <@{member.id}>", delete_after=1)
    
@Aurora.command()
async def reverse(ctx, *, message):
    await ctx.message.delete()
    message = message[::-1]
    await ctx.send(message)

@Aurora.command()
async def hastebin(ctx, *, message):
    await ctx.message.delete()
    r = requests.post("https://hastebin.com/documents", data=message).json()
    await ctx.send(f"<https://hastebin.com/{r['key']}>")

@Aurora.command()
async def count(ctx, number: int):
    await ctx.message.delete()
    for i in range(number):
        await ctx.send(i)


@Aurora.command()
async def poll(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(title="**Poll**", color=0xfc03f0, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.add_field(name=f"{message}", value="✅ ❌", inline=False)
    message = await ctx.send(embed=embed, delete_after=dv)
    await message.add_reaction("✅")
    await message.add_reaction("❌")

@Aurora.command()
async def rembed(ctx, *, message):
    await ctx.message.delete()
    embed1 = discord.Embed(description=message, color=0x9400D3, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed2 = discord.Embed(description=message, color=0x4B0082, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed3 = discord.Embed(description=message, color=0x0000FF, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed4 = discord.Embed(description=message, color=0x00FF00, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed5 = discord.Embed(description=message, color=0xFFFF00, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed6 = discord.Embed(description=message, color=0xFF7F00, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed7 = discord.Embed(description=message, color=0xFF0000, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    msg = await ctx.send(embed=embed1)
    for i in range(2):
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed2)
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed3)
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed4)
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed5)
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed6)
        await asyncio.sleep(0.2)
        await msg.edit(embed=embed7)
        await asyncio.sleep(0.2)
    await msg.delete()

@Aurora.command()
async def playing(ctx, *, message):
    await ctx.message.delete()
    game = discord.Game(
        name=message
    )
    await Aurora.change_presence(activity=game)
    await ctx.send("Playing Presence Set! ✔️")

@Aurora.command(aliases=['geoip', 'iplookup'])
async def geo(ctx, arg):
    await ctx.message.delete()
    try:
        r = requests.get(f'http://ip-api.com/json/{arg}')
        embed = discord.Embed(title='**IP Lookup**', color=0xfc03f0, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
        embed.add_field(name="**ISP**", value=r.json()['isp'], inline=False)
        embed.add_field(name="**ASN**", value=r.json()['as'], inline=False)
        embed.add_field(name="**City**", value=r.json()['city'], inline=False)
        embed.add_field(name="**Country**", value=r.json()['country'], inline=False)
        embed.add_field(name="**Region**", value=r.json()['regionName'], inline=False)
        embed.add_field(name="**Longitude**", value=r.json()['lon'], inline=False)
        embed.add_field(name="**Latitude**", value=r.json()['lat'], inline=False)
        embed.add_field(name="**Status**", value=r.json()['status'], inline=False)

        await ctx.send(embed=embed, delete_after=val)
    except Exception as e:
        print(Fore.RED + "[ERROR] " + Fore.RESET + Fore.YELLOW + str(e))

@Aurora.command()
async def phcomment(ctx, user, *, message):
    await ctx.message.delete()
    r = requests.get(f'https://nekobot.xyz/api/imagegen?type=phcomment&text={message}&username={user}&image=https://i.imgur.com/raRKTgZ.jpg').json()
    embed = discord.Embed(color=0xFFFAFA, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_image(url=r["message"])
    await ctx.send(embed=embed, delete_after=dv)


@Aurora.command()
async def hoesmad(ctx):
    await ctx.message.delete()
    await ctx.send("https://cdn.discordapp.com/attachments/785257080436949052/789664942289846292/hoes_mad.mp4")

@Aurora.command()
async def massunban(ctx):
    await ctx.message.delete()
    banlist = await ctx.guild.bans()
    for users in banlist:
        try:
            await asyncio.sleep(2)
            await ctx.guild.unban(user=users.user)
        except:
            pass

@Aurora.command()
async def deleteroles(ctx):
    await ctx.message.delete()
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
        except:
            pass


@Aurora.command(aliases=['whois'])
async def userinfo(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if not member:
        member = ctx.message.author
    roles = [role for role in member.roles]
    embed = discord.Embed(color=0xfc03f0, timestamp=ctx.message.created_at,
                          title=f"User Info - {member}")
    embed.set_thumbnail(url=member.avatar_url)

    embed.add_field(name="ID", value=member.id)
    embed.add_field(name="Display Name", value=member.display_name)
    embed.add_field(name="Animated Avatar? ", value=member.is_avatar_animated())
    try:
        embed.add_field(name="Mutual Friends", value=len(await member.mutual_friends()))
    except:
        pass

    embed.add_field(name="Created Account On", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
    embed.add_field(name="Joined Server On", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

    embed.add_field(name="Roles", value="".join([role.mention for role in roles]))
    embed.add_field(name="Highest Role", value=member.top_role.mention)
    await ctx.send(embed=embed, delete_after=20)


@Aurora.command()
async def tweet(ctx, username: str, *, message: str): # b'\xfc'
    await ctx.message.delete()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)

@Aurora.command()
async def ascii(ctx, *, text): # b'\xfc'
    await ctx.message.delete()
    r = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(text)}').text
    if len('```'+r+'```') > 2000:
        return
    await ctx.send(f"```{r}```")


@Aurora.command()
async def createchannels(ctx, *, name):
    await ctx.message.delete()
    guild = ctx.message.guild
    for i in range(250):
        try:
            await guild.create_text_channel(name)
        except:
            pass

@Aurora.command()
async def ht(ctx):
    await ctx.message.delete()
    await ctx.send("https://media.discordapp.net/attachments/796699028011614218/797503952216129556/image0-29.jpg")


@Aurora.command()
async def embed(ctx, *, message):
    await ctx.message.delete()
    embed = discord.Embed(color=0xfc03f0, description=message, timestamp=datetime.datetime.utcfromtimestamp(time.time()))
    embed.set_author(name=str(Aurora.user.display_name + "#" + Aurora.user.discriminator), icon_url=Aurora.user.avatar_url)
    await ctx.send(embed=embed, delete_after=val)

@Aurora.command()
async def deletechannels(ctx):
    await ctx.message.delete()
    for channel in ctx.message.guild.channels:
        try:
            await channel.delete()
            print(
                f"{Fore.GREEN}[Delete Channels]{Fore.RESET} {channel.name} has been deleted!"
            )
        except:
            pass


@Aurora.command()
async def getallpfp(ctx, member: discord.Member=None):
    await ctx.message.delete()
    txtfile = open(f'pfps.txt', 'w+')
    try:
        for member in ctx.message.guild.members:
            txtfile.write(f'{member.display_name}#{member.discriminator}\'s profile picture link: {member.avatar_url}\n')
    except:
        pass


@Aurora.command()
async def banall(ctx):
    await ctx.message.delete()
    guild = ctx.message.guild
    for member in ctx.message.guild.members:
        try:
            await guild.ban(member)
            print(
                f"{Fore.GREEN}[Ban Command]{Fore.RESET} {member.name} was banned from {guild}"
            )

        except:
            pass
    print(f"{Fore.GREEN}[Ban Command]{Fore.RESET} Complete!")

@Aurora.command()
async def friend(ctx, member: discord.Member=None):
    await ctx.message.delete()
    if not member:
        pass
    else:
        await member.send_friend_request()

@Aurora.command(aliases=["9/11", "911", "terrorist"])
async def nine_eleven(ctx):
    await ctx.message.delete()
    invis = ""  # char(173)
    message = await ctx.send(f'''
{invis}:man_wearing_turban::airplane:    :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis} :man_wearing_turban::airplane:   :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}  :man_wearing_turban::airplane:  :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}   :man_wearing_turban::airplane: :office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content=f'''
{invis}    :man_wearing_turban::airplane::office:           
''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
        :boom::boom::boom:    
        ''')


@Aurora.command(aliases=["jerkoff", "ejaculate", "orgasm"])
async def cum(ctx):
    await ctx.message.delete()
    message = await ctx.send('''
            :ok_hand:            :smile:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :smiley:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :grimacing:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant:  
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :persevere:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:   
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                      :ok_hand:            :confounded:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:=D 
             :trumpet:      :eggplant: 
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :tired_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D 
             :trumpet:      :eggplant:    
             ''')
    await asyncio.sleep(0.5)
    await message.edit(contnet='''
                       :ok_hand:            :weary:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8=:punch:= D:sweat_drops:
             :trumpet:      :eggplant:        
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :dizzy_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')
    await asyncio.sleep(0.5)
    await message.edit(content='''
                       :ok_hand:            :drooling_face:
   :eggplant: :zzz: :necktie: :eggplant: 
                   :oil:     :nose:
                 :zap: 8==:punch:D :sweat_drops:
             :trumpet:      :eggplant:                 :sweat_drops:
     ''')











# At the end of the file
if __name__ == "__main__":
    try:
        cursor.hide()
    except:
        pass
    AuroraSelfbot.start()
else:
    exit(-1)


