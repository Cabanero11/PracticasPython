import discord
from discord.ext import commands

# Reemplaza 'YOUR_BOT_TOKEN' con el token de tu bot
TOKEN = 'YOUR_BOT_TOKEN'

# Configuración del bot
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='!', intents=intents)

# Evento cuando el bot está listo
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

# Comando para saludar
@bot.command(name='hola')
async def hola(ctx):
    await ctx.send('¡Hola, amigo!')

# Iniciar el bot
bot.run(TOKEN)