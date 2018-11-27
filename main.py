import discord
import asyncio
import safygiphy
from discord.ext import commands



voice = await message.author.voice.channel.connect()

g = safygiphy.Giphy()
client = discord.Client()



@bot.command(pass_context=True)
async def brent(ctx):
    voice_channel = ctx.message.author.voice.voice_channel
    await bot.join_voice_channel(voice_channel)


@client.event
async def on_ready():
    print('loggend in as: ', client.user.name)
    print('ID: ',client.user.id)

@client.event
async def on_message(message):
    print(message.content)
    if message.content.startswith(".gif"):
        r = g.random(tag=message.content[5:])
        voice.play(discord.FFmpegPCMAudio('./res/rick_roll.mp3'))                        
        await client.send_message(message.channel,str(r['data']['url']))
    elif message.content == "woedy":
        await client.send_message(message.channel,"Il est pas la le con")
   
        
        
        
    

client.run("NTE2MzQwMjMxNTA3NjczMDg4.DtyZpA.-yrGE-j4yFGslxl6x5p-W0orjeI")
