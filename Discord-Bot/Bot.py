# Starter code provided by: https://github.com/pattonsgirl/Fall2022-CEG3120/blob/main/Projects/Project1/bot.py

import os
import random
from datetime import datetime

import discord
from dotenv import load_dotenv

# Get token info
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# Set intents -- kinda dumb but whatevs
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
    # Seed so it tells different jokes on different instances
    random.seed(datetime.now)

@client.event
async def on_message(message):
    if message.author == client.user: # Don't recognize your own messages
        return

    # Message and image arrays
    joke_prompts = [
        'I heard two peanuts were walking down the street...',
        'If April showers bring May flowers, what do May flowers bring?',
        'What do you call a factory that makes okay products?',
        'What did the ocean say to the beach?'
    ]
    punchlines = [
        'One was a-salted.',
        'Pilgrims',
        'A satisfactory',
        'Nothing, it just waved'
    ]
    reaction_imgs = [
        'https://c.tenor.com/J9l-6hIfBXYAAAAC/my-honest-reaction-my-honest-reaction-meme.gif',
        'https://c.tenor.com/nON19NSBKXsAAAAC/my-honest-reaction.gif',
        'https://i.pinimg.com/564x/cd/88/ee/cd88ee0db9948b8247785502a75fe2f1.jpg',
        'https://c.tenor.com/D7krIUXuUAYAAAAd/my-honest-reaction-my-honest-reaction-meme.gif'

    ]

    if message.content == "!joke": # !joke- Send two messages: the joke prompt and the punchline via parallel arrays
        resp_id = random.randint(0, joke_prompts.__len__() - 1)
        # Send prompt
        response = joke_prompts[resp_id]
        await message.channel.send(response)
        # Send punchline
        response = punchlines[resp_id]
        await message.channel.send(response)

    if message.content == "!myreaction": # Get Rowdy's honest reaction
        react_id = random.randint(0, reaction_imgs.__len__() - 1)
        # Send image
        await message.channel.send(reaction_imgs[react_id])

    if message.content == "!help": # Print command info
        await message.channel.send("!joke -- I'll tell you a joke")
        await message.channel.send("!myreaction -- Get my honest reaction")
        await message.channel.send("!kill -- Close bot instance")


    if message.content == "!kill": # TESTING ONLY: close bot client (gives me console controls back)
        await message.channel.send("Bye bye!")
        await client.close()
    

client.run(TOKEN)