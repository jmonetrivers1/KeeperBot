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
print(botcommands.searchspell(spellreq, SPELLdata))
print(botcommands.searchspell(spellreq2, SPELLdata))

"""
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
    #test - if !hello bot replys with hello (works in private messaging as well)
    if ("Keeper" in message.content or "keeper" in message.content):
        om = ""
#shhh -  for token menes
my_secret = os.environ['Secret_Memes']
bot.run(my_secret)
"""
