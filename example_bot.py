'''
    Run with:
        python example_bot.py TARGET_TOKEN
        MTA4NDY0NDMxMTU4NjU5MDc1MA.GclbDX.xe-a_Z3JemjmBCvHWFj6AxHZgvSXuPD-1HF_sU
'''

import sys
import discord

client = discord.Client(intents=discord.Intents.all())

@client.event
async def on_ready():
    print('Ready')

@client.event
async def on_message(message):
    if message.content == 'ping?':
        print('Replying')
        await message.channel.send('pong!')
    
    if message.content == 'hello':
        await message.channel.send('world!')

client.run(sys.argv[1])
