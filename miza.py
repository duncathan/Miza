import discord, ast, os, sys, asyncio, datetime, json, shlex
import urllib.request
from smath import *

client = discord.Client(max_messages=2000, activity=discord.Activity(name="Magic"),)

from matplotlib import use as plot_sys

plot_sys("Agg")
from matplotlib import pyplot as plt

bar_plot = plt.bar
plot_points = plt.scatter
plot = plt.plot
plotY = plt.semilogy
plotX = plt.semilogx
plotXY = plt.loglog
fig = plt.figure()


class _globals:
    timeout = 10
    disabled = [
        "__",
        "open",
        "import",
        "urllib",
        "discord",
        "exec",
        "eval",
        "locals",
        "globals",
        "vars",
        "client",
        "os",
        "sys",
        "async",
        "compile",
        "threading",
        "input",
        "exit",
        "quit",
        "getattr",
        ".load",
        ".save",
        ".fromfile",
        "ctypes",
    ]

    def __init__(self):
        self.lastCheck = time.time()
        self.queue = {}
        try:
            f = open("perms.json")
            self.perms = eval(f.read())
            f.close()
        except:
            self.perms = {}
        try:
            f = open("bans.json")
            self.bans = eval(f.read())
            f.close()
        except:
            self.bans = {0: {}}
        try:
            f = open("enabled.json")
            self.enabled = eval(f.read())
            f.close()
        except:
            self.enabled = {}
        doParallel(self.update, [])
        self.fig = fig
        self.plt = plt
        f = open("auth.json")
        auth = ast.literal_eval(f.read())
        f.close()
        self.owner_id = auth["owner_id"]
        self.token = auth["discord_token"]
        self.resetGlobals()
        doParallel(self.getModules)

    def getModule(self, module, category):
        exec("import " + module + " as _vars_", globals())
        commands = []
        vd = _vars_.__dict__
        for k in vd:
            var = vd[k]
            try:
                assert var.is_command
                obj = var()
                obj.__name__ = var.__name__
                obj.name.append(obj.__name__)
                commands.append(obj)
            except AttributeError:
                pass
        self.categories[category] = commands

    def getModules(self):
        comstr = "commands_"
        files = [f for f in os.listdir(".") if f[-3:] == ".py" and comstr in f]
        self.categories = {}
        for f in files:
            module = f[:-3]
            category = module.replace(comstr, "")
            doParallel(self.getModule, [module, category])

    def update(self):
        f = open("perms.json", "w")
        f.write(str(self.perms))
        f.close()
        f = open("bans.json", "w")
        f.write(str(self.bans))
        f.close()
        f = open("enabled.json", "w")
        f.write(str(self.enabled))
        f.close()

    def verifyID(self, value):
        return int(str(value).replace("<", "").replace(">", "").replace("@", "").replace("!", ""))

    def getPerms(self, user, guild):
        try:
            u_id = user.id
        except:
            u_id = user
        if guild:
            g_id = guild.id
            g_perm = self.perms.get(g_id, {})
            self.perms[g_id] = g_perm
            if u_id == self.owner_id:
                u_perm = nan
                g_perm[u_id] = nan
            else:
                u_perm = g_perm.get(u_id, 0)
        else:
            u_perm = 1
        return u_perm

    def resetGlobals(self):
        self.stored_vars = dict(globals())
        for i in self.disabled:
            try:
                self.stored_vars.pop(i)
            except:
                pass
        return self.stored_vars

    def updateGlobals(self):
        temp = dict(globals())
        for i in self.disabled:
            try:
                temp.pop(i)
            except:
                pass
        self.stored_vars.update(temp)
        return self.stored_vars

    def verifyCommand(self, func):
        f = func.lower()
        for d in self.disabled:
            if d in f:
                raise PermissionError("Issued command is not enabled.")
        return func

    def verifyURL(self, _f):
        _f = _f.replace("<", "").replace(">", "").replace("|", "").replace("*", "").replace("_", "").replace("`", "")
        return _f

    def doMath(self, f, returns):
        try:
            self.verifyCommand(f)
            try:
                answer = eval(f, self.stored_vars)
            except:
                exec(f, self.stored_vars)
                answer = None
        except Exception as ex:
            answer = "\nError: " + repr(ex)
        if answer is not None:
            answer = str(answer)
        returns[0] = answer

    def evalMath(self, f):
        self.verifyCommand(f)
        return eval(f)


