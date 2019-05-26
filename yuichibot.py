#Andrew Seak
#5/4/2019
#Personal project for discord
#5/11/2019
#   Finished quote commands

import discord
import os
import quotes
from datetime import datetime
#from discord import Game

print("yo")

client = discord.Client()
prefix = "<@573955133256368141>"

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    activity = discord.Activity(type=discord.ActivityType.watching, name = "Troy Yang")
    await client.change_presence(activity=activity)

@client.event
async def on_message(message):
    if not message.author.bot:

        if message.author == client.user:
            return

        if message.channel == message.author.dm_channel:
            return

        if message.content == (prefix):
            await message.channel.send("sup")
        elif message.content == (prefix+' hello'):
            await message.channel.send('Hello!')
        #############
        ###Utility###
        #############
        elif message.content == (prefix+' me'):
            await message.channel.send(message.author.mention)
        elif message.content == (prefix+ ' serverid'):
            await message.channel.send(message.guild.id)
        elif message.content == (prefix+' channelid'):
            await message.channel.send(message.channel.id)
        elif message.content.startswith(prefix+' url'):
            e = discord.Embed()
            e.set_image(url=message.mentions[0].avatar_url_as(format="png", size=1024))
            await message.channel.send(embed=e)
        ############
        ###Quotes###
        ############
        elif message.content == (prefix+' quote'):
            guildId = str(message.guild.id)
            path = "quotes/"+guildId+".json"
            if os.path.isfile(path):
                quote = quotes.randomquote(path)
                if not quote == None:
                    await message.channel.send(quote["quote"])
            else:
                await message.channel.send("There are no quotes.")
        elif message.content.startswith(prefix+' quote add '):
            guildId = str(message.guild.id)
            path = "quotes/"+guildId+".json"
            if os.path.isfile(path):
                print(message.guild.name + ": quotes/"+guildId+".json exists")
                print(message.guild.name + ": added quote " + message.content[len(prefix+' quote add '):])
                quote = quotes.addquote(path, message.content[len(prefix+' quote add '):], "Created " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " by " + message.author.mention + " in " + message.channel.mention)
                await message.channel.send("Added as quote " + str(quote))
            else:
                file = quotes.newfile("quotes/", guildId)
                print(message.guild.name + ": created " + file.name)
                print(message.guild.name + ": added quote " + message.content[len(prefix+' quote add '):])
                quote = quotes.addquote(path, message.content[len(prefix+' quote add '):], "Created " + str(datetime.now().strftime('%Y-%m-%d %H:%M:%S')) + " by " + message.author.mention + " in " + message.channel.mention)
                await message.channel.send("Added as quote " + str(quote))
        elif message.content.startswith(prefix+' quote '):
                guildId = str(message.guild.id)
                path = "quotes/"+guildId+".json"
                if os.path.isfile(path):
                    try:
                        index = int(message.content[len(prefix+' quote '):]) - 1
                        quote = quotes.getquote(path, index)
                        await message.channel.send(quote["quote"])
                    except:
                        await message.channel.send("There was an error dumb ass")
                else:
                    await message.channel.send("There are no quotes on this server.")
        elif message.content.startswith(prefix+' quote remove '):
                guildId = str(message.guild.id)
                path = "quotes/"+guildId+".json"
                if os.path.isfile(path):
                    #try:
                        index = int(message.content[len(prefix+' quote remove '):]) - 1
                        print(message.guild.name + ": removed quote " + str(index))
                        quote = quotes.delquote(path, index)
                        await message.channel.send("Removed quote " + str(quote+1))
                    #except:
                        #await message.channel.send("There was an error dumb ass")
                else:
                    await message.channel.send("There are no quotes in this server. Use the command `@" + client.user.name + " quote add <quote>` to add some.")
        elif message.content.startswith(prefix+ ' quotes'):
            guildId = str(message.guild.id)
            path = "quotes/"+guildId+".json"
            userDM = message.author.dm_channel
            if userDM == None:
                await message.author.create_dm()
                userDM = message.author.dm_channel
            if os.path.isfile(path):
                allquotes = quotes.getquotes(path)
                list = "There are " + str(len(allquotes)) + " quotes with " + str(quotes.getnumberremoved(path)) + " removed quotes\n"
                for i in range(len(allquotes)):
                    listConcat = ""
                    if allquotes[i] == None:
                        listConcat = "Quote " + str(i+1) + " no longer exists.\n\n"
                    else:
                        listConcat = "Quote " + str(i+1) + ": " + allquotes[i]["quote"] + "\n" + listConcat + allquotes[i]["desc"] + "\n\n"
                    list += listConcat
                    if (len(list) + len(listConcat) >= 2000):
                        await userDM.send(list)
                        list = ""
                    if (i == len(allquotes) - 1):
                        await userDM.send(list)
                await message.channel.send("Quotes sent to DM")
            else:
                await message.channel.send("There are no quotes")

client.run("token")
