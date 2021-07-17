from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)


@bot.command()
async def ping(ctx):
    await ctx.send('peng')

@bot.event
async def on_message(message):
    if message.author.voice is None:
        await message.channel.send("あなたはボイチャにいませんで")
        return
    
    await message.author.voice.channel.connect()
    await message.channel.send("接続しました")

bot.run(token)
