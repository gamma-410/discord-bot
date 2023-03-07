import discord
import requests


TOKEN = 'トークンをここへ'
client = discord.Client()


@client.event
async def on_ready():
    print('ログインしました!')


@client.event
async def on_message(message):

    if message.content == '/test':
        await message.channel.send('Bot: テストコードを受信しました。')


    if message.content == '/hello':
        await message.channel.send('Hello!')

    # 挨拶
    if message.content == 'こんにちは':
        await message.channel.send('こんにちは！')
    
    if message.content == 'おはよう':
        await message.channel.send('おはよう！')
    
    if message.content == 'おやすみ':
        await message.channel.send('おやすみ！')
        
    if message.content == 'こんばんは':
        await message.channel.send('こんばんは！')
    
    if message.content == 'ありがとう':
        await message.channel.send('いえいえ！')
        
        
client.run(TOKEN)
