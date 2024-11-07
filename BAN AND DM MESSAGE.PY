import discord
from discord.ext import commands

# Replace with your bot's token and guild ID
TOKEN = 'YOUR_BOT_TOKEN'
GUILD_ID = YOUR_GUILD_ID

intents = discord.Intents.default()
intents.members = True  # Enable member intents for accessing member list

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    # Get the guild (server) object
    guild = bot.get_guild(GUILD_ID)
    if guild is None:
        print("Guild not found. Check the GUILD_ID.")
        return

    # Iterate through all members in the guild and send DM before banning
    for member in guild.members:
        if member != guild.owner and not member.bot:  # Exclude the owner and bots from banning
            try:
                # Send DM to the member
                await member.send("Sorry, we’re recreating the server.")
                print(f"Sent DM to {member.name}")
                
                # Ban the member
                await member.ban(reason="Mass ban script execution")
                print(f"Banned member: {member.name}")
            except Exception as e:
                print(f"Could not DM or ban member {member.name}: {e}")

    print("Finished sending DMs and banning all members.")

# Run the bot
bot.run(TOKEN)
