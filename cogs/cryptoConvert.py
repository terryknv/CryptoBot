import discord
from discord.ext import commands
import requests

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

        
    @commands.command(aliases=["usdtobtc", "usd2btc"])
    async def usdbtc(self, ctx, message):

        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD"
        )

        r = r.json()
        usd = r["USD"]
        index = 1 / usd
        amount = int(message)
        converted = amount * index
        em = discord.Embed(description=f"**${amount}** = **{converted} BTC**")
        em.set_author(
            name="Currency Conversion",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)
