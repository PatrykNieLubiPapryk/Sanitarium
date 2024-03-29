import discord, random, os, requests
from discord.ext import commands
from bot_logic import gen_pass, flip_coin, gen_emodji, roll_dice, RNG

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'Zalogowaliśmy się jako {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Cześć, jestem bot{bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def flipcoin(ctx):
    await ctx.send("Rzucam monętą. Wynik: " + flip_coin())

@bot.command()
async def emoji(ctx):
    await ctx.send(str(gen_emodji()))

@bot.command()
async def genpass(ctx, pwd_length = 10):
    await ctx.send("Generuję hasło o długości " + str(pwd_length) + ": " + gen_pass(pwd_length))

@bot.command()
async def bye(ctx):
    await ctx.send("Żegnaj! " + "\U0001f642")
    
@bot.command()
async def rolldice(ctx):
    await ctx.send("Rzucam kostką do gry. Wynik: "+ roll_dice())

@bot.command()
async def rng(ctx, lower = 0, upper = 1000000):
    await ctx.send("Generuję losową liczbę od " + str(lower) + " do " + str(upper) + ". Wynik: " + str(RNG(int(lower), int(upper))))

@bot.command()
async def add(ctx, left = 9, right = 10):
    await ctx.send(int(left) + int(right))

@bot.command()
async def mem(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command()
async def zmem(ctx):
    img_name = random.choice(os.listdir('animals'))
    with open(f'animals/{img_name}', 'rb') as f:
            picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('duck')
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

def get_dog_image_url():    
    url = 'https://random.dog/woof.json'
    res = requests.get(url)
    data = res.json()
    return data['url']
@bot.command('dog')
async def dog(ctx):
    image_url = get_dog_image_url()
    await ctx.send(image_url)

bot.run("TOKEN")
