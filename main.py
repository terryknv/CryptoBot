import discord
from discord.ext import commands
from cryptography.fernet import Fernet
import time

client = commands.Bot(command_prefix = ">")
client.remove_command("help")

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

@client.event
async def on_ready():
    print("{client.user} is online.")
    
@client.command()
async def ping(ctx):
    msg = await ctx.send("Pinging...")
    time.sleep(0.5)
    await msg.edit(content=f"Ping! `{round(client.latency * 1000)}ms`")
    
client.load_extension(f'cogs.CryptoPrice')
client.load_extension(f'cogs.Help')
client.load_extension(f'cogs.ConfirmationChecker')
client.load_extension(f'cogs.CryptoConvert')

passw = 'gAAAAABhqxhNDzKk8oFHgcS7TfjorI8xZklMe1BKnhCJONhzmL3dQ3iWjbyVVzDKKYnmVrinPU9wMBIXa-e3n_7vRWjljSJquKqogAo39sVMbSD0qHJv6YtSVX9t99BMLkGPzj_h0QlNRnK0xvHKjRf_xSNm_cRDpQ=='
passwd = fer.decrypt(passw.encode()).decode()
#22
client.run(passwd)
