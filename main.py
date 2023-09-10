import os        #for os environ memes
import discord   #for discord environ memes
import gspread   #for google api memes

import gSheet    #custom file with gsheet functions
import botcommands
from math import sqrt
import random

##Credential Memes
credentials = {
  "type": "service_account",
  "project_id": os.environ['project_id'],
  "private_key_id": os.environ['private_key_id'],
  "private_key": os.environ['private_key'],
  "client_email": os.environ['client_email'],
  "client_id": os.environ['client_id'],
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": os.environ['client_x509_cert_url'],
  "universe_domain": "googleapis.com"
}
gc = gspread.service_account_from_dict(credentials)

##Opening Google Sheet
sheet = gc.open("Strahd_CS")
NPCdata = sheet.worksheet("NPCs(4)").get_all_values()
SPELLdata = sheet.worksheet("SpellsBot").get_all_values()
#print(type(SPELLdata
#gSheet.printdata(SPELLdata)
spellreq = "Acid Splash"
spellreq2 = "test"
#print(botcommands.searchspell(spellreq, SPELLdata))


#-------Discord Bot----------------------------------------------------
# Create a bot instance with a prefix for commands
bot = discord.Client(intents=discord.Intents.all())
# Define a command
@bot.event
async def on_ready():
    #Prints bots display name and id in console
    print(f'Logged in as {bot.user.name} ({bot.user.id})')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
        informant = message.author.name         #the person messaging
        #if someone is adressing the keeper
        if ("Keeper" in message.content or "keeper" in message.content):
            om = ""    
            if 'What are The Archives' in message.content or 'what are the archives' in message.content or 'what are The Archives' in message.content or 'What are the archives' in message.content or "what are the Archives" in message.content:
                om = "The Archives is a place limitless information, with knowledge gathered from many worlds and the realms within. I will answer questions to the best of my ability but The Arbiter of The Archives has deemed many archives inaccessible to you. For now."
            #bot introduction
            if 'Who are you' in message.content or 'who are you' in message.content:
                om = "I am The Keeper of The Archives. I am here to answer any questions permitted within your assigned access level."
            if 'hello' in message.content or 'Hello' in message.content:
                await message.channel.send("Hello")      
#get spell information
    if message.content.startswith('!spell'):
        #call spell function
        messageSTR = message.content.replace('!spell ', '')
        await message.channel.send(botcommands.searchspell(messageSTR, SPELLdata))
    if message.content.startswith('!hyp'):
        #call hyp function
        temp = str(message.content)
        await message.channel.send(botcommands.calchyp(temp))
    if message.content.startswith('!dmg'):
        #call damage function
        temp = str(message.content)
        await message.channel.send(botcommands.calcdmg(temp))
  
#shhh -  for token menes
my_secret = os.environ['Secret_Memes']
bot.run(my_secret)
