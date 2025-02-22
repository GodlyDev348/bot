import discord
import os
from discord.ext import commands
import asyncio
import time
from datetime import datetime, timedelta
import requests
import socket
import base64
import hashlib
import pytz
import random
import aiohttp
import re
from win10toast import ToastNotifier
import logging
from colorama import init, Fore, Back, Style
import fade

logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger('discord')

logging.getLogger('discord').setLevel(logging.ERROR)
logging.getLogger('discord.http').setLevel(logging.ERROR)
logging.getLogger('discord.gateway').setLevel(logging.ERROR)
logging.getLogger('discord.state').setLevel(logging.ERROR)
logging.getLogger('discord.client').setLevel(logging.ERROR)

os.system('cls')

watermark = f"""
  sSSs   .S_SSSs     .S   .S_sSSs    sdSS_SSSSSSbs    sSSs   .S_sSSs     .S    S.    .S_SSSs    sdSS_SSSSSSbs    sSSs  
 d%%SP  .SS~SSSSS   .SS  .SS~YS%%b   YSSS~S%SSSSSP   d%%SP  .SS~YS%%b   .SS    SS.  .SS~SSSSS   YSSS~S%SSSSSP   d%%SP  
d%S'    S%S   SSSS  S%S  S%S   `S%b       S%S       d%S'    S%S   `S%b  S%S    S%S  S%S   SSSS       S%S       d%S'    
S%|     S%S    S%S  S%S  S%S    S%S       S%S       S%S     S%S    S%S  S%S    S%S  S%S    S%S       S%S       S%S     
S&S     S%S SSSS%S  S&S  S%S    S&S       S&S       S&S     S%S    S&S  S%S SSSS%S  S%S SSSS%S       S&S       S&S     
Y&Ss    S&S  SSS%S  S&S  S&S    S&S       S&S       S&S_Ss  S&S    S&S  S&S  SSS&S  S&S  SSS%S       S&S       S&S_Ss  
`S&&S   S&S    S&S  S&S  S&S    S&S       S&S       S&S~SP  S&S    S&S  S&S    S&S  S&S    S&S       S&S       S&S~SP  
  `S*S  S&S    S&S  S&S  S&S    S&S       S&S       S&S     S&S    S&S  S&S    S&S  S&S    S&S       S&S       S&S     
   l*S  S*S    S&S  S*S  S*S    S*S       S*S       S*b     S*S    d*S  S*S    S*S  S*S    S&S       S*S       S*b     
  .S*P  S*S    S*S  S*S  S*S    S*S       S*S       S*S.    S*S   .S*S  S*S    S*S  S*S    S*S       S*S       S*S.    
sSS*S   S*S    S*S  S*S  S*S    S*S       S*S        SSSbs  S*S_sdSSS   S*S    S*S  S*S    S*S       S*S        SSSbs  
YSS'    SSS    S*S  S*S  S*S    SSS       S*S         YSSP  SSS~YSSY    SSS    S*S  SSS    S*S       S*S         YSSP  
               SP   SP   SP               SP                                   SP          SP        SP                
               Y    Y    Y                Y                                    Y           Y         Y                  
"""

faded_text = fade.fire(watermark)

print(faded_text)

print(f"{Fore.RED} FOR HELP CONTACT | Telegram t.me/falsedeity | Discord: SaintedHate |")

print(f"{Fore.YELLOW}OUTPUTS:")
print(f'Logged in go fuck around nigga')

TOKEN = token_variable

bot = commands.Bot(command_prefix='.', self_bot=True)
PREFIX = "."

autoresponses = {}

user_reactions = {}

ld_running = False

lg_running = False

ac_running = False

outlasting_num = {}

gc_task_list = {}

user_has_sent_message = {}

deleted_messages = {}

purge_active = False

APIIPKEY = "a9443d44cb614bd0955051640a075c47"


allowed_prefixes = {',', '.', '?', '@', '-', '+', '~'}

phrases = [
"# shitstain focus on me son",
"# ur so ass bro who even loves u",
"# cover ur belly rolls with ur hoodies bro it keeps rolling on the ground",
"# im ur god nigga LOL",
"# pooron u write anime quotes for a living",
"# i made u nigga bow down to ur creator",
"# lets take a breathe break to laugh at this stupid autistic nigga",
"# do u get attention at home lil bro?",
"# Nigga what your mom was selling spaghetti flavoured meatballs in the walmart parking-lot and thought she was a genius",
"# LMAO SON I OWN U",
"# BITCH ASS NIGGA CALL ME DADA LIKE A GOOD BITCH",
"# Nigga all the legendary pokemon gang banged yo momma cuz she had a Ultra poke-ball boy and when they found out she wasn't a pokemon trainer they evolved",
"# UR MY PRE-CUM NIGGA LMAOO",
"# IS BRO GETTING PRESSED RN",
"# You get frostbites when you wake up cuz you sleep naked with yo fan on full power nigga",
"# You sneak into people houses just to steal they crayola crayons just to duo draw a rainbow with ya nephew nigga",
"# You a real life fortnite chararcter nigga when someone kills you everything you own just gon float above yo body and niggas gon come pick it up nigga",
"# You went inside the Transporter in Henry Danger because yo knee caps got stolen by Dr. EggMan my nigga you dumb as shit",
"# That's why yo girl friend was in the lofi hip hop radio live stream simping to anime weebz for robux nigga you dumb as shit",
"# BRO UR SO ASS JUST QUIT SOCIALS NOBODY LIKES U",
"# WHEH WILL THIS NIGGA STOP YAPPING WITH HIS SHITTY JOKES",
"# ARYA READY TO SUCK MY DICK NIGGA",
"# NAT MY NUTS IN UR MOUTH STUPID NIGGA",
"# you get bullied irl so you try to act cool online 'heres a difference between me irl and me online' dumb ass nigga",
"# pooron ass nigga stop trying",
]

victims = {}

