import discord
import asyncio

client = discord.Client()

@client.event
async def on_ready():
    print('loggend in as: ', client.user.name)
    print('ID: ',client.user.id)

@client.event
async def on_message(message):
    if message.content == ".salut":
        await client.send_message(message.channel,"hey!")

client.run("NDQ3NzQyNzg3NjgxNjQ4NjUw.DeMHjw.vtdZmKAJTglNvQyz2qxzHrfrBdE")
