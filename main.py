import discord
import asyncio
token = os.environ['TOKEN']
client = discord.Client()

@client.event
async def on_ready():
    print('loggend in as: ', client.user.name)
    print('ID: ',client.user.id)

@client.event
async def on_message(message):
    if message.content == ".salut":
        await client.send_message(message.channel,"hey!")

client.run(token)
