import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)
@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')
@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')
@bot.command()
async def plastik_el_isi(ctx):
    fikirler = [
        "Plastik şişelerden kalemlik yapabilirsin.Plastik kalemlik için plastik şişeyi renkli kalemlerle boya",
        "Plastik kapakları kullanarak mozaik tablo yapabilirsin.",
        "Eski plastik kutulardan küçük saksIlar yapabilirsin.Bunu yapmak için plastik şişenin içine toprak koy sonra çiçek ek.Not:sulamayI unutma",
        "Plastik kaşıkları boyayıp dekoratif çerçeve tasarlayabilirsin."
        "plastik şişelerden telofon yapabilirsin iki şişe gerekli.İlk olarak plastiği altını del ve ip ğeçir aynısını diğer şişede yap "
    ]
    await ctx.send(f"Evde yapabileceğin plastik el işleri:\n- " + "\n- ".join(fikirler))

bot.run("")
