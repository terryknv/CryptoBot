import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ">")
client.remove_command("help")

@client.event
async def on_ready():
    print("{client.user} is online.")
    
@client.command()
async def ping(ctx):
    msg = await ctx.send("Pinging...")
    await msg.edit(content=f"Ping! `{round(client.latency * 1000)}ms`")

#client.load_extension(f'cogs.rep')

client.run(${{ secrets.DISCORD_TOKEN }})