messages = [
    "T'as l'air d'un harmonica pessimiste avec un handicap visuel.",
    "Pareces un proyectil de mortero desnudo y asustado con una discapacidad visual.",
    "You got beat up by a disobedient cupcake with Buzz Lightyear boots on.",
    "Du versteckst Toilettensitze im Joystick, um zu verhindern, dass sie für immer überfahren werden.",
    "Sei caduto da un jet da combattimento e ti sei trasformato in una borsa della spesa bohemienne con calcoli renali.",
    "Você parece um tabuleiro de xadrez ambicioso com uma deficiência visual.",
    "Niggas dad has a pepper shaker toenail.",
    "君はキャンドルスティックのようで、ハマグリの指がついている。",
    "Tu es resté coincé au plafond, alors maintenant tu dois en savoir plus sur le morceau de couverts sans un ver de l'air essayant de trouver l'école où tu es allé.",
    "У дяди ниггера нос с лазерным прицелом.",
    "Nigga mom got a bowman from Black Ops kneecap.",
    "Pareces Quandale Dingle con un bigote en la cara.",
    "Igel-Zylinder-aussehender Arsch, Nigga.",
    "Tua zia va al parco acquatico solo per lanciare panini Subway alla gente, è strana come l'inferno.",
    "You're the only fat nigga I know who can do Brawlhalla combos with their titties, you weird as shit."
]

nitro_sniper_enabled = False
toaster = ToastNotifier()

mimic_channels = set()

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.command()
async def change(ctx, prefix: str):
    if len(prefix) != 1 or prefix in string.ascii_letters or prefix not in allowed_prefixes:
        await ctx.send("Invalid Char")
        return
    
    bot.command_prefix = prefix
    await ctx.send(f"Prefix changed to: {prefix}")


Bot_vers = f"""
```ansi
[2;31m| SAINTED SB v2 | Creds: SaintedHate |[0m
```
"""

divider = f"""
```ansi
[2;31m[2;34m_______________________________________________[0m[2;31m[2;34m[0m[2;31m[0m
```
"""

Bot_prefix = f"""
```ansi
[2;31m| SAINTED SB | PREFIX: " {PREFIX} " |[0m
```
"""

categories = f"""
```ansi
[2;33m|SAINTED SB V2 | CREDS: SAINTEDHATE |
           | CATEGORIES |
[2;31m{PREFIX}fun [2;37m| [2;34mUse:[2;32m {PREFIX}fun[2;30m - Displays fun commands

[2;31m{PREFIX}chatpack [2;37m|[2;34m Use:[2;32m [0m[2;34m[0m[2;37m[0m[2;31m[0m[2;30m[0m[2;32m{PREFIX}chatpack[2;30m - Displays chat pack commands

[0m[2;32m[2;31m[0m[2;32m[2;31m{PREFIX}tools[2;37m|[2;34m Use:[2;32m[0m[2;34m[0m[2;37m[0m[2;31m[2;32m {PREFIX}tools[2;30m - Commands for tools like Ports Scan

[0m[2;32m[0m[2;31m[0m[2;32m[2;31m[0m[2;32m[2;31m{PREFIX}info[2;37m|[2;34m Use:[2;32m [0m[2;34m[0m[2;37m[0m[2;31m[2;32m{PREFIX}info[2;30m - Commands for info on user or server

[0m[2;32m[0m[2;31m[0m[2;32m[2;37m[2;37m[2;31m{PREFIX}raid[2;37m|[2;34m Use:[2;32m [0m[2;34m[0m[2;37m[0m[2;31m[2;32m{PREFIX}raid[2;30m - Raid Tools/commands

[0m[2;32m[2;30m[0m[2;32m[0m[2;31m[0m[2;37m[2;31m[2;31m[0m[2;31m[0m[2;37m[2;31m{PREFIX}settings[2;37m|[2;34m Use:[2;32m {PREFIX}settings[2;30m - Settings configs like Afk
[0m[2;32m[0m[2;34m[0m[2;37m[0m[2;31m
[0m[2;37m[0m[2;37m[0m[2;32m[0m[2;34m[0m[2;37m[0m[2;31m[0m[2;33m[0m
```
"""

fun_commands = f"""
```ansi
[2;33m|SAINTED SB V2 | CREDS: SAINTEDHATE |
           | FUN COMMANDS|
[2;31mToken Sniff [2;37m| [2;34mUse:[2;32m {PREFIX}ts <mention_user>[2;30m - Uses Base64 to get first third of token and a bit of random numbers

[2;31mAura [2;37m|[2;34m Use:[2;32m [0m[2;34m[0m[2;37m[0m[2;31m[0m[2;30m[0m[2;32m{PREFIX}aura[2;30m - Shows your aura (Displays a message and sends randomized aura gif)

[0m[2;32m[2;31m[0m[2;32m[2;31mGay Rate[2;37m|[2;34m Use:[2;32m[0m[2;34m[0m[2;37m[0m[2;31m[2;32m {PREFIX}gr <mention_user>[2;30m - Generates a random gay percentage of mentioned user

[0m[2;32m[0m[2;31m[0m[2;32m[2;31m[0m[2;32m[2;31mRape[2;37m|[2;34m Use:[2;32m [0m[2;34m[0m[2;37m[0m[2;31m[2;32m{PREFIX}rape <mention_user>[2;30m - Troll rapes the person

[0m[2;32m[0m[2;31m[0m[2;32m[2;37m[2;37m[2;31mSWAT[2;37m|[2;34m Use:[2;32m [0m[2;34m[0m[2;37m[0m[2;31m[2;32m{PREFIX}swat 911 <mention_user> <fake_address/real_address>[2;30m - Troll swat similar to the rape

[0m[2;32m[2;30m[0m[2;32m[0m[2;31m[0m[2;37m[2;31m[2;31m[0m[2;31m[0m[2;37m[2;31mInfinite Cat Generator[2;37m|[2;34m Use:[2;32m {PREFIX}cat[2;30m - Cat loop[0m[2;32m[0m[2;34m[0m[2;37m[0m[2;31m
[0m[2;37m[0m[2;37m[0m[2;32m[0m[2;34m[0m[2;37m[0m[2;31m[0m[2;33m[0m
```

"""

