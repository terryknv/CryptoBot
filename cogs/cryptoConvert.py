import discord
from discord.ext import commands
import requests

class cryptoConvert(commands.Cog):
    def __init__(self, client):
        self.client = client

        
    @commands.command()
    async def convert(self, ctx, amount, currency, crypto):

        r = requests.get(
            f"https://min-api.cryptocompare.com/data/price?fsym={crypto.upper()}&tsyms={currency.upper()}"
        )

        r = r.json()
        usd = r[currency.upper()]
        index = 1 / usd
        amounts = int(amount)
        converted = amounts * index
        em = discord.Embed(description=f"${amount} = {round(converted,10)} BTC")
        em.set_author(
            name="Currency Conversion",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)

        
def setup(bot):
    bot.add_cog(cryptoConvert(bot))
