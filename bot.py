#!/usr/bin/env python3

import math
import discord
import re
import conf
from decimal import Decimal

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('smp-role-bot Copyright (C) 2023 virgildoesthings \nThis program comes with ABSOLUTELY NO WARRANTY; for details see ./LICENSE \nThis is free software, and you are welcome to redistribute it \nunder certain conditions; for details see ./LICENSE')
    print('-----')
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


@client.event
async def on_message(message):
	
    if message.content.find('!') == 0 and discord.Message.channel.id == conf.channel:
        if message.content.find("smp") != -1 and message.content.find("smp") < message.content.find('!'):
            await add_roles(conf.role)
            await message.channel.send("SMP Member role granted.")

client.run(conf.key)