async def processMessage(message):
    global client
    perms = _vars.perms
    bans = _vars.bans
    categories = _vars.categories
    stored_vars = _vars.stored_vars
    msg = message.content
    if msg[:2] == "> ":
        msg = msg[2:]
    elif msg[:2] == "||" and msg[-2:] == "||":
        msg = msg[2:-2]
    msg = msg.replace("`", "")
    user = message.author
    guild = message.guild
    u_id = user.id
    if guild:
        g_id = guild.id
    else:
        g_id = 0
    if g_id:
        try:
            enabled = _vars.enabled[g_id]
        except KeyError:
            enabled = _vars.enabled[g_id] = ["string", "admin"]
            _vars.update()
    else:
        enabled = list(_vars.categories)
    u_perm = _vars.getPerms(user.id, guild)
    ch = channel = message.channel

    check = "<@!" + str(client.user.id) + ">"
    suspended = _vars.bans[0].get(u_id, False)
    if suspended or msg.replace(" ", "") == check:
        if not u_perm < 0 and not suspended:
            await channel.send("Hi, did you require my services for anything? Use ~? or ~help for help.")
        else:
            doParallel(print, ["Ignoring command from suspended user " + user.name + " (" + str(u_id) + ")."])
            await channel.send("Sorry, you are currently not permitted to request my services.")
        return
    if msg[0] == "~" and msg[1] != "~":
        comm = msg[1:]
        op = True
    elif msg[: len(check)] == check:
        comm = msg[len(check) :]
        while comm[0] == " ":
            comm = comm[1:]
        op = True
    else:
        op = False
    if op:
        commands = []
        for catg in categories:
            if catg in enabled or catg == "main":
                commands += categories[catg]
        for command in commands:
            for alias in command.name:
                alias = alias.lower()
                length = len(alias)
                check = comm[:length].lower()
                argv = comm[length:]
                if check == alias and (len(comm) == length or comm[length] == " " or comm[length] == "?"):
                    doParallel(print, [user.name + " (" + str(u_id) + ") issued command " + msg])
                    req = command.minm
                    if req > u_perm or (u_perm is not nan and req is nan):
                        await channel.send(
                            "Error: Insufficient priviliges for command "
                            + alias
                            + "\
.\nRequred level: **__"
                            + str(req)
                            + "__**, Current level: **__"
                            + str(u_perm)
                            + "__**"
                        )
                        return
                    try:
                        await channel.trigger_typing()
                        if argv:
                            while argv[0] == " ":
                                argv = argv[1:]
                        flags = {}
                        for c in range(26):
                            char = chr(c + 97)
                            flag = "?" + char
                            for r in (flag.lower(), flag.upper()):
                                if len(argv) >= 4 and r in argv:
                                    i = argv.index(r)
                                    if i == 0 or argv[i - 1] == " " or argv[i - 2] == "?":
                                        try:
                                            if argv[i + 2] == " " or argv[i + 2] == "?":
                                                argv = argv[:i] + argv[i + 2 :]
                                                addDict(flags, {char: 1})
                                        except:
                                            pass
                        for c in range(26):
                            char = chr(c + 97)
                            flag = "?" + char
                            for r in (flag.lower(), flag.upper()):
                                if len(argv) >= 2 and r in argv:
                                    for check in (r + " ", " " + r):
                                        if check in argv:
                                            argv = argv.replace(check, "")
                                            addDict(flags, {char: 1})
                                    if argv == flag:
                                        argv = ""
                                        addDict(flags, {char: 1})
                        a = argv.replace('"', "\0")
                        b = a.replace("'", "")
                        c = b.replace("<", "'")
                        d = c.replace(">", "'")
                        args = shlex.split(d)
                        for a in range(len(args)):
                            args[a] = args[a].replace("", "'").replace("\0", '"')
                        response = await command(client=client, _vars=_vars, argv=argv, args=args, flags=flags, user=user, message=message, channel=channel, guild=guild, name=alias,)  # for interfacing with discord  # for interfacing with bot's database  # raw text arguments  # split text arguments  # special flags  # user that invoked the command  # message data  # channel data  # guild data  # alias the command was called as
                        if response is not None:
                            if len(response) < 65536:
                                doParallel(print, [response])
                            else:
                                print("[RESPONSE OVER 64KB]")
                            if type(response) is list:
                                for r in response:
                                    await channel.send(r)
                            else:
                                await channel.send(response)
                    except discord.HTTPException:
                        fn = "cache/temp.txt"
                        _f = open(fn, "wb")
                        _f.write(bytes(response, "utf-8"))
                        _f.close()
                        _f = discord.File(fn)
                        await channel.send("Response too long for message.", file=_f)
                    except Exception as ex:
                        rep = repr(ex)
                        if len(rep) > 1900:
                            await channel.send("```\nError: Error message too long.\n```")
                        else:
                            await channel.send("```\nError: " + rep + "\n```")
                    return


@client.event
async def on_ready():
    print("Successfully connected as " + str(client.user))
    print("Servers: ")
    for guild in client.guilds:
        if guild.unavailable:
            print(str(guild.id) + " is not available.")
        else:
            print(guild.name)
    await handleUpdate()


##    print("Users: ")
##    for guild in client.guilds:
##        print(guild.members)


