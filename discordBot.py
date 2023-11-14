import discord, os, requests
from discord.ext import commands
TOKEN = ''

intents = discord.Intents().all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix='-',intents=intents)

@client.event
async def on_ready():
    print('Bot started')

@bot.command(name="get")
async def getUrl(ctx):
    print('Uploading image to server')
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open('./camera_image.png', 'rb')},
        data={'size': 'auto'},
        headers={'X-Api-Key': 'ZujcDVvQxtcd6wL6E5RVKd3D'},
    )
    if response.status_code == requests.codes.ok:
        with open('no-bg.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
    
    await ctx.channel.send(file=discord.File('no-bg.png'))

bot.run(TOKEN)