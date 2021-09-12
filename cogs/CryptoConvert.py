import discord
from discord.ext import commands
import requests
from cogs.util.CurrencySymbols import CurrencySymbols

class CryptoConvert(commands.Cog):
    def __init__(self, client):
        self.client = client

        
    @commands.command()
    async def convert(self, ctx, amount, currency, crypto):

        valid_curr = list(CurrencySymbols.curr_list.keys())
        joiner = ', '
        is_valid = CurrencySymbols.is_valid_curr(currency.upper())
        ls = joiner.join(valid_curr)
        
        if is_valid == False:
            await ctx.send(f"Please convert from a currency from the valid list: {ls}")
            return

        r = requests.get(
            f"https://min-api.cryptocompare.com/data/price?fsym={crypto.upper()}&tsyms={currency.upper()}"
        )
        
        curr_symbol = CurrencySymbols.curr_list[currency.upper()]
        
        r = r.json()
        usd = r[currency.upper()]
        index = 1 / usd
        amounts = int(amount)
        converted = amounts * index        
        
        em = discord.Embed(colour = 0x0df20d, description=f"{curr_symbol}{amount} = {round(converted,10)} {crypto.upper()}")
        em.set_footer(text="Prices from Cryptocompare.com")
        em.set_author(
            name="Currency Conversion"
        )
        await ctx.send(embed=em)

        
def setup(bot):
    bot.add_cog(CryptoConvert(bot))
