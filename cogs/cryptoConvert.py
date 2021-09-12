import discord
from discord.ext import commands
import requests

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

        
