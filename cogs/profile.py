import discord
from discord.ext import commands
import firebase_admin

class profile(commands.Cog):


    def __init__(self, client):
        self.client = client

  
def setup(client):
    client.add_cog(profile(client))