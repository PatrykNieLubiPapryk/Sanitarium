import discord, random, os, requests
from discord.ext import commands
from ecobot_logic import degradation_time

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem {bot.user}! Jestem czatbotem próbującym edukować o ekologii i środowisku.')

@bot.command()
async def rozpad(ctx):
    await ctx.send(degradation_time())

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def tips(ctx):
    await ctx.send("Jak dbać o przyrodę? Oszczędzaj energię i wodę, segreguj śmieci, szanuj zwierzęta, nie śmieć, zrezygnuj z jednorazowych opakowań, zmień dietę.")

@bot.command()
async def zielony(ctx):
    await ctx.send("Do zielonego worka wrzucamy szkło.")

@bot.command()
async def niebieski(ctx):
    await ctx.send("Do niebieskiego worka wrzucamy papier.")

@bot.command()
async def zolty(ctx):
    await ctx.send("Do żółtego worka wrzucamy metale i tworzywa sztuczne.")

@bot.command()
async def szary(ctx):
    await ctx.send("Do szarego worka wrzucamy odpady zmieszane.")

@bot.command()
async def brazowy(ctx):
    await ctx.send("Do brązowego worka wrzucamy bioodpady.")

bot.run("TOKEN")