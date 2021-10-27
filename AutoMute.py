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
async def show(ctx):
    try:
        msg=await ctx.send("下のボタンでミュート、ミュート解除ができます！")
        await msg.add_reaction("🎤")
        await msg.add_reaction("❌")
    except Exception as e:
        print(e)
        await ctx.send("エラーが発生しました。もう一度お試しください。")

#リアクションで操作を行えるようにする
@client.event
async def on_reaction_add(reaction, user):
    if user.bot:
        return
    if reaction.message.author.bot != 1:
        return
    try:
        #リアクションを付けたユーザーを探す
        reaction_ids=await reaction.users().flatten()
        user=None
        for users in reaction_ids:
            if users.bot != 1:
                user=users
        #ミュート解除
        vc_ids=user.voice.channel.voice_states.keys()
        if reaction.emoji == "🎤":
            for id in vc_ids:
                m=reaction.message.guild.get_member(id)
                await m.edit(mute=False)
        #ミュート
        if reaction.emoji =="❌":
            for id in vc_ids:
                m=reaction.message.guild.get_member(id)
                await m.edit(mute=True)
    except Exception as e:
        print("#エラー:"+str(e))
        await reaction.message.channel.send("エラーが発生した可能性があります、もし失敗していたらもう一度お試しください。")
    #リアクションを何度も実行できるように、リアクションを削除する必要がある
    try:
        reaction_idss=await reaction.users().flatten()
        for users in reaction_ids:
            if users.bot != 1:
                await reaction.remove(users)
    except Exception as e:
        print("エラー:"+str(e))


@client.command()
async def h(ctx):
    await ctx.send("使い方")
    await ctx.send(".showで操作画面を表示できます。(joinは必要ありません。)")
    await ctx.send("リアクション操作でミュート・ミュート解除が行えます")

@client.command()
async def upd(ctx):
    await ctx.send("2021/10/28 Update")
    await ctx.send("・ボイチャにいちいち参加させなくてもミュート可能になりました。")
    await ctx.send("・リアクションを使ってボタンで操作できるようになりました。")

@client.command()
async def unmuteme(ctx):
    try:
        await ctx.author.edit(mute=False)
    except Exception as e:
        pass

client.run(auth.token)