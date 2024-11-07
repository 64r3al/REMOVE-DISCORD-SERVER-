import discord
import asyncio
from discord.ext import commands

# Replace with your bot token and guild ID
TOKEN = 'YOUR_BOT_TOKEN'  # Replace with your bot token
GUILD_ID = YOUR_GUILD_ID  # Replace with your guild ID as an integer

intents = discord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    
    # Wait for the bot to fully initialize before trying to get the guild
    await asyncio.sleep(2)
    guild = bot.get_guild(GUILD_ID)

    if guild is None:
        print("Guild not found. Please check your GUILD_ID.")
        return

    print(f"Creating 100 channels in guild: {guild.name}")

    for i in range(100):
        # Name each channel as "twizzyrich" and add a number suffix if desired
        channel_name = f"twizzyrich-{i+1}"
        try:
            await guild.create_text_channel(channel_name)
            print(f"Created channel: {channel_name}")
            await asyncio.sleep(0.1)  # Small delay to prevent hitting rate limits
        except discord.Forbidden:
            print("Bot does not have permission to create channels.")
            break
        except discord.HTTPException as e:
            print(f"Failed to create channel: {channel_name} - {e}")
            continue

    print("Finished creating channels!")

# Run the bot
bot.run(TOKEN)
