#!/usr/bin/env python3
#https://github.com/mulveyben1/factorial-bot

import math
import discord
import re
import conf
from decimal import Decimal

client = discord.Client(intents=discord.Intents.all())
#https://github.com/mulveyben1/factorial-bot

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('-----')


@client.event
async def on_message(message):
	
    if message.content.find('!') != -1 and message.content[message.content.find('!') - 1] != "@":  # Print source code
        # link
        if message.content.find("src") != -1 and message.content.find("src") < message.content.find('!'):
            await message.channel.send("Unfortunately, this project can no longer be found on Github.")
            await message.channel.send("Ping Virgil if you want the source code.")

        elif message.content.find("source") != -1 and message.content.find("source") < message.content.find('!'):  #
            # Print source code link
            await message.channel.send("Unfortunately, this project can no longer be found on Github.")
            await message.channel.send("Ping Virgil if you want the source code.")

        elif message.content.find('!') == 0:  # ! is typically used for commands when in the 0 index of a message
            print("Not a factorial.")

        elif str(message.author) == "DJ Mitch#4397":  # That bot will never have factorials,ignore it
            print("Not a factorial.")
            
        elif message.content.find("image") != -1 and message.content.find("image") < message.content.find('!'):
            await message.channel.send("https://instrumental-tracking-others-pill.trycloudflare.com/140800ed-b8ac-4b32-a86f-57ea2071a30b")
		


        else:
            numberpre = None
            try:  # Check if there's actually a factorial
                numberpre = re.search(r'-?\d+!', message.content).group()
            except:
                print("Not a factorial.")

            if numberpre is None:  # Should never run
                pass
            else:
                number = int(numberpre[:len(numberpre) - 1])
                if message.content.find('-') != -1:  # Handling negative #s
                    await message.channel.send("You can't take the factorial of a negative number!")
                    print("Sent by: " + str(message.author) + " with content: " + str(message.content))

                elif number >= 1000000:  # Handling #s that are way too big (give up)
                    await message.channel.send("I can't calculate this without setting Virgil's server on fire!")
                    print("Sent by: " + str(message.author) + " with content: " + str(message.content))

                elif number > 60000:  # Handling large #s (might take a while to compute)
                    await message.channel.send("That's a big number. Give me a second.")
                    numberFac = math.factorial(number)
                    numberFac = "{:.5E}".format(Decimal(numberFac))
                    await message.channel.send(numberFac)
                    print("Sent by: " + str(message.author) + " with content: " + str(message.content))

                elif number > 15:  # Keep messages short, use scientific notation
                    numberFac = math.factorial(number)
                    numberFac = "{:.5E}".format(Decimal(numberFac))
                    await message.channel.send(numberFac)
                    print("Sent by: " + str(message.author) + " with content: " + str(message.content))

                else:  # Just the factorial
                    numberFac = math.factorial(number)
                    await message.channel.send(numberFac)
                    print("Sent by: " + str(message.author) + " with content: " + str(message.content))


client.run(conf.key)
