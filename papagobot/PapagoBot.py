#This code and description is written by Hoplin
#This code is written with API version 1.0.0(Rewirte-V)
#No matter to use it as non-commercial.
#Papago API Reference : https://developers.naver.com/docs/nmt/reference/

import discord
import yaml
from asyncio import *
from discord.ext import commands
from urllib.error import HTTPError, URLError
from papagoRequestClass import dataProcessStream

with open('config.yml') as f:
    keys = yaml.load(f, Loader=yaml.FullLoader)

###############################################################
#discord bot tokken
token = keys['Keys']['discordAPIToken']
#Naver Open API application ID
client_id = keys['Keys']['client_id']
#Naver Open API application token
client_secret = keys['Keys']['client_secret']
# stream Instane
streamInstance = dataProcessStream(client_id,client_secret)
###############################################################

client = discord.Client()
@client.event # Use these decorator to register an event.
async def on_ready(): # on_ready() event : when the bot has finised logging in and setting things up
    await client.change_presence(status=discord.Status.online, activity=discord.Game("Tokimeki Memorial"))
    print("New log in as {0.user}".format(client))

@client.event
async def on_message(message): # on_message() event : when the bot has recieved a message
    def sendmsg(resultPackage) -> discord.Embed:
        if resultPackage['status']["code"] < 300:
            embed = discord.Embed(title=f"{resultPackage['data']['ntl']['name']} -> {resultPackage['data']['tl']['name']}",description="", color=0x5CD1E5)
            embed.add_field(name=f"{resultPackage['data']['ntl']['text']}", value=resultPackage['data']['tl']['text'],inline=False)
            return embed
        else:
            embed = discord.Embed(title="Error Code", description=resultPackage['status']['code'],color=0x5CD1E5)
            return embed

    #To user who sent message
    # await message.author.send(msg)
    print(message.content)
    if message.author == client.user:
        return
    if message.content.startswith("!ke"):
        #띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) != 1:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send(embed=embedInstance)
        except HTTPError as e:
            await message.channel.send(f"Translate Failed. HTTPError Occured : {e}")

    if message.content.startswith("!ek"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) != 1:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send(embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!kj"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) != 1:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send(embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

    if message.content.startswith("!jk"):
        baseurl = "https://openapi.naver.com/v1/papago/n2mt"
        # 띄어쓰기 : split처리후 [1:]을 for문으로 붙인다.
        trsText = message.content.split(" ")
        try:
            if len(trsText) != 1:
                resultPackage = streamInstance.returnQuery(trsText)
                embedInstance = sendmsg(resultPackage)
                await message.channel.send(embed=embedInstance)
        except HTTPError as e:
            await message.channel.send("Translate Failed. HTTPError Occured.")

client.run(token)
