import discord
from discord.ext import commands

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):
        em = discord.Embed(colour=0xf7931a)
        em.set_author(name="Crypto Manager Commands", icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png")
        em.add_field(name="Price Command", value="`>btc`, `>eth`, `>ltc` all return the price of the crypto, you can use the `>price <crypto>` to check any crypto.")
        em.add_field(name="Convert Command", value="`>convert <amount> <currency> <crypto>` converts a currency to a crypto or another currency")
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(Help(client))
