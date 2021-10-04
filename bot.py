import discord
import datetime as datetime
from discord.ext import commands


PREFIX = "."
red = (10,10,10)

client = commands.Bot( command_prefix = PREFIX )
client.remove_command( "help" )



@client.event


async def on_ready():
    print( "BOT connected" )

#@client.event
#async def on_command_error( ctx, error ):
    #pass


#_____clear_______
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def clear( ctx, amount : int ): 
    await ctx.channel.purge( limit = amount )

    #await ctx.send( embed = discord.Embed(description = f':white_check_mark: Удалено {amount} сообщение', color = red))


@clear.error
async def clear_error( ctx, error ):
    if isinstance( error, commands.MissingRequiredArgument ):
        await ctx.send( f'{ ctx.author.name }, обязательно укажите аргумент!!!' )

    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f'{ ctx.author.name }, у вас недостаточно прав!!!' )

#______hello______
@client.command( pass_context = True )

async def hello( ctx, amount = 1 ):
    
    await ctx.channel.purge( limit = amount )

    

    author = ctx.message.author
    await ctx.send( f"Hello { author.mention } " )



#_____kick________
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def kick( ctx, member: discord.Member, *, reason = None, amount : int ):
    await ctx.channel.purge( limit = 1 )

    await member.kick( reason = reason )
    await ctx.send( f"kick user { member.mention } " )


@kick.error

async def kick_error( ctx, error):
    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f' { ctx.author.name }, у вас недостаеочно прав!!!')



#_______ban__________
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def ban( ctx, member: discord.Member, *, reason = None ):
    emd = discord.Embed( title = "Ban", color = discord.Color.red() )
    await ctx.channel.purge( limit = 1 )

    await member.ban( reason = reason )

    emd.set_author( name = member.name, icon_url = member.avatar_url )
    emd.add_field( name = "Ban user", value = "Baned user : {}".format( member.mention ) )
    emd.set_footer( text = "Был забанен администратором {}".format( ctx.author.name ), icon_url = ctx.author.avatar_url )

    await  ctx.send( embed = emd ) 

    #await ctx.send( f"ban user { member.mention } " )



@ban.error

async def ban_error( ctx, error):
    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f' { ctx.author.name }, у вас недостаеочно прав!!!')

#_________unban___________
@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def unban( ctx,* , member ):
    await ctx.channel.purge( limit = 1 )

    banned_users = await ctx.guild.bans()

    for ban_entry in banned_users:
        user = ban_entry.user

        await ctx.guild.unban( user )
        await ctx.send( f"unbanned user { user.mention } "  )

        return


@unban.error

async def unban_error( ctx, error):
    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f' { ctx.author.name }, у вас недостаеочно прав!!!')



#_________help________
@client.command( pass_context = True )
#(Admin)

async def help( ctx ):
    emb = discord.Embed( title = "Навигация по командам" )

    emb.add_field( name = "{}clear".format( PREFIX ), value = "Отчистка чата(Admin)" )
    emb.add_field( name = "{}kick".format( PREFIX ), value = "Удаление учасника с сервера(Admin)" )
    emb.add_field( name = "{}ban".format( PREFIX ), value = "Ограничение доступа к серверу(Admin)" )
    emb.add_field( name = "{}time".format( PREFIX ), value = "Смотреть текущее время" )
    emb.add_field( name = "{}unban".format( PREFIX ), value = "Удаление ограничения к серверу(Admin)" )
    emb.add_field( name = "{}hello".format( PREFIX ), value = "Простое приветствие" )


    await ctx.send( embed = emb )


#___________________________________________________________________

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def time( ctx ):
    emb = discord.Embed( title = "Your time", description = "Узнать текущее время " ,colour = discord.Color.green(), url = "https://www.timeserver.ru/cities/kz/taldykorgan" )

    emb.set_author(name = client.user.name, icon_url = client.user.avatar_url)
    emb.set_footer(text = "Спасибо за использования нашего бота!")
    emb.set_image(url = "https://cdn1.ozone.ru/multimedia/1022092489.jpg")
    emb.set_thumbnail(url = "https://cdn1.ozone.ru/multimedia/1022092489.jpg")

    new_date = datetime.datetime.now()


    emb.add_field(name = time, value = "Time : {}".format(new_date))

    await ctx.send(embed = emb)


#____________________________user_mute_______________________________________

@client.command( pass_context = True )
@commands.has_permissions( administrator = True )

async def user_mute( ctx , member: discord.Member ):
    await ctx.channel.purge( limit = 1 )

    mute_role -discod.ntils.get( ctx.message.guild.roles, name = "mute" )

    await member.add_roles( mure_role )
    await ctx.send( f'У { member.mention }, ограничение чата, за нарушение прав!!!' )


@user_mute.error

async def user_mute_error( ctx, error):
    if isinstance( error, commands.MissingPermissions ):
        await ctx.send( f' { ctx.author.name }, у вас недостаеочно прав!!!')




@client.command()
async def send_a( ctx ):
    await ctx.author.send("Hello world")

@client.command()
async def send_m( ctx ):
    await member.send(f' { member.name } , Привет от { ctx.author.name }')



#_________Токен___________
token = open( "token.txt", "r" ).readline()

client.run( token )

