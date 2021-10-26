#必要なライブラリのimport

import discord
from discord.ext import commands
import asyncio
import os
import subprocess
import ffmpeg
import threading
import time
import auth

#プレフィックスを"."としてボットとして動作させる
intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix='.',intents=intents)
voice_client = None

#起動時にログイン名とidを表示
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.command()
async def join(ctx):
    try:
        vc = ctx.author.voice.channel
        print('Connected to VC.')
        await vc.connect()
    except Exception as e:
        print(e)
        await ctx.send("ボイスチャンネルに入った上で実行してください！")

@client.command()
async def mute(ctx):
    try:
        vc_ids=ctx.author.voice.channel.voice_states.keys()
        print("Mute All")
        for id in vc_ids:
            try:
                m=ctx.guild.get_member(id)
                await m.edit(mute=True)
            except Exception as e:
                print(e)
    except Exception as e:
        print("#エラー:"+str(e))
        ctx.send("ボイスチャンネルに入った上で実行してください!")



@client.command()
async def unmute(ctx):
    try:
        vc_ids=ctx.author.voice.channel.voice_states.keys()
        print("Unmute All")
        for id in vc_ids:
            try:
                m=ctx.guild.get_member(id)
                await m.edit(mute=False)
            except Exception as e:
                print(e)
    except Exception as e:
        print("#エラー:"+str(e))
        ctx.send("ボイスチャンネルに入った上で実行してください!")

@client.command()
async def quit(ctx):
    print("Disconnect from VC.")
    try:
        await ctx.voice_client.disconnect()
    except Exception as e:
        pass

@client.command()
async def h(ctx):
    await ctx.send("使い方")
    await ctx.send(".joinでボイチャ参加")
    await ctx.send(".muteで全員ミュート")
    await ctx.send(".unmuteでミュート解除")
    await ctx.send("unmutemeで自分だけミュート解除")
    await ctx.send(".quitで終了")

@client.command()
async def unmuteme(ctx):
    try:
        await ctx.author.edit(mute=False)
    except Exception as e:
        pass

client.run(auth.token)