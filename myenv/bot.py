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
#Desde Discord, introduce el ID del servidor en CHANNEL_ID. Para más información sobre esto, consultado la documentación.
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
        print("Mensaje vacío")
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
    print(f"{client.user} funcionando correctamente.")


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
    print("¡Buenas! El bot de organización de tareas está listo")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send("¡Buenas! El bot de organización de tareas está listo. Escribe !commands para ver la lista de comandos.")

    
@tasks.loop(minutes=MAX_SESSION_MINUTES, count=10)
async def break_reminder():
    if break_reminder.current_loop == 0:
        return
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"**Tómate un descanso**, llevas trabajando {MAX_SESSION_MINUTES} minutos.")


@bot.command()
async def commands(ctx):
    lista_de_comandos = "!start - Comienza una sesión de trabajo.\n!end - Finaliza una sesión de trabajo.\n!add _tarea_ - Añade una tarea a la lista de tareas.\n!endtask _tarea_ - Finaliza la tarea deseada.\n!list - Muestra una lista con todas las tareas.\n!clear - Elimina todas las tareas de la lista de tareas."
    await ctx.send(f"Lista de comandos:\n{lista_de_comandos}")

@bot.command()    
async def start(ctx):
    if session.is_active:
        await ctx.send("Ya hay una sesión activa.")
        return
    session.is_active = True
    session.start_time = ctx.message.created_at.timestamp()  
    human_time = ctx.message.created_at.strftime("%H:%M:%S")
    break_reminder.start()  
    await ctx.send(f"Sesión de trabajo comenzada a las {human_time}")


@bot.command()
async def end(ctx):
    if not session.is_active:
        await ctx.send("No hay ninguna sesión activa.")
        return
    session.is_active = False
    end_time = ctx.message.created_at.timestamp()
    duration = end_time - session.start_time  
    human_duration = str(datetime.timedelta(seconds=duration))  
    break_reminder.stop()
    await ctx.send(f"Sesión de trabajo comenzada a las {human_duration}.")

@bot.command()
async def add(ctx, tarea):
    
    with open("data.json", "r") as f:
        data = json.load(f)

        data.append({"tarea": tarea})

        with open("data.json", "w") as f:
            json.dump(data, f)
    f.close()
    await ctx.send(f'Tarea "{tarea}" añadida a la lista de tareas')
    
@bot.command()
async def list(ctx):
    with open('data.json', 'r') as file:
        data = json.load(file)
    file.close()
    await ctx.send(f"La lista de tareas actual es: {data}")
    
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
    await ctx.send(f'Tarea "{tarea}" completada')
    
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
    await ctx.send(f'Datos eliminados exitosamente')
            
    
bot.run(BOT_TOKEN)

client.run(token=BOT_TOKEN)

    

   
    
    