import discord
import asyncio
import safygiphy


g = safygiphy.Giphy()
client = discord.Client()

@client.event
async def on_ready():
    print('loggend in as: ', client.user.name)
    print('ID: ',client.user.id)

@client.event
async def on_message(message):
    print(message.content)
    if message.content.startswith(".gif"):
        r = g.random(tag=message.content[5:])
        await client.send_message(message.channel,str(r['data']['url']))
    elif message.content == "woedy":
        await client.send_message(message.channel,"Il est pas la le con")
        
        
        
    

client.run("NDQ3NzQyNzg3NjgxNjQ4NjUw.DeMHjw.vtdZmKAJTglNvQyz2qxzHrfrBdE")
