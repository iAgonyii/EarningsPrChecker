import json
from urllib.request import Request, urlopen
from urllib.parse import *
import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="*", intents=intents)


@client.event
async def on_ready():
    print('PR Checker bot ready.')
    game = discord.Game("*earnings @user | *prcheck @user")
    await client.change_presence(activity=game)


@client.command(aliases=['pr'])
async def prcheck(ctx, user: discord.Member = None):
    if user:
        name = user.display_name
        epicid = getepicidbyname(name)
        # valid connection - look for PR values
        if epicid:
            fnrprofile = getfnrdata(epicid)
            fntprofile = getfntdata(name)
            await ctx.send(buildmsg(fnrprofile, fntprofile, user))
        else:
            await ctx.send(
                user.mention + "This user's Epic account is not properly connected with this Discord server. Unable to PR check.")
    else:
        ctx.send('Commands usage: *prcheck @user')


@client.command(aliases=['earnings'])
async def earningscheck(ctx, user: discord.Member = None):
    if user:
        name = user.display_name
        fntprofile = getfntdata(name)
        if fntprofile:
            await ctx.send('**Earnings check {}**\n- **${:,}** Earnings\n🥶🥶🥶🥶🥶🥶🥶'.format(user.display_name, round(fntprofile['cashPrize'])))
        else:
            await ctx.send('Unable to load profiles...')
    else:
        ctx.send('Commands usage: *prcheck @user')


def buildmsg(fnr, fnt, user: discord.Member):
    msg = ''
    if fnr and fnt:
        msg += '**Power Rankings check {}**\n- **{} PR points** on Fortnite Rankings\n- **{} PR points** on Fortnite Tracker\n🥶🥶🥶🥶🥶🥶🥶'.format(
            user.display_name, fnr['prPoints'], fnt['points'])
    elif not fnr and fnt:
        msg += '**Power Rankings check {}**\n- **No profile** on Fortnite Rankings\n- **{} PR points** on Fortnite Tracker\n🥶🥶🥶🥶🥶🥶🥶'.format(
            user.display_name, fnt['points'])
    elif not fnr and not fnt:
        msg += 'Unable to load profiles...'
    return msg


def getepicidbyname(name):
    req = Request(os.getenv('FNAPI_URL') + 'lookup?username=' + quote(name))
    req.add_header('Authorization', os.getenv('FNAPI_TOKEN'))
    content = urlopen(req).read()
    content = json.loads(content.decode('UTF-8'))
    if content['result']:
        return content['account_id']
    else:
        return False


def getfnrdata(id):
    req = Request(os.getenv('FNR_URL') + 'player/id/' + id)
    req.add_header('Authorization', os.getenv('FNR_TOKEN'))
    req.add_header('Accept', 'application/json')
    req.add_header('user-agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
    content = urlopen(req).read()
    content = json.loads(content.decode('UTF-8'))
    if content:
        return content
    else:
        return False


def getfntdata(name):
    req = Request(os.getenv('FNT_URL') + 'powerrankings/GLOBAL/GLOBAL/' + quote(name))
    req.add_header('TRN-Api-Key', os.getenv('FNT_TOKEN'))
    req.add_header('Accept', 'application/json')
    req.add_header('user-agent',
                   'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
    content = urlopen(req).read()
    content = json.loads(content.decode('UTF-8'))
    try:
        if content and content['points']:
            return content
        else:
            return False
    except KeyError:
        return False


client.run(os.getenv('BOT_TOKEN'))
