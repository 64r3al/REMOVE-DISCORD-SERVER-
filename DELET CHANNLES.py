import discord
from discord.ext import commands

# Replace with your bot's token and guild ID
TOKEN = 'YOUR_BOT_TOKEN'
GUILD_ID = YOUR_GUILD_ID

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    # Get the guild (server) object
    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        print("Guild not found. Check the GUILD_ID.")
        return

    # Iterate through all channels in the guild and delete them
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"Deleted channel: {channel.name}")
        except Exception as e:
            print(f"Could not delete channel {channel.name}: {e}")

    print("Finished deleting all channels.")

# Run the bot
bot.run(TOKEN)
