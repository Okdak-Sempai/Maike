# Work with Python 3.6
#pip install --upgrade discord.py
#sudo apt-get install ffmpeg
import discord
from discord.ext import tasks
from discord.ext import commands
from discord import Member
import asyncio
import youtube_dl #pip install youtube-dl
from pytube import YouTube
import os
from datetime import date, datetime
from discord.flags import Intents

def GiveDate():
    '''Give date following Month day, Year [HR:MN:SS](TimeZone)
        -Example December 07, 2021 [11:17:25](UTC+2)'''
    now = datetime.now()
    LaDate = now.strftime("%B %d, %Y %H:%M:%S")
    LaDate=LaDate[:17]+"["+LaDate[17:]+"]"+"(UTC+2)"
    return LaDate

def Download(link):
    print("Debut de donwnload function")
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.filter(only_audio=True).first()
    directory = os.getcwd() + "/Groovy"
    if not os.path.exists(directory):
        os.makedirs(directory)
    try:
        youtubeObject.download(directory, filename="song.mp3")
        os.remove(directory + "/song.mp3")
        youtubeObject.download(directory, filename=youtubeObject.title + ".mp3")
    except:
        print("Download failed")
    print("Download complete")
    return youtubeObject.title
    


TOKEN ='TOKENVALUE'
intents = discord.Intents.all()
client = discord.Client(intents=intents)
bot = commands.Bot(command_prefix=">", intents=discord.Intents.all())

Spamcounter=bot.Spamcounter=(0)
MaxSpam=bot.MaxSpam=10
Spammessage=bot.Spammessage=[]
Spamuser=bot.Spamuser=[]
Spamchannel=bot.Spamchannel=[]
#Groovy
queues = []
queuesvalue=0


Testcase=0
DIC =	{

  "spam": [ID] ,
  "dm": [ID] ,
  "safe-room" : [ID]
}

DIC2 = {
    "SERVER1" : [ID] ,
    "SERVER2" : [ID],
    "SERVER3" : [ID]
}

HISTORY = {
    "SERVER1" : [ID] ,
    "SERVER2" : [ID],
    "SERVER3" : [ID]
}

@client.event
async def on_message(message):
    #if Testcase== 0:
    '''LOGS DE MESSAGE'''
    print(message.content,"-",message.author) #Afiche message rentre sur le serv #history
    #MAIKE HISTORY
    #print("###",message.guild.id,"\n###",DIC2["SERVER1"])
    if message.guild is not None:
        if (message.guild.id)==DIC2["SERVER1"] and not(str(message.channel)=='maike-history'):
            channel = client.get_channel(HISTORY["SERVER1"])
            response="**"+"__"+str(message.author)+"__"+"**"+" "+GiveDate()+" <#"+str(message.channel.id)+">\n"+str(message.content)
            #response=("Ca marche")
            await channel.send(response)
        
        if (message.guild.id)==DIC2["SERVER2"] and not(str(message.channel)=='maike-history'):
            channel = client.get_channel(HISTORY["SERVER2"])
            response="**"+"__"+str(message.author)+"__"+"**"+" "+GiveDate()+" <#"+str(message.channel.id)+">\n"+str(message.content)
            await channel.send(response)
        
        if (message.guild.id)==DIC2["SERVER3"] and not(str(message.channel)=='maike-history'):
            channel = client.get_channel(HISTORY["SERVER3"])
            response="**"+"__"+str(message.author)+"__"+"**"+" "+GiveDate()+" <#"+str(message.channel.id)+">\n"+str(message.content)
            await channel.send(response)
