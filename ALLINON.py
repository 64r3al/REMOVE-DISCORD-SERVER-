import discord
from discord.ext import commands
import tkinter as tk
from tkinter import messagebox
import threading

# Define intents and bot
intents = discord.Intents.default()
intents.members = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Function to create and run the Discord bot in a separate thread
def run_bot(token):
    try:
        bot.run(token)
    except Exception as e:
        print(f"Error: {e}")

# Global variables for storing UI input values
bot_token = None
guild_id = None
dm_message = None
channel_name = None
channel_count = None

# Bot event when ready
@bot.event
async def on_ready():
    print(f'Bot is ready as {bot.user}')

# Function to ban all members with an optional DM
async def ban_all_members():
    guild = bot.get_guild(int(guild_id.get()))
    if guild is None:
        messagebox.showerror("Error", "Guild not found. Check the Server ID.")
        return
    
    for member in guild.members:
        if member != guild.owner and not member.bot:
            try:
                if dm_message.get():
                    await member.send(dm_message.get())
                await member.ban(reason="Mass ban script execution")
                print(f"Banned member: {member.name}")
            except Exception as e:
                print(f"Could not DM or ban member {member.name}: {e}")

# Function to delete all channels in the guild
async def delete_all_channels():
    guild = bot.get_guild(int(guild_id.get()))
    if guild is None:
        messagebox.showerror("Error", "Guild not found. Check the Server ID.")
        return
    
    for channel in guild.channels:
        try:
            await channel.delete()
            print(f"Deleted channel: {channel.name}")
        except Exception as e:
            print(f"Could not delete channel {channel.name}: {e}")

# Function to create specified number of channels with a specified name
async def create_channels():
    guild = bot.get_guild(int(guild_id.get()))
    if guild is None:
        messagebox.showerror("Error", "Guild not found. Check the Server ID.")
        return

    num_channels = int(channel_count.get())
    for i in range(num_channels):
        try:
            await guild.create_text_channel(f"{channel_name.get()}-{i+1}")
            print(f"Created channel: {channel_name.get()}-{i+1}")
        except Exception as e:
            print(f"Could not create channel {channel_name.get()}-{i+1}: {e}")

# Tkinter UI setup
root = tk.Tk()
root.title("Discord Server Management Bot")

# Set the background color of the window
root.configure(bg='#1a1a1a')  # Dark background

# Set the font color for labels and buttons
label_font = ('Helvetica', 12, 'bold')
button_font = ('Helvetica', 12, 'bold')

# Bot Token Input
tk.Label(root, text="Bot Token:", fg='white', font=label_font, bg='#1a1a1a').grid(row=0, column=0, sticky="w")
bot_token = tk.Entry(root, width=50, bg='#3c3c3c', fg='white', font=('Helvetica', 12))
bot_token.grid(row=0, column=1, padx=5, pady=5)

# Server ID Input
tk.Label(root, text="Server ID:", fg='white', font=label_font, bg='#1a1a1a').grid(row=1, column=0, sticky="w")
guild_id = tk.Entry(root, width=50, bg='#3c3c3c', fg='white', font=('Helvetica', 12))
guild_id.grid(row=1, column=1, padx=5, pady=5)

# DM Message Input
tk.Label(root, text="DM Message (for Ban):", fg='white', font=label_font, bg='#1a1a1a').grid(row=2, column=0, sticky="w")
dm_message = tk.Entry(root, width=50, bg='#3c3c3c', fg='white', font=('Helvetica', 12))
dm_message.grid(row=2, column=1, padx=5, pady=5)

# Ban All Members Button
def on_ban_all_click():
    if not bot.is_ready():
        messagebox.showerror("Error", "Bot is not ready yet.")
        return
    bot.loop.create_task(ban_all_members())

ban_button = tk.Button(root, text="Ban All Members", command=on_ban_all_click, bg='#8a2be2', fg='white', font=button_font)
ban_button.grid(row=3, column=1, pady=5)

# Delete All Channels Button
def on_delete_channels_click():
    if not bot.is_ready():
        messagebox.showerror("Error", "Bot is not ready yet.")
        return
    bot.loop.create_task(delete_all_channels())

delete_button = tk.Button(root, text="Delete All Channels", command=on_delete_channels_click, bg='#8a2be2', fg='white', font=button_font)
delete_button.grid(row=4, column=1, pady=5)

# Channel Name and Count Input for Creation
tk.Label(root, text="Channel Name:", fg='white', font=label_font, bg='#1a1a1a').grid(row=5, column=0, sticky="w")
channel_name = tk.Entry(root, width=50, bg='#3c3c3c', fg='white', font=('Helvetica', 12))
channel_name.grid(row=5, column=1, padx=5, pady=5)

tk.Label(root, text="Number of Channels:", fg='white', font=label_font, bg='#1a1a1a').grid(row=6, column=0, sticky="w")
channel_count = tk.Entry(root, width=50, bg='#3c3c3c', fg='white', font=('Helvetica', 12))
channel_count.grid(row=6, column=1, padx=5, pady=5)

# Create Channels Button
def on_create_channels_click():
    if not bot.is_ready():
        messagebox.showerror("Error", "Bot is not ready yet.")
        return
    bot.loop.create_task(create_channels())

create_button = tk.Button(root, text="Create Channels", command=on_create_channels_click, bg='#8a2be2', fg='white', font=button_font)
create_button.grid(row=7, column=1, pady=5)

# Function to start bot with input token
def start_bot():
    token = bot_token.get()
    if token:
        threading.Thread(target=run_bot, args=(token,)).start()
    else:
        messagebox.showerror("Error", "Please enter a bot token.")

# Start Bot Button
start_button = tk.Button(root, text="Start Bot", command=start_bot, bg='#32cd32', fg='white', font=button_font)
start_button.grid(row=8, column=1, pady=10)

# Made By IVX Label
made_by_label = tk.Label(root, text="MADE BY IVX", fg='#32cd32', font=('Helvetica', 10, 'italic'), bg='#1a1a1a')
made_by_label.grid(row=9, column=1, pady=10)

root.mainloop()
