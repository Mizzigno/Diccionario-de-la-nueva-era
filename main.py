import random
import os
import requests
import discord
from discord.ext import commands

description = '''Un bot de ejemplo con varios comandos de utilidad.'''

intents = discord.Intents.default()
intents.members = True          # Actívalo también en el Developer Portal (Privileged Gateway Intents)
intents.message_content = True

# Un solo bot, con un solo prefijo
bot = commands.Bot(command_prefix='$', description=description, intents=intents)


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')


# ---------- Comandos del primer código ----------

@bot.command()
async def add(ctx, left: int, right: int):
    """Suma dos números."""
    await ctx.send(left + right)


@bot.command()
async def roll(ctx, dice: str):
    """Lanza dados en formato NdN."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('¡El formato debe ser NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)


@bot.command(description='Para cuando quieras decidir de otra forma')
async def choose(ctx, *choices: str):
    """Elige entre varias opciones."""
    await ctx.send(random.choice(choices))


@bot.command()
async def repeat(ctx, times: int, content='repeating...'):
    """Repite un mensaje varias veces."""
    for i in range(times):
        await ctx.send(content)


@bot.command()
async def joined(ctx, member: discord.Member):
    """Dice cuándo se unió un miembro."""
    await ctx.send(f'{member.name} joined {discord.utils.format_dt(member.joined_at)}')


@bot.group()
async def cool(ctx):
    """Dice si un usuario es cool."""
    if ctx.invoked_subcommand is None:
        await ctx.send(f'No, {ctx.subcommand_passed} no es cool')


@cool.command(name='bot')
async def _bot(ctx):
    """¿El bot es cool?"""
    await ctx.send('Yes, the bot is cool.')


# ---------- Comandos del segundo código ----------

@bot.command()
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')


@bot.command()
async def heh(ctx, count_heh=5):
    await ctx.send("he" * int(count_heh))


@bot.command()
async def kodland(ctx):
    for i in range(4):
        await ctx.send("HOLA PROFEE")
    await ctx.send("Buenas tardes :D")


@bot.command()
async def saludo(ctx):
    await ctx.send("Buenas tardes :D")

@bot.command()
async def mem(ctx):
    archivos = (os.listdir('images'))
    foto = random.choice(archivos)
    with open(f'images/{foto}', 'rb') as f:
        # ¡Vamos a almacenar el archivo de la biblioteca Discord convertido en esta variable!
        picture = discord.File(f)
    # A continuación, podemos enviar este archivo como parámetro.
    await ctx.send(file=picture)
def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

