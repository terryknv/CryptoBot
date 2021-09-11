import discord
from discord.ext import commands
import requests

class crypto(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["bitcoin"])
    async def btc(self, ctx):

        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
        em = discord.Embed(
            colour=0xf7931a,
            description=f"USD: `${str(round(usd))}`\n\nEUR: `€{str(round(eur))}`\n\nGBP: `£{str(round(gbp))}`"
        )
        em.set_author(
            name="Bitcoin",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)

    @commands.command(aliases=["ethereum"])
    async def eth(self, ctx):
      
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
        em = discord.Embed(
            colour=0x716b94,
            description=f"USD: `${str(round(usd))}`\n\nEUR: `€{str(round(eur))}`\n\nGBP: `£{str(round(gbp))}`"
        )
        em.set_author(
            name="Ethereum",
            icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
        )
        await ctx.send(embed=em)

def setup(bot):
    bot.add_cog(cryptoprice(bot))
