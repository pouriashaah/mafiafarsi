import discord
import asyncio
import responses
from discord.ext import commands

intents = discord.Intents.all()
TOKEN = 'ljCS2P2lt6d-nbgDtnZy3vZmg'
bot = commands.Bot(command_prefix = "!",intents=intents)

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    @bot.event
    async def on_ready():
        print("bot is ready !")

    @bot.event
    async def on_disconnect():
        print("bot is off !")

    @bot.event
    async def on_message(m):
        username = str(m.author)
        user_message = str(m.content)
        channel = str(m.channel)
        print(channel)
        # if user_message[0] == '?':
        #     user_message = user_message[1:]
        if channel:
            await send_message(m, user_message, is_private=False)
        else:
            await send_message(m, user_message, is_private=True)
    bot.run(TOKEN)
























# import responses

# async def send_message(message, user_message):
#     try:
#         print(message)
#         response = responses.handle_response(user_message)
#         # await message.author.send(response)
#         # if is_private else 
#         await message.channel.send(response)
#     except Exception as e:
#         print(e)


# 
#     TOKEN = 'MTAyMjIyMjM5NTMyNDUxODQ2MA.GPeiPL.nZ2ZfDWXMkIZIljCS2P2lt6d-nbgDtnZy3vZmg'
#     client = discord.Client(intents=discord.Intents.default())

#     @client.event
#     async def on_ready():
#         print(f'{client.user} is no running!')


#     @client.event
#     async def on_message(message):
#         # if message.author == client.user:
#         #     return

#         username = str(message.author)
#         user_message = str(message.content)
#         channel = str(message.channel)

#         print(f"{username} said: '{user_message}' ({channel})")

#         # if user_message[0] == '?':
#         #     print("ok")
#         #     user_message = user_message[1:]
#         await send_message(message, user_message)
#         # else:
#         #     await send_message(message, user_message, is_private=False)


#     client.run(TOKEN)