#################################################################################################################

    if message.content.casefold() == 'test' and (message.author != client.user):
        response = 'Un Deux Un Deux'
        await message.channel.send(response)
    
    if message.content == ('Un Deux Un Deux') and (message.author == client.user):
        response = '3 4 3 4'
        #Testcase+=1
        await message.channel.send(response)

    '''MP'''
    case=0
    if ('Direct Message with' in str(message.channel)):
        case=1
    if 'SoulUnison' in message.content:
        case=2   
    if case==1:
        channel = client.get_channel(701867917540851712)
        await channel.send(message.content + ' -' + str(message.author))
    #exemple "SoulUnison%Channel:XXXX%MESSAGE:XXXX%"
    #exemple SoulUnison%Channel:time-to-get-schwifty%MESSAGE: bip :ohgodohduck: Bip%
    if case==2:
        liste=[]
        a=""
        for i in str(message.content):
            if i!="%":
                a+=i
            else:
                liste.append(a)
                a=""
        chan=liste[1][8::]
        response=liste[2][8::]
        channel = client.get_channel(DIC[chan])
        await channel.send(response)
    
    #////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    if message.content == 'もう大丈夫':
        response = '私が来た'
        await message.channel.send(response)
    if message.content.casefold() == 'Re' and str(message.author)!="[BOTDISCORDTAG]":
        response = 'Re'
        await message.channel.send(response)
    if message.content.casefold() == 'wesh' in message.content and not(str(message.channel)=='generalイナスト'):
        response = "wsh la street"
        await message.channel.send(response)
    if 'bien vu' in message.content or 'bv' in message.content:
        response = 'Tkt'
        await message.channel.send(response)
    if message.content == "/type\\" or "/type\\" in message.content:
        response = 'message type=>',type(message.content),"/////","user type=>",type(message.author)
        await message.channel.send(response)
    '''Winx'''
    if message.content == 'Si tu le veux':
        response = 'Demain tu peux'
        await message.channel.send(response)
    if message.content == 'Etre avec nous':
        response = 'Winx, si tu me tiens bien la main,\nNous aurons tout les pouvoirs,\nNous battrons en forgeant notre destin!'
        await message.channel.send(response)
    '''jap'''
    if ((('Je suis japonais') in message.content) or (('je suis japonais') in message.content)):
        response = "Domo"
        await message.add_reaction("🙏")
        await message.channel.send(response)
        await message.add_reaction("🙏")
    if (message.content.casefold() == "Maike") and (message.content.casefold() == "Japonais") and not(str(message.channel)=='maike-history'):
        response = "Je suis japonais"
        await message.channel.send(response)
    if (message.content.casefold() == "domo" and not(str(message.channel)=='maike-history')) and str(message.author)!="[BOTDISCORDTAG]":
        response='Arigatou'
        await message.add_reaction("🙏")
        await message.channel.send(response)
        await message.add_reaction("🙏")


    if message.content=='POGGERS':
        #if (message.guild.id)==DIC2["SERVER1"]:
            response= '<:SAKUPOG:689648785168662677><:SAKUPOG:689648785168662677><:SAKUPOG:689648785168662677><:SAKUPOG:689648785168662677><:SAKUPOG:689648785168662677><:SAKUPOG:689648785168662677><:SAKUPOG:689648785168662677><:SAKUPOG:689648785168662677><:SAKUPOG:689648785168662677>'
            await message.channel.send(response)
    if message.content=='POG':
        #if (message.guild.id)==DIC2["SERVER1"] or (message.guild.id)==DIC2["SERVER2"]:
            await message.add_reaction('<:SAKUPOG:689648785168662677>')
    if message.content=='ono':
        #if (message.guild.id)==DIC2["SERVER1"] or (message.guild.id)==DIC2["SERVER2"]:
            response= '<:ohgodohduck:682299223336550416>'
            await message.channel.send(response)


    '''ANIMATED EMOTES'''
    if message.content.casefold() == 'Flex' in message.content:
        response = '<a:dance:534355236505255937>'
        #await message.add_reaction('<a:dance:534355236505255937>')
        await message.channel.send(response)
    if message.content.casefold() == 'Nitro' in message.content:
        await message.add_reaction('<a:dance:534355236505255937>')
    if message.content==':dance:':
        response = '<a:dance:534355236505255937>'
        await message.delete()
        await message.channel.send(response)
        await message.channel.send('|| De ' + str(message.author) + '||')


    if message.content == ('Vote,Oui/Non?'):
        await message.add_reaction("👍")
        await message.add_reaction("👎")
    if message.content == ('USER CHECK'):
        await message.channel.send("Checking...")
        if str(message.author) == str('[BOTDISCORDTAG]'):
            await message.channel.send("Maike USER CHECK")
        if str(message.author) == str('[OWNERDISCORDTAG]'):
            await message.channel.send("OWNER USER CHECK")
    ''''FONCTIONS'''
    if message.content == ('AUTEUR'):
        await message.channel.send(message.author)
    if message.content =='!channel':
        await message.channel.send(message.channel)
        await message.channel.send(type(message.channel))
        await message.channel.send('------ str : ')
        await message.channel.send(str(message.channel))
    #if message.author == [OWNERDISCORDTAG]:
    #    await message.delete()
    if message.content ==('PURGE'):
        await message.delete()
    if (('PURGE VN') in message.content) and (str(message.author) == str('[OWNERDISCORDTAG]')):
        dele=str(message.content)[8:]
        channel=message.channel
        await channel.purge(limit=int(dele)+1)

    if message.content ==('SERV-ID=? TOP SECRET XXX!'):
        await message.channel.send(message.guild.id)

    if message.content ==('Le nom du serveur ?'):
        if (message.guild.id)==DIC2["SERVER1"]:
            await message.channel.send("name is SERVER1")
        if (message.guild.id)==DIC2["SERVER2"]:
            await message.channel.send("name is SERVER2")


    '''MP''' #DM
    if message.content.casefold() == 'maike viens pv':
        await message.author.send('Yo buddy')
    '''test txt'''
    with open("MessageHistorique.txt","a") as doc:
            doc.write(str(message.content)+"MESSAGE\n")
    '''Groovy'''
    
    DocVocal='''
    ```
    To connect => Maike viens voc OR Maike vocal connect
    To disconnect => Maike casse toi du voc OR Maike vocal disconnect
    To display actual library avalaible without link => Groovy ALL
    To play => Groovy play [name] OR Groovy play [link]
    To stop => Groovy stop
    To pause/resume => Groovy pause
    To go back => Groovy back
    To go next => Groovy next
    To add add a song to queue => Groovy add [name] OR Groovy add [link]
    To display queue => Groovy queue
    To clear the queue => Groovy clear
    
    To loop the queue => Groovy loop
    ```
    '''
    
    if (message.content == 'Maike viens voc') or ('Maike vocal connect' in message.content) and str(message.author)!="[BOTDISCORDTAG]":
        channel = message.author.voice.channel
        await channel.connect()
        
    if (message.content == 'Maike casse toi du voc') or ('Maike vocal disconnect' in message.content) and str(message.author)!="[BOTDISCORDTAG]":
        await client.voice_clients[0].disconnect()
        
    if message.content.startswith('Groovy play'):
        song_name = message.content[12:]
        print(song_name)
        if song_name.startswith("http") or song_name.startswith("www."):
            file_path = Download(song_name)
            file_name = os.path.basename(file_path)
            half_file_name = file_name[:len(file_name)//2]
            song_name = half_file_name
        song_name_words = song_name.split()
        server = message.guild
        voice_channel = message.author.voice.channel
        if not message.guild.voice_client:
            vc = await voice_channel.connect()
        else:
            vc = message.guild.voice_client
            vc.stop() # stop the current playing song
        # Check if the Groovy folder exists, if not create it
        if not os.path.exists("Groovy"):
            os.makedirs("Groovy")
        # get all files in the Groovy folder
        song_paths = [f for f in os.listdir("Groovy") if os.path.isfile(os.path.join("Groovy", f))]
        matching_songs = []
        for song_path in song_paths:
            song_file_name = os.path.basename(song_path).lower()
            match_count = 0
            for word in song_name_words:
                if word in song_file_name:
                    match_count += 1
            if match_count > 0:
                matching_songs.append((match_count, os.path.join("Groovy",song_path)))
        if not matching_songs:
            await message.channel.send("No song found with name :"+song_name)
        else:
            best_match = max(matching_songs, key=lambda x: x[0])[1]
            source = discord.FFmpegPCMAudio(best_match)
            vc.play(source, after=lambda e: print('done', e))
            await message.channel.send(f'Now playing: {os.path.basename(best_match)[:-4]}')

            # Vider la liste "queues" s'il y a déjà des éléments
            if queues:
                queues.clear()

            # Ajouter la nouvelle musique à la fin de la liste "queues"
            queues.append(best_match)

    if message.content.startswith('Groovy queue'):
        if not queues:
            await message.channel.send("La file d'attente est vide.")
        else:
            queue_str = '\n'.join([queue.split('/')[-1].split('.mp3')[0] for queue in queues])
            await message.channel.send("La file d'attente actuelle est :```\n" + queue_str + "```")

    if message.content == "Groovy stop":
        vc = message.guild.voice_client
        if vc and vc.is_playing():
            vc.stop()
            await message.channel.send("THE WORLD!")
        else:
            await message.channel.send("There's nothing playing, you deaf.")

    if message.content == 'Groovy clear':
        queues.clear()
        queuesvalue = 0
        await message.channel.send(f'Queue:\n```{queues}```')

    if message.content == 'Groovy ALL':
        # Check if the Groovy folder exists
        if not os.path.exists("Groovy"):
            await message.channel.send("No Groovy folder found.")
        else:
            # get all files in the Groovy folder
            song_paths = [f for f in os.listdir("Groovy") if os.path.isfile(os.path.join("Groovy", f))]
            songs = '\n'.join([os.path.splitext(song)[0] for song in song_paths])
            await message.channel.send(f'Songs in Groovy folder:\n```{songs}```')

    if message.content.startswith('Groovy add'):
        song_name = message.content[11:]
        print(song_name)
        if song_name.startswith("http") or song_name.startswith("www."):
            file_path = Download(song_name)
            file_name = os.path.basename(file_path)
            half_file_name = file_name[:len(file_name)//2]
            song_name = half_file_name
        song_name_words = song_name.split()
        # Check if the Groovy folder exists, if not create it
        if not os.path.exists("Groovy"):
            os.makedirs("Groovy")
        # get all files in the Groovy folder
        song_paths = [f for f in os.listdir("Groovy") if os.path.isfile(os.path.join("Groovy", f))]
        matching_songs = []
        for song_path in song_paths:
            song_file_name = os.path.basename(song_path).lower()
            match_count = 0
            for word in song_name_words:
                if word in song_file_name:
                    match_count += 1
            if match_count > 0:
                matching_songs.append((match_count, os.path.join("Groovy",song_path)))
        if not matching_songs:
            await message.channel.send("No song found with name :"+song_name)
        else:
            best_match = max(matching_songs, key=lambda x: x[0])[1]
            queues.append(best_match)
            await message.channel.send(f'Song added to queue: {os.path.basename(best_match)[:-4]}')

    if message.content.startswith('Groovy pause'):
        vc = message.guild.voice_client
        if vc.is_playing():
            vc.pause()
            await message.channel.send("時よ！止まれ！")
        else:
            vc.resume()
            await message.channel.send("時が動く。")

###marche avant tout ca
    if message.content.startswith('Groovy back'):
        if not queues:
            await message.channel.send("La file d'attente est vide.")
        else:
            queuesvalue -= 1 # décrémenter l'index de la liste de musiques
            if queuesvalue < 0:
                queuesvalue = len(queues) - 1 # revenir à la dernière musique
            source = discord.FFmpegPCMAudio(queues[queuesvalue])
            vc.play(source, after=lambda e: print('done', e))
            await message.channel.send(f'Maintenant en train de jouer: {queues[queuesvalue].split("/")[-1][:-4]}')


    if message.content.startswith('Groovy next'):
        if not queues:
            await message.channel.send("La file d'attente est vide.")
        else:
            queuesvalue += 1
            if queuesvalue == len(queues):
                queuesvalue = 0
                await message.channel.send("La file d'attente est terminée.")
            else:
                source = discord.FFmpegPCMAudio(queues[queuesvalue])
                vc.play(source, after=lambda e: print('done', e))
                await message.channel.send(f'Now playing: {os.path.basename(queues[queuesvalue])[:-4]}')

    if message.content.startswith('Groovy loop'):
        server = message.guild
        if server.id in players:
            player = players[server.id]
            if player.is_playing():
                player.loop = not player.loop
                if player.loop:
                    await message.channel.send("Queue loop enabled.")
                else:
                    await message.channel.send("Queue loop disabled.")
            else:
                await message.channel.send("There is no song playing.")
        else:
            await message.channel.send("There is no song playing.")

        
    if message.content == 'man voc Maike':
        response=DocVocal
        await message.channel.send(response)
        

    '''ROLES'''
    '''Done le role principal'''
    '''SERVER1 VER'''
    if  (message.content.casefold() == "![value]" in message.content)) and (str(message.channel)=='safe-room') and (message.guild.id)==DIC2["SERVER2"]:

        guild = message.author.guild
        role = discord.utils.get(guild.roles, name="They")
        await message.author.add_roles(role)
        await message.delete()
    '''SERVER3 VER'''
    if  (message.content.casefold() == "![value]" in message.content) and (str(message.channel)=='safe-room') and (message.guild.id)==DIC2["SERVER3"]:
        guild = message.author.guild
        role = discord.utils.get(guild.roles, name="They")
        await message.author.add_roles(role)
        await message.delete()
    '''Mute Command'''
    if ("Mute " in message.content) and (str(message.author) == str('[OWNERDISCORDTAG]')):
        if (message.guild.id)==DIC2["SERVER2"]:
            guild = client.get_guild(DIC2["SERVER2"])
        if (message.guild.id)==DIC2["SERVER3"]:
            guild = client.get_guild(DIC2["SERVER3"])
        Lui=str(message.content)[7::]
        Lui=Lui.replace('@','');Lui=Lui.replace('!','');Lui=Lui.replace('<','');Lui=Lui.replace('>','')
        Lui=int(Lui)
        member=guild.get_member(Lui)
        role = discord.utils.get(guild.roles, name='TG/SHUT UP')
        await member.add_roles(role)
        role = discord.utils.get(guild.roles, name='They')
        await member.remove_roles(role)

    '''Unmute command'''
    if ("Unmute " in message.content) and (str(message.author) == str('[OWNERDISCORDTAG]')):
        if (message.guild.id)==DIC2["SERVER2"]:
            guild = client.get_guild(DIC2["SERVER2"])
        if (message.guild.id)==DIC2["SERVER3"]:
            guild = client.get_guild(DIC2["SERVER3"])
        Lui=str(message.content)[7::]
        Lui=Lui.replace('@','');Lui=Lui.replace('!','');Lui=Lui.replace('<','');Lui=Lui.replace('>','')
        Lui=int(Lui)
        member=guild.get_member(Lui)
        role = discord.utils.get(guild.roles, name="TG/SHUT UP")
        await member.remove_roles(role)
        role = discord.utils.get(guild.roles, name="They")
        await member.add_roles(role)
        
    '''SECURITY'''
    #GIVE TG/SHUT UP Tag to everyone and thus mute them
    if (('DISCORD ROOM !') == message.content) and (str(message.author) == str('[OWNERDISCORDTAG]')):
        if (message.guild.id)==DIC2["SERVER2"]:
            channel = client.get_channel([announcements channel ID]) #announcements  
            response="SECURITY ACTIVATING ! PLEASE WAIT ..."
            guild = client.get_guild(DIC2["SERVER2"])
            await channel.send(response)
        if (message.guild.id)==DIC2["SERVER3"]:
            channel = client.get_channel([announcements channel ID]) #announcements 
            response="SECURITY ACTIVATING ! PLEASE WAIT ..."
            guild = client.get_guild(DIC2["SERVER3"])
            await channel.send(response)
        memberList = guild.members
        for i in (memberList):
            role = discord.utils.get(guild.roles, name="TG/SHUT UP")
            await i.add_roles(role)
            role = discord.utils.get(guild.roles, name="They")
            await i.remove_roles(role)
            print(i,"done")
        response="SECURITY ACTIVATED !"
        await channel.send(response)

    if (('REMOVE DISCORD ROOM !') == message.content) and (str(message.author) == str('[OWNERDISCORDTAG]')):
        if (message.guild.id)==DIC2["SERVER2"]:
            channel = client.get_channel([announcements channel ID]) #announcements
            response="SECURITY DISABLING ! PLEASE WAIT ..."
            guild = client.get_guild(DIC2["SERVER2"])
            await channel.send(response)
        if (message.guild.id)==DIC2["SERVER3"]:
            channel = client.get_channel([announcements channel ID]) #announcements
            response="SECURITY DISABLING ! PLEASE WAIT ..."
            guild = client.get_guild(DIC2["SERVER3"])
            await channel.send(response)
        memberList = guild.members
        for i in (memberList):
            role = discord.utils.get(guild.roles, name="TG/SHUT UP")
            await i.remove_roles(role)
            if not(str(i)=="Groovy#7254") and not(str(i)=="Smoogle Translate#1934") and not(str(i)=="Wiki-Bot#2998") and not(str(i)=="DISBOARD#2760"): # c'etait pas des or
                role = discord.utils.get(guild.roles, name="They")
                await i.add_roles(role)
            print(i,"done")
        response="SECURITY DISABLED !"
        await channel.send(response)

    
    if (('!HAKAI') in message.content) and (str(message.author) == str('[OWNERDISCORDTAG]')):
        if (message.guild.id)==DIC2["SERVER2"]:
            guild = client.get_guild(DIC2["SERVER2"])
        if (message.guild.id)==DIC2["SERVER3"]:
            guild = client.get_guild(DIC2["SERVER3"])
        memberList = guild.members
        a=sorted(memberList,key=lambda m: m.joined_at,reverse=True)
        bannumb=str(message.content)[7:]
        for q in range(int(bannumb)):
            await (a[q]).ban(reason="Hakai",delete_message_days=7)

    '''SINGLE BAN AND UNBAN'''
    if ("Ok; ban " in message.content) and (str(message.author) == str('[OWNERDISCORDTAG]')):
        if (message.guild.id)==DIC2["SERVER2"]:
            guild = client.get_guild(DIC2["SERVER2"])
        if (message.guild.id)==DIC2["SERVER3"]:
            guild = client.get_guild(DIC2["SERVER3"])
        Lui=str(message.content)[9::]
        Lui=Lui.replace('@','');Lui=Lui.replace('!','');Lui=Lui.replace('<','');Lui=Lui.replace('>','')
        Lui=int(Lui)
        member=guild.get_member(Lui)
        await member.ban(reason="Banned from ban command",delete_message_days=7)
        response=str(member)+" Has been banned"
        await message.channel.send(response)

    '''BAN A ROLE'''
    if message.content=="!Ban muted" and (str(message.author) == str('[OWNERDISCORDTAG]')): #Ban Mute role
        if (message.guild.id)==DIC2["SERVER2"]:
            guild = client.get_guild(DIC2["SERVER2"])
        if (message.guild.id)==DIC2["SERVER3"]:
            guild = client.get_guild(DIC2["SERVER3"])
        else:
            guild = client.get_guild(DIC2["SERVER1"])
        role = discord.utils.get(guild.roles, name="TG/SHUT UP")
        usernames = [m.id for m in role.members]
        for i in usernames:
            member=guild.get_member(i)
            print(str(member))
            await member.ban(reason="Banned from muted role(Spam?)",delete_message_days=7)

    '''SPAM SECURITY'''
    
    if str(message.author)!="[BOTDISCORDTAG]":
        Spammessage.append(str(message.content))
        Spamuser.append(message.author)
    
    if len(Spammessage)==MaxSpam:
        if len(set(Spammessage))==1 and len(set(Spamuser))==1 :# and len(set(Spamchannel)):
            await message.channel.send("Attention tu spam BATARD")
            if (message.guild.id)==DIC2["SERVER2"]:
                guild = client.get_guild(DIC2["SERVER2"])
            if (message.guild.id)==DIC2["SERVER3"]:
                guild = client.get_guild(DIC2["SERVER3"])
            role = discord.utils.get(guild.roles, name="TG/SHUT UP")
            await Spamuser[0].add_roles(role)
            role = discord.utils.get(guild.roles, name="They")
            await Spamuser[0].remove_roles(role)
            Spammessage.clear()
            Spamuser.clear()
            Spamchannel.clear()
    if len(Spammessage)==MaxSpam:
        Spammessage.clear()
        Spamuser.clear()
        Spamchannel.clear()

    '''DOC DE MAIKE'''

    LaDoc='''
        #2 #test OR Test : Answer 'Un Deux Un Deux'
        #3 #Un Deux Un Deux : Answer '3 4 3 4'
        #? #もう大丈夫 Answer 
        #4 #SoulUnison : Send a Message in a specific channel using Maike
            -Example "SoulUnison%Channel:XXXX%MESSAGE:XXXX%"
            -Example SoulUnison%Channel:time-to-get-schwifty%MESSAGE: bip :ohgodohduck: Bip%
        #? #Re OR re : Answer 'Re'
        #? #Wesh OR wesh : Answer 'wsh la street'
        #? #bien vu OR bv : Answer 'Tkt'
        #? #/Type\ :Return the message type 
            -Example ('message type=>', <class 'str'>, '/////', 'user type=>', <class 'discord.member.Member'>)
        #Winx
        #? #Si tu le veux Answer 'Demain tu peux'
        #? #Etre avec nous Answer 'Winx, si tu me tiens bien la main,\nNous aurons tout les pouvoirs,\nNous battrons en forgeant notre destin!'
        
        
        #? #Je suis japonais OR je suis japonais : Answer 'Domo' AND react "🙏"
        #? #Maike OR maike AND japonais or Japonais : Answer "Je suis japonais"
        #? #Domo or Domo AND Author is Maike : Answer 'Arigatou'
        #? #man Maike : Send Maike's documentation


        SERVER1 ONLY
        #? #POGGERS : Answer 9 SAKUPOG emotes
        #? #POG : React with a SUKPOG
        #? #ono : Answer ohgodohduck emote
        #? #flex OR Flex : Answer dance animated emote
        #? #Nitro OR nitro : React with dance animated emote
        #? #:dance: Delete author's message and Answer the dance animated emote with the author's name
        #? #Vote,Oui/Non? add "👍" and "👎" to the message
        #? #USER CHECK : Answer Checking... USER USER CHECk
            only works for OWNER and MAIKE
        #? #AUTEUR : Anwser the User's Username and tag
            -Example [OWNERDISCORDTAG]
        #? #!channel : Answer Channel Name
                            Channel Type
                            '------ str : '
                            Channel Name into a string
        #? #PURGE : Delete the message
        #? #'SERV-ID=? TOP SECRET XXX!' : Answer the server's ID
            -Example 793490627396708365
        #? #Le nom du serveur ? : Answer the server's name
            only works for SERVER1 and SERVER1
        #? #Maike viens pv OR maike viens pv : Make Maike DM 'Yo buddy to someone'
    

        SUPERUSER COMMANDS (Que OWNER pour l'instant !)
        #? #PURGE VNXXX : Delete XXX(Number) of messages above one's message
            -Example PURGE VN5
        #? #Mute @SOMEONE : Mute the taged person(Removing the "They" role and giving it "TG/SHUT UP")
            only works on SERVER1Inazuma server
            -Example Mute @Tannard
        #? #Unmute @SOMEONE : Unmute the taged person(Removing the "TG/SHUT UP" role and giving it "They")
            only works on SERVER1Inazuma server
            -Example Unmute @Tannard
        #? #DISCORD ROOM ! : Mute everyone and send ""SECURITY ACTIVATING ! PLEASE WAIT ..." in announcements.When everyone is muted it will send "SECURITY ACTIVATED !" in announcements
        #? #REMOVE DISCORD ROOM ! :Unmute everyone and send "SECURITY DISABLING ! PLEASE WAIT ..." in announcements and send "SECURITY DISABLED !" when everyone is Unmuted
        #? #Ok; ban @SOMEONE : Ban the taged person
        #? #!Ban muted Ban all the muted 
        #? #!HAKAI XXX : Ban XXX latest members
            -Example !HAKAI 5


        SERVER1 RELATED
        #? #![value] OR ![value] or jack in!(Flated): Give "They" role (And delete the message)
            -only works in safe-room
    '''
    '''Display le manuel de Maike'''
    if "man Maike" == message.content:
        p1 = LaDoc[:len(LaDoc)//2]
        p2 = LaDoc[len(LaDoc)//2:]
        response=p1
        await message.channel.send(response)
        response=p2
        await message.channel.send(response)


###################################################################################

'''PING TOUT LES X temps'''
#SecTime=60 #3660

@tasks.loop(minutes=360) #6h
async def PING():
    channel = client.get_channel([PINGCHANNELID])
    LePing="PING du "+GiveDate()
    await channel.send(LePing)

#####################################################################################

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print(GiveDate())
    print('------')


    game = discord.Game("Updating...")
    listen=discord.Activity(type=discord.ActivityType.listening, name="Updating...")
    await client.change_presence(status=discord.Status.online,activity=listen)
    PING.start()

client.run(TOKEN)