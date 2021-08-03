import os
import asyncio
import discord
from webserver import keep_alive
from discord.ext import commands
from discord.ext.commands import Bot

client = commands.Bot(command_prefix='.', intents=discord.Intents.all())

client.remove_command('help')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{len(client.users)} members in STEM Nest"))
    print('Bot is Ready.')


'''

@client.event()
async def on_message(message):
    if message.author == client.user:
        return


    if message.content.startswith('no u'):
        await message.channel.send('no u')

'''

@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
    msg = '**Command is still on Cooldown**, Please try again in {:.2f}s'.format(error.retry_after)
    await ctx.send(msg)

# HELP COMMANDS
@client.command()
async def help2(ctx):
  await ctx.send('There are Two Categories in the **.help** Command, Type **.helpmod** For Moderation Commands and Type **.helpothers** For Other Commands.')


@client.command(pass_context=True)
async def helpmod(ctx):
  author = ctx.message.author

  embed = discord.Embed(
    color = discord.Colour.red()
  )

  embed.set_author(name='Moderation')
  embed.add_field(name='.help', value='Shows this Embed.', inline=False)
  embed.add_field(name='.ban', value='Bans the user, use **.ban <user>**.', inline=False)
  embed.add_field(name='.unban', value='Unbans the user, use **.unban <user>**.', inline=False)
  embed.add_field(name='.mute', value='Mutes the user, use **.mute <user>**.', inline=False)
  embed.add_field(name='.unmute', value='Unmutes the user, use **.unmute <user>**.', inline=False)
  embed.add_field(name='.addrole', value='Adds a Role to the user, use **.addrole <role> <user>**.__**Note**__: You must have the **Manage Server** Permit To Use This Command.', inline=False)
  embed.add_field(name='.removerole', value='Removes a Role from the user, use **.removerole <role> <user>**.__**Note**__: You must have the **Manage Server** Permit to use this Command.', inline=False)
  embed.add_field(name='.kick', value='Kicks the member, use **.kick <user>**.', inline=False)
  embed.add_field(name='.purge', value='Deletes the selected amount of messages, use **.purge <amount>**.', inline=False)

  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def helpothers(ctx):
  author = ctx.message.author

  embed = discord.Embed(
    color = discord.Colour.red()
  )
  
  embed.set_author(name='Others')
  embed.add_field(name='.ping', value='Shows the ping.', inline=False)
  embed.add_field(name='.whois', value='Gives information about the user, use **.whois <user>**.', inline=False)

  await ctx.send(embed=embed)

@client.command(pass_context=True)
async def help(ctx):
  author = ctx.message.author

  embed = discord.Embed(
    color=discord.Colour.dark_purple(), description="**Type Any ONE of Them in Their Channels To Ping The Roles, Please Don't Spam and be patient**")

  embed.set_author(name='STEM Nest Help Manual!')
  embed.add_field(name='**__Math__ Help**!', value='``.algebra`` , ``.geometry`` , ``.trigonometry`` , ``.calculus`` , ``.statistics``', inline=False)
  embed.add_field(name='**__Physics__ Help**!', value='``.mechanics`` , ``.wavesandthermodynamics`` , ``.electricityandmagnetism`` , ``.opticsandmodernphysics``', inline=False)
  embed.add_field(name='**__Chemistry__ Help**!', value='``.analytical`` , ``.biochemistry`` , ``.inorganic`` ``.organic | .physical``', inline=False)
  embed.add_field(name='**__Biology__ Help**!', value='``.generalbiology | .zoology | .anatomy | .microbiology | .botany | .ecology``', inline=False)
  embed.set_footer(text=f'Requested By {ctx.message.author.display_name}', icon_url=f'{ctx.message.author.avatar_url}')

  await ctx.send(embed=embed)


