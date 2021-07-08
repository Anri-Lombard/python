import discord

bot = discord.Client()

@bot.event
async def on_ready():
    guild_count = 0
    
    
    for guild in bot.guilds:
        print(f"- {guild.id} (name: {guild.name})")
        
        guild_count += 1
        
    print("Encourage Bot is in " + str(guild_count) + " guilds.")
    
@bot.event
async def on_message(message):
    if message.content.startswith("hello"):
        await message.channel.send("hey you!")

bot.run("ODYyNjk3NDA5NDc3ODY5NjY5.YOcHkg.Xs7-76r03iiYZq10DHE1cd37wUk")