Chatpack_commands = f"""
```ansi
[2;33m|SAINTED SB V2 | CREDS: SAINTEDHATE |
           | CHATPACK COMMANDS|
[2;31mOut Last [2;37m| [2;34mUse:[2;32m {PREFIX}ol <mention_user>[2;30m - outlasts user until stopped by using ".ols"

[2;31mChat Spam [2;37m|[2;34m Use:[2;32m [0m[2;34m[0m[2;37m[0m[2;31m[0m[2;30m[0m[2;32m{PREFIX}cs <text_to_spam>[2;30m - spams given text until stopped by using ".csoff"

[0m[2;32m[2;31m[0m[2;32m[2;31mGroup Chat Outlaste[2;37m|[2;34m Use:[2;32m[0m[2;34m[0m[2;37m[0m[2;31m[2;32m {PREFIX}gcl <text_to_use>[2;30m - Groupchat outlasts using given text until stopped by using ".gcls"

[0m[2;32m[0m[2;31m[0m[2;32m[2;31m[0m[2;32m[2;31mAuto Flame/Ladder[2;37m|[2;34m Use:[2;32m [0m[2;34m[0m[2;37m[0m[2;31m[2;32m{PREFIX}ld <mention_user>[2;30m - Auto Ladders/Flames until stopped by using ".lds"

[0m[2;32m[0m[2;31m[0m[2;32m[2;37m[2;37m[2;31mAuto Respond[2;37m|[2;34m Use:[2;32m [0m[2;34m[0m[2;37m[0m[2;31m[2;32m{PREFIX}ar <mention_user> <text_to_use>[2;30m - Auto replies to mentioned user with given text until stopped by using ".ars" (note this will stop ALL autoresponds)

[0m[2;32m[2;30m[0m[2;32m[0m[2;31m[0m[2;37m[2;31m[2;31m[0m[2;31m[0m[2;37m[2;31mAuto React[2;37m|[2;34m Use:[2;32m {PREFIX}rs <mention_user> <emoji_to_react_with>[2;30m - auto reacts to mentioned user with given emoji until stopped by using ".rse <mention_user>"
[0m[2;32m[0m[2;34m[0m[2;37m[0m[2;31m
[0m[2;37m[0m[2;37m[0m[2;32m[0m[2;34m[0m[2;37m[0m[2;31m[0m[2;33m[0m
[2;31mAuto AFK Check [2;37m| [2;34mUse:[2;32m {PREFIX}ac <mention_user>[2;30m - Afk checks user with a 20 count down or can be stopped by using ".acs"

[2;31mVictimize [2;37m| [2;34mUse:[2;32m {PREFIX}victimize <mention_user>[2;30m - auto replies to user with a list of phrases that it goes through once each and then loops, can be stopped by using ".victimizest"
```

"""

Tool_commands = f"""
```ansi
[2;33m|SAINTED SB V2 | CREDS: SAINTEDHATE |
           | TOOL COMMANDS|
[2;31mIP Lookup [2;37m| [2;34mUse:[2;32m {PREFIX}iplookup <IP_address>[2;30m - looks up basic info on an IP address

[2;31mPort Scan [2;37m|[2;34m Use:[2;32m [0m[2;34m[0m[2;37m[0m[2;31m[0m[2;30m[0m[2;32m{PREFIX}portscan <IP_ADDRESS>[2;30m - scans IP address for Open ports
```
"""

Info_commands = f"""
```ansi
[2;33m|SAINTED SB V2 | CREDS: SAINTEDHATE |
           | INFO COMMANDS|
[2;31mServer Info [2;37m| [2;34mUse:[2;32m {PREFIX}sf[2;30m - provides basic info of a server

[2;31mSpy [2;37m|[2;34m Use:[2;32m [0m[2;34m[0m[2;37m[0m[2;31m[0m[2;30m[0m[2;32m{PREFIX}spy <mention_user>[2;30m - Gives Basic info on given user
```
"""

Raid_commands = f"""
```ansi
[2;33m|SAINTED SB V2 | CREDS: SAINTEDHATE |
           | CHATPACK COMMANDS|
[2;31mMass Channel Create [2;37m| [2;34mUse:[2;32m {PREFIX}chs <number_of_channels> <number_of_messages_to_send> <message>[2;30m - deletes all existing channels and categories, then make new channels, amount being input amount, then amount of messages to be send will send that many messages of the given message in each new channel.

[2;31mMass Role Create [2;37m| [2;34mUse:[2;32m {PREFIX}rls <number_of_roles> <role_names>[2;30m - deletes all previous roles that it can then creates new roles with given name and amount is given amount

[2;31mKill Server[2;37m| [2;34mUse:[2;32m {PREFIX}death <server_new_name> <image_url>[2;30m - changes server name to given name and image to given image url
```
"""

Settings_commands = f"""
```ansi
[2;33m|SAINTED SB V2 | CREDS: SAINTEDHATE |
           | CATEGORIES |
[2;31mNitro Sniper [2;37m| [2;34mUse:[2;32m {PREFIX}ns[2;30m - Looks for nitro codes/gifts and redeems them, Notification and message shows if it was valid or not (toggle based command)
```
"""


@bot.command()
async def menu(ctx):
    await ctx.message.delete()   
    await ctx.send(Bot_vers)
    await asyncio.sleep(0.1)
    await ctx.send(Bot_prefix)
    await asyncio.sleep(0.1)
    await ctx.send(categories)
    
@bot.command()
async def fun(ctx):
    await ctx.message.delete()
    await ctx.send(Bot_vers)
    await asyncio.sleep(0.1)
    await ctx.send(Bot_prefix)
    await asyncio.sleep(0.1)
    await ctx.send(fun_commands)
    