async def handleUpdate(force=False):
    global client, _vars
    if force or time.time() - _vars.lastCheck > 0.5:
        _vars.lastCheck = time.time()
        dtime = datetime.datetime.utcnow().timestamp()
        bans = _vars.bans
        if bans:
            for g in bans:
                bl = list(bans[g])
                for b in bl:
                    if type(bans[g][b]) is list and dtime >= bans[g][b][0]:
                        u_target = await client.fetch_user(b)
                        g_target = await client.fetch_guild(g)
                        c_target = await client.fetch_channel(bans[g][b][1])
                        bans[g].pop(b)
                        try:
                            await g_target.unban(u_target)
                            await c_target.send("**" + u_target.name + "** has been unbanned from **" + g_target.name + "**.")
                        except:
                            await c_target.send("Unable to unban **" + u_target.name + "** from **" + g_target.name + "**.")
            f = open("bans.json", "w")
            f.write(str(bans))
            f.close()
        for vc in client.voice_clients:
            membs = vc.channel.members
            cnt = len(membs)
            if not cnt > 1:
                await vc.disconnect(force=False)


async def checkDelete(message, reaction, user):
    if message.author.id == client.user.id:
        u_perm = _vars.getPerms(user.id, message.guild)
        check = False
        if not u_perm < 1:
            check = True
        else:
            for reaction in message.reactions:
                async for u in reaction.users():
                    if u.id == client.user.id:
                        check = True
        if check:
            if user.id != client.user.id:
                s = str(reaction)
                if s in "❌✖️🇽❎":
                    try:
                        temp = message.content
                        await message.delete()
                        print(temp + " deleted by " + user.name)
                    except Exception as ex:
                        print(repr(ex))
            await handleUpdate()


async def reactCallback(message, reaction, user):
    if message.author.id == client.user.id:
        suspended = _vars.bans[0].get(user.id, False)
        if suspended:
            return
        u_perm = _vars.getPerms(user.id, message.guild)
        check = "```callback-"
        msg = message.content.split("\n")[0]
        if msg[: len(check)] == check:
            msg = msg[len(check) :]
            args = msg.split("-")
            catx = args[0]
            func = args[1]
            vals = args[2]
            argv = "-".join(args[3:])
            catg = _vars.categories[catx]
            for f in catg:
                if f.__name__ == func:
                    try:
                        await asyncio.wait_for(f._callback_(client=client, message=message, reaction=reaction, user=user, perm=u_perm, vals=vals, argv=argv), timeout=_vars.timeout)
                        return
                    except Exception as ex:
                        killThreads()
                        await message.channel.send("```\nError: " + repr(ex) + "\n```")


@client.event
async def on_reaction_add(reaction, user):
    message = reaction.message
    if user.id != client.user.id:
        await checkDelete(message, reaction, user)
        await reactCallback(message, reaction, user)


@client.event
async def on_reaction_remove(reaction, user):
    message = reaction.message
    if user.id != client.user.id:
        await checkDelete(message, reaction, user)
        await reactCallback(message, reaction, user)


@client.event
async def on_raw_reaction_add(payload):
    try:
        channel = await client.fetch_channel(payload.channel_id)
        user = await client.fetch_user(payload.user_id)
        message = await channel.fetch_message(payload.message_id)
    except Exception as ex:
        print(repr(ex))
        return
    if user.id != client.user.id:
        reaction = payload.emoji
        await checkDelete(message, reaction, user)


@client.event
async def on_raw_message_delete(payload):
    await handleUpdate()


@client.event
async def on_typing(channel, user, when):
    await handleUpdate()


@client.event
async def on_voice_state_update(member, before, after):
    await handleUpdate()


async def handleMessage(message):
    msg = message.content
    user = message.author
    u_id = user.id
    u_perm = _vars.perms.get(u_id, 0)
    if not len(msg) > 1:
        return
    elif u_id == client.user.id:
        if "Error: " in msg or "Commands for " in msg or msg == "Response too long for message.":
            try:
                await message.add_reaction("❎")
            except Exception as ex:
                print(repr(ex))
    try:
        await asyncio.wait_for(processMessage(message), timeout=_vars.timeout)
    except Exception as ex:
        killThreads()
        await message.channel.send("```\nError: " + repr(ex) + "\n```")
    return


@client.event
async def on_message(message):
    await reactCallback(message, None, message.author)
    await handleUpdate()
    await handleMessage(message)
    await handleUpdate(True)


@client.event
async def on_message_edit(before, after):
    message = after
    await handleUpdate()
    await handleMessage(message)
    await handleUpdate(True)


@client.event
async def on_raw_message_edit(payload):
    message = None
    if payload.cached_message is None:
        try:
            channel = await client.fetch_channel(payload.data["channel_id"])
            message = await channel.fetch_message(payload.message_id)
        except:
            for guild in client.guilds:
                for channel in guild.text_channels:
                    try:
                        message = await channel.fetch_message(payload.message_id)
                    except Exception as ex:
                        print(repr(ex))
    if message:
        await handleUpdate()
        await handleMessage(message)
        await handleUpdate(True)


if __name__ == "__main__":
    _vars = _globals()
    print("Attempting to authorize with token " + _vars.token + ":")
    client.run(_vars.token)
