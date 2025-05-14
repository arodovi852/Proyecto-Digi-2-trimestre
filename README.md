# Discord Word Management Bot
## Tutorial video - How the bot works and its commands
<video controls src="img/2025-05-11 19-18-24.mp4" title="Title"></video>[
https://drive.google.com/file/d/1VyIs0Fh4fZt9A3UJse96aLpNXrr5QWjG/view?usp=sharing

## Requirements
The bot works locally, so you need to follow these instructions:

It's not mandatory but it's recommended to install the following from the terminal:

    pip install discord.py
    
    pip install python-dotenv

It's only really necessary if either one doesn't appear as installed.

Now onto the bot's features (in written form):

## Steps to follow

- **Step 1:** Enter a Discord server where you're admin.
 
![alt text](img/image.png)

- **Step 2:** Go to user settings.
 
![alt text](img/image-2.png)

- **Step 3:** Go to App Settings y Advanced.
 
![alt text](img/image-3.png)

- **Step 4:** Turn on Developer Mode. This will allow you to use the bot.
 
![alt text](img/image-4.png)

- **Step 5:** Going back to the server, enter the channel where you want to use your bot. You will copy its ID here.

![alt text](img/image-6.png)

- **Step 6:** Paste your ID on CHANNEL_ID:

![alt text](img/image-8.png)

Remember to **paste it normally**, the variable must be an integer for the bot to work:

![alt text](img/image-9.png)

And now, you should be able to run the bot by pressing the run button on VSCode!

## Devlog
At the very start of the project, the most important part took place: Brainstorming. Lots of ideas were thrown out, but the one that
stuck out the most was the idea of a bot that could automatically do tasks for you. This idea would later become a Twitter bot.

This idea was further developed into a bot that would automatize posts pulling data from an excel sheet, and since it was mainly being created with the intent of helping with annoying tasks, the idea of marketing and making the process of posting content on social media much easier arose.

Now, the issue with this particular idea was that, while very straightforward came with the complexities of Twitter's developer portal, which while usable it could be very limited at that. This lead to the idea being scrapped.

However, the bot still seemed like a good idea, and since lots of people use Discord for work the bot was now repurposed to 

This way, after following some YouTube tutorials and reading a lot of Discord's documentation, progress was made and lots of functionalities were created.

Since the main purpose of this bot was to organize, there needed to be some functionalities that fit into this. This is when the work session was created. Work sessions would allow users to keep track of their time and be reminded every once in a while to take a break, which was settled in 30 minutes after some consideration.

However, this was too simple, so another feature was added: Saving and deleting tasks from a list. Things went smooth when it came to coding them, but the biggest roadblock was actually figuring out how to go about inserting data into the list, since it was a difficult decision. The final result shows the following format: 

    "Task: (taskname)"

Additionally, there was a lot of testing done surrounding the delete command, since the format of the list kept changing throughout the bot's history. This is also when the final functionality was created: Clear. By clearing tasks from the list, they list would be fully depleted from any tasks, which came in handy specially during testing.

And as the time of writing this, that's everything about the bot so far. It might get some additional functionalities in the future that weren't included, but for now this is the first version of the product.

The bot was going to be initially going to be a Twitter bot instead, however while developing the project 
Para este proyecto he decidido desarrollar un programa/plugin para automatizar la subida de vídeos a Twitter, una especie de bot con el propósito de facilitar en específico el ámbito del marketing
de los videojuegos indie a través de la subido de contenido y clips diversos del juego, ya que esta suele ser una de las partes más tediosas del desarrollo de juegos.
