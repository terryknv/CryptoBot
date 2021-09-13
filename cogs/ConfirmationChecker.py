import discord
from discord.ext import commands
import requests
from blockcypher import get_transaction_details

class ConfirmationChecker(commands.Cog):
    def __init__(self, client):
        self.client = client
        
    @commands.command()
    async def check(self, ctx, tid, confirms=1):

      dic = get_transaction_details(tid)

      bh = dic['confirmations']
      
        
        
        
        
def setup(client):
    client.add_cog(ConfirmationChecker(client))
