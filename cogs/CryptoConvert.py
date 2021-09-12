import discord
from discord.ext import commands
import requests
from cogs.util.CurrencySymbols import CurrencySymbols

class CryptoConvert(commands.Cog):
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
        em = discord.Embed(colour = 0xf7931a, description=f"${amount} = {round(converted,10)} BTC")
        em.set_footer(text="Prices from Cryptocompare.com")
        em.set_author(
            name="Currency Conversion",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)

        
def setup(bot):
    bot.add_cog(CryptoConvert(bot))