@bot.command()
async def chatpack(ctx):
    await ctx.message.delete()
    await ctx.send(Bot_vers)
    await asyncio.sleep(0.1)
    await ctx.send(Bot_prefix)
    await asyncio.sleep(0.1)
    await ctx.send(Chatpack_commands)
    
@bot.command()
async def tools(ctx):
    await ctx.message.delete()
    await ctx.send(Bot_vers)
    await asyncio.sleep(0.1)
    await ctx.send(Bot_prefix)
    await asyncio.sleep(0.1)
    await ctx.send(Tool_commands)
 
@bot.command()
async def info(ctx):
    await ctx.message.delete()
    await ctx.send(Bot_vers)
    await asyncio.sleep(0.1)
    await ctx.send(Bot_prefix)
    await asyncio.sleep(0.1)
    await ctx.send(Info_commands)
 
@bot.command()
async def raid(ctx):
    await ctx.message.delete()
    await ctx.send(Bot_vers)
    await asyncio.sleep(0.1)
    await ctx.send(Bot_prefix)
    await asyncio.sleep(0.1)
    await ctx.send(Raid_commands)

@bot.command()
async def settings(ctx):
    await ctx.message.delete()
    await ctx.send(Bot_vers)
    await asyncio.sleep(0.1)
    await ctx.send(Bot_prefix)
    await asyncio.sleep(0.1)
    await ctx.send(Settings_commands)
 
