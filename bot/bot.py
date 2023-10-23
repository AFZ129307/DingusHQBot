import discord
import responses

async def send_message(message, user_message, is_private):
    response = responses.handle_response(user_message)
    if is_private:
        await message.author.send(response)
    else:
        await message.channel.send(response)

def run_discord_bot():
    TOKEN = 'MTEzNDg5NzQxNTc2MjIyNzM4MA.G5REfj.TxQ2H7VgXcDXSC2CHQw7vZv_udn99kluGGYmTM'
    responses.create_response_table()
    Intents = discord.Intents.default()
    Intents.message_content=True

    client = discord.Client(intents=Intents)
    @client.event
    

    async def on_ready():
        print(f'{client.user} is now running!')


    @client.event
    async def on_message(message):
        # Avoid bot responding to itself
        if message.author == client.user:
            return
        
        user = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{user} said: '{user_message}' ({channel})")

        await send_message(message, user_message, is_private=False)

    client.run(TOKEN)