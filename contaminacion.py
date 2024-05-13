import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    
@bot.command()
async def mina(ctx):
    await ctx.send(f'Hola, soy un bot de la contaminación 🪷, mi nombre es {bot.user} ')
    
@bot.command()
async def contaminacion(ctx):
    num = random.randint(1,3)
    await ctx.send('Sus efectos son perjudiciales para la salud, biodiversidad y los ecosistemas, además de contribuir al cambio climático y otros problemas ambientales')
    if num == 1:
        with open('img/agua.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif num == 2:
        with open('img/aire.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif num == 3:
        with open('img/tierra.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    
@bot.command()
async def plastico(ctx):
    numero = random.randint(1,4)
    if numero == 1:
        await ctx.send('Tarda hasta 450 años en desintegrarse')
    elif numero == 2:
        await ctx.send('Se tiran un millón de botellas de plástico por minuto')
        with open('img/botellas.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif numero == 3:
        await ctx.send('Existe varias islas de contaminación plástica, una de ellas está flotando en el Océano Pacífico, con 1.6 millones de km2 y unas 80,000 toneladas de plástico.')
        with open('img/isla.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)
    elif numero == 4:    
        await ctx.send('Más de 2144 especies marinas mueren asfixiadas o por ingerirlos')
        with open('img/marino.jpg', 'rb') as f:
            picture = discord.File(f)
        await ctx.send(file=picture)

@bot.command()
async def agua(ctx):
    nume = random.randint(1,3)
    if nume == 1:
        await ctx.send('Más de 5 millones de personas mueren cada año por beber agua contaminada')
        with open('img/aguac.jpg', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
    if nume == 2:
        await ctx.send('Casi 2 billones de personas en el planeta no tienen acceso al agua potable')
        with open('img/nopotable.jpg', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
    if nume == 3:
        await ctx.send('Las enfermedades provocadas por el agua contaminada han matado a más seres humanos que cualquier guerra')
        with open('img/niñ.jpg', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
        
@bot.command()
async def suelo(ctx):
    numer = random.randint(1,3)
    if numer == 1:
        await ctx.send('La contaminación del suelo puede hacer que los terrenos se vuelvan estériles')
        with open('img/suelo.jpg', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
    elif numer == 2:
        await ctx.send('13 millones de personas pierden la vida por vivir o trabajar en ambientes poco saludables')
    elif numer == 3:
        await ctx.send('Los grupos de población más afectados son los adultos y niños')
    
@bot.command()
async def aire(ctx):
    nur = random.randint(1,2)
    if nur == 1:
        await ctx.send('Nueve de cada 10 personas respiran aire contaminado')
        with open('img/resaire.jpg', 'rb') as f:
                picture = discord.File(f)
        await ctx.send(file=picture)
    elif nur == 2:
        await ctx.send('Puede contener particulas microscopicas de diferentes materiales perjudiciales, tan pequeños que pueden penetrar los pulmones y llegar al torrente sanguineo')
    
@bot.command()
async def comandos(ctx):
    await ctx.send('!mina')
    await ctx.send('!contaminacion')
    await ctx.send('!plastico')
    await ctx.send('!agua')
    await ctx.send('!suelo')
    await ctx.send('!aire')
