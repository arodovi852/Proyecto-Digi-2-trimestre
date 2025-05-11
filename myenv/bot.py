import datetime
import json
import os
import discord
from discord.ext import commands, tasks
from dataclasses import dataclass
from typing import Final
from dotenv import load_dotenv
from discord import Intents, Client, Message
from responses import get_response



load_dotenv()
BOT_TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
#Put the Channel_ID here. For more info, check the documentation.
CHANNEL_ID = 1350811849137983630



MAX_SESSION_MINUTES = 30
@dataclass
class Session:
    is_active: bool = False
    start_time: int = 0
bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())
session = Session()

intents: Intents = Intents.default()
intents.message_content = True
client: Client = Client(intents=intents)

async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        print("Empty message")
        return
    if is_private := user_message[0] == '?':
        user_message=user_message[1:]
    try:
        response: str = get_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready():
    print(f"{client.user} working as intended.")


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return
    username: str = str(message.author)
    user_message: str = str(message.content)
    channel: str = str(message.channel)
    print(f'[{channel}] {username}: "{user_message}"')

@bot.event
async def on_ready():
    print("Welcome! The Discord Work Management bot is ready.")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("Welcome! The Discord Work Management bot is ready. Type !commands to see the list of commands.")

    
@tasks.loop(minutes=MAX_SESSION_MINUTES, count=20)
async def break_reminder():
    if break_reminder.current_loop == 0:
        return
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"**Take a break**, you've been working for {MAX_SESSION_MINUTES} minutes.")


@bot.command()
async def commands(ctx):
    lista_de_comandos = "!start - Starts a new work session.\n!end - Ends an on-going work session.\n!add _task_ - Adds a task to the tasklist.\n!endtask _task_ - Ends the selected task.\n!list - Shows a list with every task.\n!clear - Deletes all saved tasks."
    await ctx.send(f"List of commands:\n{lista_de_comandos}")

@bot.command()    
async def start(ctx):
    if session.is_active:
        await ctx.send("There's an on-going session already. Close the session with !end to start a new one.")
        return
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()  
    human_time = ctx.message.created_at.strftime("%H:%M:%S")
    break_reminder.start()  
    await ctx.send(f"Work session started at {human_time}")


@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("There aren't any active sessions.")
        return
    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time  
    human_duration = str(datetime.timedelta(seconds=duration))  
    break_reminder.stop()
    await ctx.send(f"Work session lasted: {human_duration}.")

@bot.command()
async def add(ctx, tarea):
    
    with open("data.json", "r") as f:
        data = json.load(f)

        data.append({"Task": tarea})

        with open("data.json", "w") as f:
            json.dump(data, f)
    f.close()
    await ctx.send(f'Task "{tarea}" added to the list of tasks')
    
@bot.command()
async def list(ctx):
    with open('data.json', 'r') as file:
        data = json.load(file)
    file.close()
    await ctx.send(f"The current list of tasks is: {data}")
    
@bot.command()
async def endtask(ctx, tarea):
    
    
    with open("data.json", "r") as f:
        data = json.load(f)

        
        for i in range(len(data)):
            if data[i]['tarea'] == tarea:  
                data.pop(i)  
                break  
            
        with open("data.json", "w") as f:
            json.dump(data, f)
    f.close()
    await ctx.send(f'Task "{tarea}" completed')
    
@bot.command()
async def clear(ctx):
    with open("data.json", "r") as f:
        data = json.load(f)
        while not data == []:
            for k in data:
                data.remove(k)
        with open("data.json", "w") as f:
            json.dump(data, f)
    f.close()
    await ctx.send(f'Data deleted successfully')
            
    
bot.run(BOT_TOKEN)

client.run(token=BOT_TOKEN)

    

   
    
    