@client.command(pass_context=True, aliases=['algebrahelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def algebra(ctx):
  if ctx.channel.name == "algebra":
    await ctx.channel.send(f'Heya <@&848771024275243008> {ctx.message.author.mention} Needs help with Algebra!')
  else:
    await ctx.channel.send("Please Ask for help in <#807282403093381201>  ")

@client.command(pass_context=True, aliases=['geohelp', 'geometryhelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def geometry(ctx):
  if ctx.channel.name == "geometry-and-trigonometry":
    await ctx.channel.send(f'Hey <@&848772546819129395> {ctx.message.author.mention} Needs help with Geometry!')
  else:
    await ctx.channel.send("Please Ask for help in <#807282446693302312>")

@client.command(pass_context=True, aliases=['trigonometryhelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def trigonometry(ctx):
  if ctx.channel.name == "geometry-and-trigonometry":
    await ctx.channel.send(f'Hey <@&850008049921294388> {ctx.message.author.mention} Needs help with Trigonometry!')
  else:
    await ctx.send('Please Ask for help in <#807282446693302312>')



@client.command(pass_context=True, aliases=['calculushelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def calculus(ctx):
  if ctx.channel.name == "calculus":
    await ctx.channel.send(f'Hey <@&848772641338032199> {ctx.message.author.mention} Needs help with Calculus!')
  else:
    await ctx.send('Please Ask for help in <#807282536538570793>')

@client.command(pass_context=True, aliases=['statisticshelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def statistics(ctx):
  if ctx.channel.name == "algebra":
    await ctx.channel.send(f'Hey <@&850243484463530004> {ctx.message.author.mention} Needs help with Statistics!')
  else:
      await ctx.send('Please Ask for help in <#807282403093381201>')

@client.command(pass_context=True, aliases=['mechanicshelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def mechanics(ctx):
  if ctx.channel.name == "mechanics":
    await ctx.channel.send(f'Hey <@&848772803493888030> {ctx.message.author.mention} Needs help with Mechanics!')
  else:
    await ctx.send('Please Ask for help in <#844457291679137823>')

@client.command(pass_context=True, aliases=['wavesandthermodynamicshelp', 'watts', 'wattshelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def wavesandthermodynamics(ctx):
  if ctx.channel.name == "general-physics":
    await ctx.channel.send(f'Hey <@&848769506649047071> {ctx.message.author.mention} Needs help with Waves and Thermodynamics!')
  else:
    await ctx.send('Please Ask for help in <#844460186696810507>')

@client.command(pass_context=True, aliases=['electricityandmagnetismhelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def electricityandmagnetism(ctx):
  if ctx.channel.name == "general-physics":
    await ctx.channel.send(f'Hey <@&848772932301357066> {ctx.message.author.mention} Needs help with Electricity and Magnetism!')
  else:
    await ctx.send('Please Ask for help in <#844460186696810507>')

@client.command(pass_context=True, aliases=['opticsandmodernphysicshelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def opticsandmodernphysics(ctx):
  if ctx.channel.name == "modern-physics":
    await ctx.channel.send(f'Hey <@&848772932301357066> {ctx.message.author.mention} Needs help with Optics and Modern Physics!')
  else:
    await ctx.send('Please Ask for help in <#844457609657712640>')

@client.command(pass_context=True, aliases=['analyticalhelp', 'analyticalchemistry', 'analyticalchemistryhelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def analytical(ctx):
  if ctx.channel.name == "physical-chemistry":
    await ctx.channel.send(f'Hey <@&848771745786757129> {ctx.message.author.mention} Needs help with Analytical Chemistry!')
  else:
    await ctx.send('Please Ask for help in <#844438926680784926>')

@client.command(pass_context=True, aliases=['biochemhelp', 'biochemistryhelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def biochemistry(ctx):
  if ctx.channel.name == "organic-chemistry":
    await ctx.channel.send(f'Hey <@&850009374218911754> {ctx.message.author.mention} Needs help with Biochemistry!')
  else:
    await ctx.send('Please Ask for help in <#844438870166601738>')

@client.command(pass_context=True, aliases=['inorganicchemistryhelp', 'inorganichelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def inorganic(ctx):
  if ctx.channel.name == "general-chemistry":
    await ctx.channel.send(f'Hey <@&848770555297398794> {ctx.message.author.mention} Needs help with Inorganic Chemistry!')
  else:
    await ctx.send('Please ask for help in <#790602027293868032>')


@client.command(pass_context=True, aliases=['physicalchemistryhelp', 'physicalchemhelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def physical(ctx):
  if ctx.channel.name == "physical-chemistry":
    await ctx.channel.send(f'Hey <@&850009061478891622> {ctx.message.author.mention} Needs help with Physical Chemistry!')
  else:
    await ctx.send('Please Ask for help in <#844438926680784926>')

@client.command(pass_context=True, aliases=['genralbiohelp', 'generalbiologyhelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def generalbiology(ctx):
  if ctx.channel.name == "general-biology":
    await ctx.channel.send(f'Hey <@&848770355094355998> {ctx.message.author.mention} Needs help with General Biology!')
  else:
    await ctx.send('Please Ask for help in <#800291268064313355>')

@client.command(pass_context=True, aliases=['zoologyhelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def zoology(ctx):
  if ctx.channel.name == "general-biology":
    await ctx.channel.send(f'Hey <@&850007047135035423> {ctx.message.author.mention} Needs help with Zoology!')
  else:
    await ctx.send('Please Ask for help in <#800291268064313355>')

@client.command(pass_context=True, aliases=['anatomyhelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def anatomy(ctx):
  if ctx.channel.name == "anatomy":
    await ctx.channel.send(f'Hey <@&850007757909131284> {ctx.message.author.mention} Needs help with Anatomy!')
  else:
    await ctx.send('Please Ask for help in <#851416066063728640>')

@client.command(pass_context=True, aliases=['microbiologyhelp', 'microbiohelp', 'microbio'])
@commands.cooldown(1,10,commands.BucketType.user)
async def microbiology(ctx):
  if ctx.channel.name == "general-biology":
    await ctx.channel.send(f'Hey <@&850007757909131284> {ctx.message.author.mention} Needs help with Microbiology!')
  else:
    await ctx.send('Please Ask for help in <#800291268064313355>')

@client.command(pass_context=True, aliases=['botanyhelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def botany(ctx):
  if ctx.channel.name == "botany":
    await ctx.channel.send(f'Hey <@&850007446021865502> {ctx.message.author.mention} Needs help with Botany!')
  else:
    await ctx.send('Please ask for help in <#851713349158174730>')

@client.command(pass_context=True, aliases=['ecologyhelp'])
@commands.cooldown(1,10,commands.BucketType.user)
async def ecology(ctx):
  if ctx.channel.name == "general-biology":
    await ctx.channel.send(f'Hey <@&850007446021865502> {ctx.message.author.mention} Needs help with Ecology!')
  else:
    await ctx.send('Please ask for help in <#800291268064313355>')

# WHOIS
@client.command()
async def whois(ctx, member : discord.Member = None):
  if not member:
        member = ctx.message.author
  roles = [role for role in member.roles[1:]]

  embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

  embed.set_thumbnail(url=member.avatar_url)
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  embed.add_field(name="ID:", value=member.id, inline=False)
  embed.add_field(name="Nickname:", value=member.display_name, inline=False)

  embed.add_field(name="Created at:", value=member.created_at.strftime("%a %#d %B %Y, %I:%M %p UTC"))
  embed.add_field(name="Joined at:", value=member.joined_at.strftime("%a %#d %B %Y, %I:%M %p UTC"))

  embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
  embed.add_field(name="Top Role:", value=member.top_role.mention, inline=False)

  embed.add_field(name="Bot?", value=member.bot, inline=True)

  await ctx.send(embed=embed)


# PURGE
@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount=1002):
    channel = ctx.message.channel
    messages = []
    async for message in channel.history(limit=amount + 1):
              messages.append(message)

    await channel.delete_messages(messages)
    await ctx.send(f'{amount} Messages Have Been Purged By {ctx.message.author.mention}', delete_after=4)


 
# PING
@client.command()
async def ping(ctx):
    await ctx.send(f"pong {round(client.latency * 1000)}ms")

# KICK
@client.command()
async def kick(ctx,member:discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.kick_members):
        await ctx.send('This command requires you to have The Permit ''Kick Members.''')
        return
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked!')

# BAN AND UNBAN
@client.command()
async def ban(ctx,member:discord.Member, *, reason=None):
    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send('This command requires you to have The Permit **Ban Members.**')
        return
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been Banned!')
@client.command()
async def unban(ctx, *, member):
    if (not ctx.author.guild_permissions.ban_members):
        await ctx.send('This command requires you to have The Permit **Ban Members.**')
        return
    bannned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')

    for ban_entry in bannned_users:
        user = ban_entry.user

        if(user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#ROLES ADDING AND REMOVING
@client.command(aliases=['ar'])
async def addrole(ctx, role: discord.Role, member: discord.Member=None):
    if (not ctx.message.author.guild_permissions.administrator):
        await ctx.send('This command requires you to have The Permit ''Manage Server.''')
        return
    discord.utils.get(ctx.guild.roles, name=role)
    member = member or ctx.message.author
    await member.add_roles(role)
    await ctx.send("Added **{}** to **{}**".format(role, member))

@client.command(aliases=['rr'])
async def removerole(ctx, role: discord.Role, member: discord.Member=None):
    if (not ctx.message.author.guild_permissions.administrator):
        await ctx.send('This command requires you to have The Permit ''Manage Server.''')
        return
    discord.utils.get(ctx.guild.roles, name=role)
    member = member or ctx.message.author
    await member.remove_roles(role)
    await ctx.send("Removed **{}** from **{}**".format(role, member))

#VOTE
@client.command(pass_context=True, aliases=['Vote'])
async def vote(ctx):
 await ctx.member.send(f'Hey  {ctx.message.author.mention} Vote for our server at <https://top.gg/servers/790486836979433492/vote>')
@vote.error
async def vote_error(ctx, error):
 await ctx.sedn(error)

# KEEPING THE BOT ONLINE ALL THE TIME
keep_alive()
TOKEN = os.environ.get("STEM_Nest")
client.run(TOKEN)
