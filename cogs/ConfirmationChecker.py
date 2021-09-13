import discord
from discord.ext import commands
import requests
from blockcypher import get_transaction_details
import asyncio

class ConfirmationChecker(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def check(self, ctx, tid, confirms=1):

      try:
        dic = get_transaction_details(tid)
        bh = dic['confirmations']
      except (AssertionError):
        await ctx.send('Invalid transaction ID, please make sure it\'s correct.')
      if bh >= confirms:
        await ctx.send(f'That transaction has already reached {confirms} confirmation(s).')
      else:
        await ctx.send(f'{ctx.author.mention}, when that transaction reaches {confirms} confirmation(s), you will be pinged.')
        while True:
            await asyncio.sleep(5)
            dic1 = get_transaction_details(tid)
            bh1 = dic1['confirmations']
            await asyncio.sleep(5)
            if bh1 >= confirms:
                await ctx.send(f'{ctx.author.mention}, your transaction has reached {confirms} confirmation(s)')
                break
            else:
                continue
                
def setup(client):
    client.add_cog(ConfirmationChecker(client))
