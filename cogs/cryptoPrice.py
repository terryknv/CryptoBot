import discord
from discord.ext import commands
import requests

class cryptoPrice(commands.Cog):
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
        
        #asigning 5 strings to each digit in the price of btc so I can add a comma between the 2nd and 3rd digit
        usd_rounded = str(round(usd))
        one,two,three,four,five=usd_rounded
        eur_rounded = str(round(eur))
        one1,two1,three1,four1,five1=eur_rounded
        gbp_rounded = str(round(gbp))
        one2,two2,three2,four2,five2=gbp_rounded
        
        em = discord.Embed(
            colour=0xf7931a,
            description=f"USD: `${one}{two},{three}{four}{five}`\n\nEUR: `€{one1}{two1},{three1}{four1}{five1}`\n\nGBP: `£{one2}{two2},{three2}{four2}{five2}`"
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
        
        usd_rounded = str(round(usd))
        one,two,three,four=usd_rounded
        eur_rounded = str(round(eur))
        one1,two1,three1,four1=eur_rounded
        gbp_rounded = str(round(gbp))
        one2,two2,three2,four2=gbp_rounded
        
        em = discord.Embed(
            colour=0x716b94,
            description=f"USD: `${one},{two}{three}{four}`\n\nEUR: `€{one1},{two1}{three1}{four1}`\n\nGBP: `£{one2},{two2}{three2}{four2}`"
        )
        em.set_author(
            name="Ethereum",
            icon_url="https://cdn.discordapp.com/attachments/271256875205525504/374282740218200064/2000px-Ethereum_logo.png",
        )
        await ctx.send(embed=em)

    @commands.command(aliases=["litecoin"])
    async def ltc(self, ctx):
      
        r = requests.get(
            "https://min-api.cryptocompare.com/data/price?fsym=LTC&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
                
        em = discord.Embed(
            colour=0xbebebe,
            description=f"USD: `${round(usd)}`\n\nEUR: `€{round(eur)}`\n\nGBP: `£{round(gbp)}`"
        )
        em.set_author(
            name="Litecoin",
            icon_url="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1c/Litecoin.svg/2500px-Litecoin.svg.png",
        )
        await ctx.send(embed=em)

    @commands.command(aliases=["cryptocurrency"])
    async def crypto(self, ctx, crypto):
      
        r = requests.get(
            f"https://min-api.cryptocompare.com/data/price?fsym={crypto.upper()}&tsyms=USD,EUR,GBP"
        )
        r = r.json()
        usd = r["USD"]
        eur = r["EUR"]
        gbp = r["GBP"]
                
        em = discord.Embed(
            colour=0xf7931a,
            description=f"USD: `${round(usd)}`\n\nEUR: `€{round(eur)}`\n\nGBP: `£{round(gbp)}`"
        )
        em.set_author(
            name=f"Price of {crypto.upper()}",
            icon_url="https://cdn.pixabay.com/photo/2013/12/08/12/12/bitcoin-225079_960_720.png",
        )
        await ctx.send(embed=em)

        
def setup(bot):
    bot.add_cog(cryptoPrice(bot))
