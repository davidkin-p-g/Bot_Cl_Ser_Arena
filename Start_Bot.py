# -*- coding: utf-8 -*-

from interactions import Client, Intents, listen
from interactions import slash_command, SlashContext
from interactions.api.events import Component, GuildJoin, MessageCreate, Startup

bot = Client(intents=Intents.DEFAULT)
# intents are what events we want to receive from discord, `DEFAULT` is usually fine

@listen()  # this decorator tells snek that it needs to listen for the corresponding event, and run this coroutine
async def on_ready():
    # This event is called when the bot is ready to respond to commands
    print("Ready")
    print(f"This bot is owned by {bot.owner}")


@listen(MessageCreate)
async def on_message_create(event : MessageCreate):
    # This event is called when a message is sent in a channel the bot can see
    print(f"message received: {event.message.content}")


@slash_command(name="my_command", description="My first command :)")
async def my_command_function(ctx: SlashContext):
    await ctx.send("Hello World")

bot.load_extension("global_menu")
bot.load_extension("user_profile")
bot.start("MTAxODI5NTYyODczODA3MjYzNA.Gqza5J.yA5JMJUK76p6DSSWTol46n4UEcXnDwgKewy1A4")