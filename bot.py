import discord
import asyncio
import responses
from discord.ext import commands

intents = discord.Intents.all()
TOKEN = 'MTAyMjI2MTM5NDg0MzkxMDE2NA.G8u-C5.sdeczN0ctCSRG0DwsGGGquLPPrJOspvS9EUS28'
bot = commands.Bot(command_prefix = "?",intents=intents)
activity = discord.Game(name="!help")




async def send_message(message, user_message, is_private):

        if isinstance(message.channel, discord.channel.DMChannel):
            try:
                response = responses.handle_response(user_message)
                await message.author.send(response) if is_private else await message.channel.send(response)
            except Exception as e:
                print(e)
                pass
        elif(message.channel.name == 'mafia'):
            try:
                    response = responses.handle_response(user_message)
                    await message.author.send(response) if is_private else await message.channel.send(response)
            except Exception as e:
                print(e)
                pass
        else:
            return



def run_discord_bot():
    @bot.event
    async def on_ready():
        await bot.change_presence(status=discord.Status.idle, activity=activity)
        for guild in bot.guilds:
            if 'Mafia' not in [role.name for role in guild.roles]:
                await guild.create_role(name='Mafia')
            role = discord.utils.get(guild.roles, name='Mafia')
            found = []
            for channel in guild.channels:
                if channel.name == 'mafia' or channel.name == 'Mafia':
                    found.append(channel.type)
            if discord.ChannelType.text not in found:
                await guild.create_text_channel('mafia')
            if discord.ChannelType.voice not in found:
                await guild.create_voice_channel('Mafia')
            for channel in guild.channels:
                if channel.name == 'mafia' or channel.name == 'Mafia':
                    await channel.set_permissions(guild.default_role, read_messages = False)
                    await channel.set_permissions(role, read_messages = True)
        print("bot is ready !")

    @bot.event
    async def on_disconnect():
        print("bot is off !")

    @bot.event
    async def on_message(m):
        bot_name = "amirtestingthis#9523"
        username = str(m.author)
        user_message = str(m.content)
        channel = str(m.channel)
        print(channel)
        # if user_message[0] == '?':
        #     user_message = user_message[1:]
        if username!=bot_name:
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