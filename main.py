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
    time.sleep(1)
    await msg.edit(content=f"Ping! `{round(client.latency * 1000)}ms`")
    
client.load_extension(f'cogs.cryptoPrice')
client.load_extension(f'cogs.cryptoConvert')

passw = 'gAAAAABhPSJIdDJOL_DREp4XAlxrJinJjukXaXyYyV1q3vy5Rs0hFZh3YHUqIJoXG-Kw83V_ZUp8VFhG5eh4ReyVCadyP3N1PkqYh4I03wPMfyYwFKhC1iFt7FMMkdj1f2ZWPDMlzkdj80gG1kWcbgp32GJ_YvyWmQ=='
passwd = fer.decrypt(passw.encode()).decode()

client.run(passwd)