@bot.command()
async def sf(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    serverinfo = f"""
```ansi
[2;31m[2;34mServer ID: {guild.id}
Server name: {guild.name}
Server owner: {guild.owner.name if guild.owner else "Unknown"}
Verification level :{guild.verification_level.name}
Creation time: {guild.created_at.strftime("%Y-%m-%d %H:%M:%S")}
Member count: {guild.member_count}
Boost level: {guild.premium_tier}[0m[2;31m
[0m
```
"""
    await ctx.send(Bot_vers)
    await ctx.send(Bot_prefix)
    await ctx.send(serverinfo)
    
@bot.command()
async def pi(ctx):
    await ctx.message.delete()
    x = os.system("ping discord.com | findstr delay")
    delay_message = f"""
    ```
    SAINTED SB V2
    ______________________________________________________________
    
    Discord delay: {x} ms
    
    made by: saintedhate
    ```
    """
    await ctx.send(delay_message)
    
@bot.command()
async def cs(ctx, *, message: str):
    global spamming
    await ctx.message.delete()
    spamming = True

    while spamming:
        await ctx.send(message)

@bot.command()
async def csoff(ctx):
    global spamming
    await ctx.message.delete()
    spamming = False
    await ctx.send("you got hoed gg")

@bot.command()
async def ar(ctx, member: discord.Member, *, message: str):
    await ctx.message.delete()
    
    def check(m):
        return m.author == member and m.channel == ctx.channel

    autoresponses[ctx.channel.id] = True

    try:
        while ctx.channel.id in autoresponses:
            response = await bot.wait_for('message', check=check, timeout=None)
            await response.reply(message)
    except asyncio.CancelledError:
        pass
    except asyncio.TimeoutError:
        await ctx.send(f"{member.display_name} died cold")

@bot.command()
async def ars(ctx):
    await ctx.message.delete()
    if ctx.channel.id in autoresponses:
        del autoresponses[ctx.channel.id]
        await ctx.send("I won gg")
    else:
        await ctx.send("I won gg")

@bot.command()
async def spy(ctx, member: discord.Member):
    await ctx.message.delete()
    info = f"""
```ansi
[2;31m[2;34m[2;33m    Username: {member.display_name}
    ID: {member.id}
    Created At: {member.created_at.strftime("%Y-%m-%d %H:%M:%S")}
    Joined At: {member.joined_at.strftime("%Y-%m-%d %H:%M:%S")}
    Avatar: {member.avatar.url if member.avatar else member.default_avatar.url}[0m[2;34m[0m[2;31m
[0m
```
    ||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​||||​|| {member.avatar.url if member.avatar else member.default_avatar.url}
    """
    await ctx.send(Bot_vers)
    await ctx.send(Bot_prefix)
    await ctx.send(info)
    
@bot.command()
async def ld(ctx, member: discord.Member):
    await ctx.message.delete()
    global ld_running
    ld_running = True
    messages = [
    "lame ass nigga shut the fuck up ugly faxxxgxgoxxt",
    "stfu faxgxxxxgoxxxxt boy go brush your teeth smelly nigga",
    "lame ass skidder larp",
    "autistic aeroplane",
    "nigga nose look like a blast furnace",
    "dont you like gummy worms up your butt freak",
    "waaah waaah waaah get your shit slapped lame ass nigga",
    "you trash as FUCK \n STUPID \n ASS \n NIGGA \n FUCKING \n LOSER \n ASS \n FAXGXGxxOXT",
    "i heard you said 'go deeper' to your doctor at the prostate exam loser faxxgxgoxxxt geek",
    " yo stfu ",
    "YOURE BEING CUCKED RN THEY DONT WANT YOU LMFFAOAO",
    "loser geek",
    "trash kid",
    "small faxgxgxxoxxt",
    "keep licking old men forexsxsxkin dixcxk gobbler",
    "yo guess what",
    "your ass fucking loser nigga ",
    "you're a mutt",
    "you died to me",
    "youre a 2 wpm demon",
    "gayass nigga I dont rate you g",
    "you're piss poor",
    "slow ass nigga",
    "LO",
    "L",
    "OO",
    "LO",
    "OL",
    "YOURE UGLY AS SHIT NIGGA",
    "LO",
    "O",
    "OLO",
    "LL",
    "NAME A COM THAT CLAIMS YOU",
    "YOURE A PUNCHING BAG",
    "LOSER NIGGA GOT CUCKED LMFOAOA",
    "# YOURE DYING TO ME KEEP UP G",
    "# I OWN YOUR RETARDED ASS",
    "DONT GET LOST NOW",
    "FOCUS GEEK",
    "NO ONE FEARS YOU",
    "PEDO NIGGA",
    "LOOK AT YOU FALLING BEHIND LMFOAOA",
    "PISS POOR RANDOM LMFOAOA",
    "SLOW NIGGA",
    "dont die already im not done with you geek",
    "you cant keep up",
    "Ima put you 6 feet deep in this chat you're dying to me LOLOL",
    "keep up Im not even done g",
    "you're corny no one laughed",
    "You're my son",
    "failed jr ass nigga",
   "clone ass nigga,",
   "dont repeat :rofl:",
    ]

    for message in messages:
        if not ld_running:
            break
        await ctx.send(f'{message} {member.mention}')

@bot.command()
async def lds(ctx):
    global ld_running
    ld_running = False
    await ctx.send("GG CANT KEEP UP")
    
@bot.command()
async def ac(ctx, member: discord.Member):
    await ctx.message.delete()
    global ac_running
    ac_running = True
    messages = [
        "AFK CHECK SAY 'NOT AFK' LOLOL",
        "20",
        "19",
        "18",
        "17",
        "16",
        "15",
        "14",
        "13",
        "12",
        "11",
        "10",
        "9",
        "8",
        "7",
        "6",
        "5",
        "4",
        "3",
        "2",
        "1",
        "0",
        "GG NIGGA GOT SENT TO SLEEP LMFAOOAO",
    ]

    for message in messages:
        if not ac_running:
            break
        await ctx.send(f'{member.mention} {message}')

@bot.command()
async def acs(ctx):
    await ctx.message.delete()
    global ac_running
    ac_running = False
    await ctx.send("GG NIGGAS AFK LMFOAOA")

@bot.command()
async def ol(ctx, member: discord.Member, *, message: str):
    await ctx.message.delete()
    if ctx.channel.id in outlasting_num:
        await ctx.send("Outlast already active")
        return
    task = bot.loop.create_task(outlast_up(ctx, member, message))
    outlasting_num[ctx.channel.id] = task

@bot.command()
async def ols(ctx):
    await ctx.message.delete()
    if ctx.channel.id in outlasting_num:
        task = outlasting_num[ctx.channel.id]
        task.cancel()
        del outlasting_num[ctx.channel.id]
        await ctx.send("# NIGGA WENT TO SLEEP GG")
    else:
        await ctx.send("No outlast active")

async def outlast_up(ctx, member: discord.Member, message: str):
    count = 1
    try:
        while True:
            await ctx.send(f"{member.mention} {message} {count}")
            count += 1
            await asyncio.sleep(0)
    except asyncio.CancelledError:
        pass
    
@bot.command()
async def rape(ctx, user: discord.User):
    await ctx.message.delete()
    message = await ctx.send(f"{user.mention}, YOU ARE GETTING RAPED LOL")
    edit_messages = [
    "**Unzips dick**",
    "**Puts it in your mouth**",
    "**Aggresivly pulls your hair knowing you dont like it **😈 😈 ",
    "**Starts going harder while seeing you choking**",
    "Ohh im about to cum💦 💦 ",
    "**Fills your mouth with my cum**",
    "Goodboy.❤️❤️"
    ]

    for i in range(7):
        await asyncio.sleep(1)
        edit_content = edit_messages[i % len(edit_messages)]
        await message.edit(content=f"{user.mention}, {edit_content}")
        
@bot.command()
async def swat(ctx, phone: int, targ: discord.User, *, addy: str):
    await ctx.message.delete()
    message = await ctx.send(f"📞 | $ | Calling police | $ | 📞")
    time.sleep(5)
    script = [
    f"```{phone}: Emergency services how can I help you```",
    f"```{message.author}: Hello, this is {targ.name} speaking, There is a bomb planted in your building. It will detonate in 30 minutes.```",
    f"```{phone}: I understand. Thank you for letting us know. Can you provide any specific information about the location or nature of the threat?```",
    f"```{message.author}: I am at {addy}, I have 2 fully automatic weapons on me```",
    f"```{phone}: Thank you, A swat team is on route to your location```",
    f"```{message.author}: They betta be ready```",
    ]
    for s in script:
        await message.edit(content=s)
        time.sleep(2)
    await message.edit(content=f"📞 | $ | Ended call | $ | 📞")

@bot.command()
async def portscan(ctx, ip):
    t = time.localtime()
    currenttime = time.strftime("%H:%M", t)
    await ctx.message.delete()
    ports = [
        20,     # FTP Data
        21,     # FTP Control
        22,     # SSH
        23,     # Telnet
        25,     # SMTP
        53,     # DNS
        80,     # HTTP
        110,    # POP3
        119,    # NNTP
        143,    # IMAP
        443,    # HTTPS
        465,    # SMTPS
        587,    # SMTP (Submission)
        993,    # IMAPS
        995,    # POP3S
        3306,   # MySQL
        5432,   # PostgreSQL
        8080,   # HTTP Proxy
        8443    # HTTPS Alternate
    ]
    open_ports = []
    closed_ports = []
    os = ""

    for port in ports:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        result = s.connect_ex((ip, port))
        s.close()
        if result == 0:
            open_ports.append(port)
        else:
            closed_ports.append(port)
    for port in open_ports:
        os += f"Port: {port}\n"

    message1 = f"""
```ansi
    [2;31m[2;36m[2;35mNEXUS SB | V2 | PORTSCAN
```
"""

    message2 = f"""
```ansi
[2;31m[2;36m[2;35m{os}[0m[2;36m[0m[2;31m
[0m
```
```
    """
    await ctx.send(Bot_vers)
    await ctx.send(Bot_prefix)   
    await ctx.send(message1)
    await ctx.send(message2)

@bot.command()
async def iplookup(ctx, ip):
    t = time.localtime()
    currenttime = time.strftime("%H:%M", t)
    if APIIPKEY:
        await ctx.message.delete()
        lookuopurl = f'https://api.ipgeolocation.io/ipgeo?apiKey={APIIPKEY}&ip={ip}'
        response = requests.get(
            lookuopurl, headers={
                'Accept': 'application/json'})
        ip_info = response.json()
        city = ip_info['city']
        region = ip_info['continent_name']
        regioncode = ip_info['continent_code']
        countryname = ip_info['country_name']
        countrycode = ip_info['country_code2']
        countrycapital = ip_info['country_capital'] 
        postalcode = ip_info['zipcode']
        latitude = ip_info['latitude']
        longitude = ip_info['longitude']
        timezone = ip_info['time_zone']['name']
        currentiptime = ip_info['time_zone']['current_time']
        isp = ip_info['isp']
        info = f"""
```ansi
[2;32mRegion: {region} | {regioncode}
Country: {countryname} | {countrycode}
Captial: {countrycapital}
Postal code: {postalcode}
Latitude: {latitude}
Longitude: {longitude}
Timezone: {timezone}
PostalCode: {postalcode}
ISP: {isp}
TIME: {currentiptime}
Region Code: {regioncode}[0m
```
"""
        message = info
        await ctx.send(Bot_vers)
        await ctx.send(Bot_prefix)
        await ctx.send(message)

@bot.command()
async def sts(ctx, user, *, rpc):
    await ctx.message.delete()
    await bot.change_presence(activity=discord.Streaming(name=rpc, url=f"https://twitch.tv/{user}"))
    
@bot.command()
async def sd(ctx, limit: int):
    async for message in ctx.channel.history(limit=limit):
        if message.author.id == bot.user.id:
            await message.delete()
            time.sleep(1)

@bot.command()
async def cat(ctx):
    await ctx.message.delete()
    gen = "https://tenor.com/view/cat-generator-gif-22648083"
    steal = "https://tenor.com/view/cat-stealer-gif-21321506"
    await ctx.send(gen)
    await ctx.send(steal)
    
@bot.command()
async def ts(ctx, user: discord.User):
    await ctx.message.delete()
    token = base64.b64encode(str(user.id).encode('utf-8')).decode('utf-8').rstrip('=')
    info = f"""
    ```
    SAINTED SB V2 TOKEN SNIFF RESULT
>-------------------------------------------------------<
Username: {user.name}
User ID: {user.id}

>-------------------------------------------------------<
Token: {token}.[HIDDEN]
>-------------------------------------------------------<
```
    """
    url = info
    await ctx.send(url)

async def change_gc_name(channel, base_name):
    count = 1
    try:
        while True:
            new_name = f"{base_name} {count}"
            await channel.edit(name=new_name)
            count += 1
            await asyncio.sleep(0.5)
    except asyncio.CancelledError:
        pass

@bot.command()
async def gcl(ctx, *, base_name: str):
    await ctx.message.delete()
    global gc_task_list

    if not isinstance(ctx.channel, discord.GroupChannel):
        return

    channel = ctx.channel

    if channel.id in gc_task_list:
        await ctx.send(":rofl:")
        return

    task = bot.loop.create_task(change_gc_name(channel, base_name))
    gc_task_list[channel.id] = task
    await ctx.send(f"OUT LAST ME LMFOAOAOAO.")

@bot.command()
async def gcls(ctx):
    await ctx.message.delete()
    global gc_task_list

    if not isinstance(ctx.channel, discord.GroupChannel):
        return

    channel = ctx.channel
    if channel.id in gc_task_list:
        task = gc_task_list[channel.id]
        task.cancel()
        del gc_task_list[channel.id]
        await ctx.send(f"gg outlasted.")
    else:
        await ctx.send("inactive")


@bot.event
async def on_message_delete(message):
    if message.content.startswith('.'):
        return

    if isinstance(message.channel, discord.DMChannel):
        channel_name = f"Dms with {message.channel.recipient.display_name}"
    else:
        channel_name = f"Channel: {message.channel.name} (ID: {message.channel.id})"

    channel_id = message.channel.id
    if channel_id not in deleted_messages:
        deleted_messages[channel_id] = []
    
    central = pytz.timezone('US/Central')
    sent_time = message.created_at.astimezone(central)
    deleted_time = datetime.now(central)
    
    deleted_message = (message, sent_time, message.author, channel_name)
    deleted_messages[channel_id].append(deleted_message)

    with open('logger.txt', 'a', encoding='utf-8') as file:
        file.write(f"Channel: {channel_name}\n")
        file.write(f" - Sent at: {sent_time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        file.write(f" - Author: {message.author.name}\n")
        file.write(f" - Content: {message.content}\n")
        file.write(f" - Deleted at: {deleted_time.strftime('%Y-%m-%d %H:%M:%S')}\n\n")

@bot.command()
async def snipe(ctx, position: int = 1):
    await ctx.message.delete()
    channel_id = ctx.channel.id
    if channel_id in deleted_messages:
        deleted_message_list = deleted_messages[channel_id]
        if 1 <= position <= len(deleted_message_list):
            deleted_message, sent_time, deleted_author, channel_name = deleted_message_list[-position]
            author_name = deleted_author.name
            author_discriminator = deleted_author.discriminator
            author_id = deleted_author.id

            if deleted_message.attachments:
                media_info = deleted_message.attachments[0].url
                content_info = None
            else:
                media_info = None
                content_info = deleted_message.content if deleted_message.content else "(message deleted)"
                
            central = pytz.timezone('US/Central')
            deleted_time = sent_time + timedelta(hours=6)
            deleted_time = deleted_time.astimezone(central).strftime('%Y-%m-%d %H:%M:%S')

            await ctx.send(Bot_vers)
            if content_info:
                await ctx.send(f"```ansi\n[2;34mCONTENT: {content_info} [DELETED AT: {deleted_time}][0m\n```")
            elif media_info:
                await ctx.send(f"```ansi\n[2;34mMEDIA: [{media_info}] [DELETED AT: {deleted_time}][0m\n```")
            await ctx.send(f"```fix\nAUTHOR: [{author_name}#{author_discriminator}]"
                           f"  ID: [{author_id}]\n```")

            if media_info:
                await ctx.send(f"{media_info}")
        else:
            await ctx.send(Bot_vers)
            await ctx.send(f"```ansi\n[2;34mPOSITION OUT OF RANGE OR NO RECENTLY DELETED MESSAGES FOUND.[0m\n```")
    else:
        await ctx.send(Bot_vers)
        await ctx.send(f"```ansi\n[2;34mPOSITION OUT OF RANGE OR NO RECENTLY DELETED MESSAGES FOUND.[0m\n```")

@bot.event
async def on_message(message):
    # Process commands first
    await bot.process_commands(message)

    # User Reaction Logic
    if message.author.id in user_reactions:
        emoji = user_reactions[message.author.id]
        await message.add_reaction(emoji)

    # Nitro Sniper Logic
    if nitro_sniper_enabled:
        nitro_code_pattern = re.compile(r'(discord.gift/|https://discord.gift/)([a-zA-Z0-9]+)')
        nitro_match = nitro_code_pattern.search(message.content)

        if nitro_match:
            code = nitro_match.group(2)
            print(f"Found Nitro code: {code}")

            headers = {
                'Authorization': bot.http.token,
                'Content-Type': 'application/json',
            }

            response = requests.post(
                f'https://discord.com/api/v9/entitlements/gift-codes/{code}/redeem',
                headers=headers,
            )

            if response.status_code == 200:
                await message.channel.send("Nitro Sniped: The code was valid and redeemed.")
            else:
                await message.channel.send("Nitro Sniped: The code was already used or invalid.")

            toaster.show_toast("Nitro Sniped", "Check the bot's response in Discord", duration=5)

    # Target User Mention Logic
    if message.author == bot.user and message.content.startswith('yo peep this') and message.mentions:
        target_user = message.mentions[0]
        target_user_mention = target_user.mention

        for msg in messages:
            await message.channel.send(f'{target_user_mention} {msg} :skull:')
    
@bot.command()
async def rs(ctx, user: discord.User, emoji: str):
    await ctx.message.delete()
    user_reactions[user.id] = emoji
    await asyncio.sleep(0)
    await ctx.message.delete()

@bot.command()
async def rse(ctx, user: discord.User):
    await ctx.message.delete()
    if user.id in user_reactions:
        del user_reactions[user.id]
    else:
        await ctx.send(f"```md\n# RichModels | No reaction set for user {user.name}\n # MADE BY RICHMODELS```", delete_after=2)
    
@bot.command()
async def noleave(ctx, user: discord.User, gc_id: int):
    global user_id_to_add
    user_id_to_add = user.id
    run_threads(user.id, gc_id)
    await asyncio.sleep(1)
    await ctx.message.delete()
        
@bot.command()
async def gr(ctx, member: discord.Member = None):
    await ctx.message.delete()
    if member is None:
        await ctx.send("Please mention a user")
    else:
        rating = random.randint(0, 100)
        gayrate = f"""
        ```md\n# SAINTED SB V2\n```
       ``` _______________________________________________```
        USER: {member.mention}
       ``` _______________________________________________```
        ```md\n# IS {rating} % GAY\n```
        
        
        """
        await ctx.send(gayrate)
        
@bot.command()
async def clean(ctx, amount: int = None):
    global purge_active
    purge_active = True
    await ctx.message.delete()
    if amount is None:
        async for message in ctx.message.channel.history(limit=10000):
            if not purge_active:
                break
            if message.author == bot.user:
                try:
                    await message.delete()
                except discord.HTTPException:
                    pass
    else:
        async for message in ctx.message.channel.history(limit=amount):
            if not purge_active:
                break
            if message.author == bot.user:
                try:
                    await message.delete()
                except discord.HTTPException:
                    pass
    
@bot.command()
async def cleanst(ctx):
    global purge_active
    purge_active = False
    
gif_links = [
    "https://tenor.com/view/mob-psycho-season3-mob-psycho-shigeo-shigeo-kageyama-mob-gif-26873452",
    "https://tenor.com/view/aura-de-insanidade-gif-25469126",
    "https://tenor.com/view/red-aura-shanks-gif-15239642149115408408",
    "https://tenor.com/view/hellsing-alucard-power-up-dark-aura-gif-16526700",
    "https://tenor.com/view/devil-anime-evil-gif-17413754",
    "https://tenor.com/view/anime-gif-25980167",
    "https://tenor.com/view/rolecism-role-roles-look-at-these-roles-check-these-roles-gif-1210171411774150648",
]

aura_message = f"""
```ansi
[2;31mFeel my aura and bow down to me.[0m
```
"""

aura_bot = f"""
```ansi
[2;31mSAINTED SB | V2 | AURA: INFINITE+[0m
```
"""

@bot.command()
async def aura(ctx):
    await ctx.message.delete()
    await ctx.send(aura_bot)
    await ctx.send(aura_message)
    gif = random.choice(gif_links)
    await ctx.send(gif)

@bot.command()
async def victimize(ctx, member: discord.Member):
    await ctx.message.delete()

    def check(m):
        return m.author == member and m.channel == ctx.channel

    victims[ctx.channel.id] = True
    phrase_index = 0

    try:
        while ctx.channel.id in victims:
            response = await bot.wait_for('message', check=check, timeout=None)
            await response.reply(phrases[phrase_index])
            phrase_index = (phrase_index + 1) % len(phrases)
    except asyncio.CancelledError:
        pass
    except asyncio.TimeoutError:
        await ctx.send(f"{member.display_name} died cold")

@bot.command()
async def victimizest(ctx):
    await ctx.message.delete()
    if ctx.channel.id in victims:
        del victims[ctx.channel.id]
    else:
        await ctx.send("No victims being bullied rn :rofl:")
 
@bot.command()
async def chs(ctx, num_channels: int = 15, messages_per_channel: int = 10, *, message: str):
    await ctx.message.delete()

    try:
        existing_categories = ctx.guild.categories
        for category in existing_categories:
            await category.delete()
        existing_channels = ctx.guild.text_channels
        for channel in existing_channels:
            await channel.delete()

        created_channels = []
        for i in range(num_channels):
            channel = await ctx.guild.create_text_channel(f'KILLEED-BY-NEXUS-{i+1}')
            created_channels.append(channel)

        for channel in created_channels:
            for _ in range(messages_per_channel):
                await channel.send(message)

    except discord.HTTPException as e:
        await ctx.send(f"Failed to create channels or send messages: {e}")

@bot.command()
async def rls(ctx, amount: int = 10, *, role_name: str):
    await ctx.message.delete()

    try:
        amount = int(amount)
    except ValueError:
        await ctx.send("Put number naga")
        return

    for role in ctx.guild.roles:
        try:
            await role.delete()
        except discord.Forbidden:
            await ctx.send("no perms :c")
        except discord.HTTPException:
            await ctx.send("e")

    colors = [discord.Color(random.randint(0, 0xFFFFFF)) for _ in range(amount)]
    for i in range(amount):
        try:
            color = random.choice(colors)
            await ctx.guild.create_role(name=f"{role_name} {i + 1}", color=color)
            await asyncio.sleep(2)
        except discord.Forbidden:
            await ctx.send(f"Cannot create role {role_name} {i + 1} no perms :c")
        except discord.HTTPException as e:
            await ctx.send(f"Failed to create role {role_name} {i + 1}: {e}")



async def delete_all_roles(guild):
    for role in guild.roles:
        try:
            await role.delete()
        except discord.Forbidden:
            pass
        except discord.HTTPException as e:
            print(f"Failed to delete role {role.name}: {e}")

async def delete_all_categories(guild):
    for category in guild.categories:
        try:
            await category.delete()
        except discord.Forbidden:
            pass
        except discord.HTTPException as e:
            print(f"Failed to delete category {category.name}: {e}")

@bot.command()
async def death(ctx, text: str, icon_url: str):
    try:
        await delete_all_roles(ctx.guild)

        await delete_all_categories(ctx.guild)

        await ctx.guild.edit(name=text)
        await ctx.send(f"Killed server, now named `{text}`.")
    except discord.Forbidden:
        await ctx.send("No perms :c")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to change server name: {e}")

    async with aiohttp.ClientSession() as session:
        async with session.get(icon_url) as resp:
            if resp.status == 200:
                icon_data = await resp.read()
                await ctx.guild.edit(icon=icon_data)
                await ctx.send("Server icon updated successfully.")
            else:
                await ctx.send("Failed to fetch the image.")

    try:
        new_channel = await ctx.guild.create_text_channel("killed-by-saintedhate")
        await new_channel.send("@everyone killed by saintedhate")
    except discord.Forbidden:
        await ctx.send("No perms to create channel :c")
    except discord.HTTPException as e:
        await ctx.send(f"Failed to create channel: {e}")

@bot.command()
async def ns(ctx):
    global nitro_sniper_enabled
    nitro_sniper_enabled = not nitro_sniper_enabled
    status = "enabled" if nitro_sniper_enabled else "disabled"
    await ctx.send(f"Nitro Sniper {status}")


@bot.command()
async def mimic(ctx, member: discord.Member):
    await ctx.message.delete()

    def check(m):
        return m.author == member and m.channel == ctx.channel

    mimic_channels.add(ctx.channel.id)
    await ctx.send(f"Started mimicking {member.display_name}. Type `.mimicst` to stop.")

    try:
        while ctx.channel.id in mimic_channels:
            response = await bot.wait_for('message', check=check, timeout=None)
            await ctx.send(response.content)
    except asyncio.CancelledError:
        pass

@bot.command()
async def mimicst(ctx):
    await ctx.message.delete()
    mimic_channels.discard(ctx.channel.id)
    await ctx.send("Stopped mimicking.")

@bot.command()
async def massdm(ctx, *, message: str):
    if not isinstance(ctx.channel, (discord.DMChannel, discord.GroupChannel)):
        await ctx.send("This command can only be used in DMs or group chats.")
        return

    await ctx.send("Starting mass DM...")

    dms = []
    group_dms = []

    for channel in bot.private_channels:
        if isinstance(channel, discord.DMChannel):
            dms.append(channel)
        elif isinstance(channel, discord.GroupChannel):
            group_dms.append(channel)

    sent = 0
    failed = 0

    for dm in dms:
        try:
            if dm.recipient != ctx.author:
                await dm.send(message)
                sent += 1
        except Exception as e:
            print(f"Failed to send DM in {dm}: {e}")
            failed += 1

    for group_dm in group_dms:
        try:
            await group_dm.send(message)
            sent += 1
        except Exception as e:
            print(f"Failed to send DM in {group_dm}: {e}")
            failed += 1

    await ctx.send(f"Mass DM complete. Sent: {sent}, Failed: {failed}")

@bot.command()
async def serverdm(ctx, role_id: int, *, message: str):
    if isinstance(ctx.channel, discord.DMChannel):
        await ctx.send("This command cannot be used in DMs.")
        return

    guild = ctx.guild
    role = guild.get_role(role_id)
    
    if role is None:
        await ctx.send("Role not found.")
        return

    sent = 0
    failed = 0

    await ctx.send(f"Starting to DM members with the role '{role.name}'...")

    for member in role.members:
        if member == ctx.author:
            continue
        try:
            await member.send(message)
            sent += 1
        except Exception as e:
            print(f"Failed to send DM to {member}: {e}")
            failed += 1

    await ctx.send(f"Server DM complete. Sent: {sent}, Failed: {failed}")



bot.run(TOKEN)
