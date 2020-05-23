import discord,asyncio,random, urllib, bs4, time
from urllib.request import urlopen, Request
import urllib.request
from selenium import webdriver
import os,sys,json
from discord.ext import commands
import soup
import youtube_dl
import openpyxl
import json
import os
import sys
import setting
from discord.ext import commands
from discord.utils import get
import requests
import unicodedata
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen
from urllib.request import Request, urlopen
from urllib.parse import quote
import re
import warnings



countG = 0
players = {}
queues= {}
musiclist=[]
mCount=1
searchYoutube={}
searchYoutubeHref={}

a = setting.a
b = setting.b
client = commands.Bot(command_prefix='$$')
calcResult = 0

def BotNameAndStat(**kwargs):
    for n in kwargs.keys():
        print("%s's Development Progress : %s" % (n, kwargs[n]))

def check_queue(id):
    if queues[id]!=[]:
        player = queues[id].pop(0)
        players[id] = player
        del musiclist[0]
        player.start()


uptime = time.time()
embed = discord.Embed
admin = '682524312858656789'

def info():
    end = time.time()-uptime
    ut = int(end)
    min = int(ut/60)
    hour = int(min/60)
    day = str(int(hour/60))
    hour = str(hour%24)
    ut = str(ut%60)
    min = str(min%60)
    e = embed(title='초롱봇 정보',description="개발자: 초롱이#3632\n업타임:"+day+"일 "+hour+"시간 "+min+"분 "+ut+"초 ", colour=0xffc0cb)
    e.set_thumbnail(url='https://images-ext-2.discordapp.net/external/-yi7BQbZeWDKMkFPL0fCA2T4mFQRoWd-Hc9AIkSfefc/%3Fsize%3D1024/https/cdn.discordapp.com/avatars/688918373203050581/ff5c7a93cd68fff81c64267a382af76c.webp?width=468&height=468')
    return e

@client.event
async def on_ready():

    print(client.user.name)
    print(client.user.id)
    server = len(client.guilds)
    users = 0
    for now_guild in client.guilds:
        users = users + len(now_guild.members)
    while True:
        await client.change_presence(status=discord.Status.online, activity=discord.Game('`초롱아 도움`을 입력하세요!'))
        await asyncio.sleep(10)
        await client.change_presence(status=discord.Status.online, activity=discord.Game(str(server)+'개의 서버 | '+str(users)+'명의 유저'))
        await asyncio.sleep(10)
        await client.change_presence(status=discord.Status.online, activity=discord.Game('개발중인 봇이라 불안정함'))
        await asyncio.sleep(10)

@client.event
async def on_message(message):
    await client.process_commands(message)
    
    if message.author.bot:
        return None


    if message.content.startswith("초롱아 도움"):
        embed=discord.Embed(title='초롱봇V3 기능', description='초롱봇 V3의 기능은 아래 웹사이트에서 확인하실수 있습니다.', color=0xffc0cb)
        embed.add_field(name='초롱봇V3 소개 및 명령어 보기', value='[초롱봇V3 소개 및 명령어](<https://park2825.github.io/cholongbot/index.html>)', inline=False)
        
        
        embed.set_footer(text="발신자 : %s#%s" % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("초롱아 강아지"):
        embed=discord.Embed(title='강아지는', description='야옹야옹', color=0xffc0cb)
        urlBase = 'https://loremflickr.com/320/240/dog?lock='
        randomNum=random.randrange(1, 30977)
        urlF=urlBase+str(randomNum)
        embed.set_image(url=urlF)
        embed.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("초롱아 고양이"):
        embed=discord.Embed(title='고양이는', description='왈왈', color=0xffc0cb)
        urlmain = 'https://loremflickr.com/320/240/cat?lock='
        randomimg=random.randrange(1, 30977)
        urlN=urlmain+str(randomimg)
        embed.set_image(url=urlN)
        embed.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "초롱아 프사":
        embed=discord.Embed(title='당신의 프사', description='회원님의 프사는', color=0xffc0cb)
        embed.set_image(url=message.author.avatar_url)
        embed.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("초롱아 프사 "):
        e = discord.Embed(title='맨션한 회원님의 프사', description='맨션한 사용자의 프로필 입니다.', color=0xffc0cb)
        if not message.mentions:
            e = discord.Embed(title='오류!', description='맨션을 하지 않으셨습니다.', color=0xff0000)
            e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
            await message.channel.send(embed=e)
        else:
            user = message.mentions[0]
            e.set_image(url=user.avatar_url)
            e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
            await message.channel.send(embed=e)

    if message.content.startswith("초롱아 정보"):
        e = info()
        e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)

    if message.content.startswith("초롱아 날씨"):
        lean = message.content.split("초롱아 날씨 ")
        location = lean[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'user-Agent': 'Mozila/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=l&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()
        print(todayTemp)

        todayvalueBase = todayBase.find('ul', {'class': 'info_list'})
        todayvalue2 = todayvalueBase.find('p', {'class': 'cast_txt'})
        todayvalue = todayvalue2.text.strip()
        print(todayvalue)

        todayFeelingTemp1 = todayvalueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

        e = discord.Embed(title='오늘 '+lean[1]+'의 날씨', description=lean[1]+'의 날씨입니다.', color=0xffc0cb)
        e.add_field(name='현재온도', value=todayTemp+'*', inline=False)
        e.add_field(name='체감온도', value=todayFeelingTemp, inline=False)
        e.add_field(name='현재상태', value=todayvalue, inline=False)
        e.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)
        e.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)
        e.add_field (name='**----------------------------------**',value='**----------------------------------**', inline=False)
        e.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
        e.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        e.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        e.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태
        e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
    
    if message.content.startswith('초롱아 골라 '):
        tmp = message.content.split('초롱아 골라 ')[1]
        ans = random.choice(tmp.split('/'))
        e = discord.Embed(title='초롱봇은 이걸 선택하겠다.', description=ans, color=0xffc0cb)
        e.set_footer(text="사용자: %s#%s" % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)

    if message.content.startswith('초롱아 따라해 '):
        ans = message.content.split('초롱아 따라해')[1]
        await message.channel.send(ans)
    
    if message.content.startswith('초롱아 확률 '):
        ans = str(random.randrange(0,100))
        q = message.content.split('초롱아 확률')[1]
        e = discord.Embed(title=q+'은?', description=ans+'%이다.', color=0xffc0cb)
        e.set_footer(text="사용자: %s#%s" % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
    '''
    if message.content.startswith('초롱아 나무위키 '):
        msg = await message.channel.send('검색중...')
        m = message.content[6:]
        ans = soup.namu(m)
        await msg.delete()
        if not ans:
            e = discord.Embed(title = '오류',description = '나무위키에 없는 문서입니다',color=0xF44336)
            await message.channel.send(embed=e)
        else:
            e = discord.Embed(title = m+" 검색결과",color=0x00A495)
            e.add_field(name = '내용',value = ans)
            e.set_footer(text='namu.wiki 나무위키')
            await message.channel.send(embed=e)
            '''

    if message.content == "초롱아 멜론":
        ms = await message.channel.send('차트를 확인중입니다...')
        e = discord.Embed(title='멜론 TOP10', description='멜론 10위를 불러온다', color=0xffc0cb)
        ans = soup.Melon()

        for i in range(10):
            e.add_field(name=i+1, value = ans.b[i].text+' - '+ans.tag[i].text, inline=False)
            e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await ms.delete()
        await message.channel.send(embed=e)

    if message.content.startswith("초롱아 롤"):
        learn = message.content.split("초롱아 롤 ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)

        url = "http://www.op.gg/summoner/userName=" + enc_location
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        rank1 = bsObj.find("div", {"class": "TierRankInfo"})
        rank2 = rank1.find("div", {"class": "TierRank"})
        rank4 = rank2.text  # 티어표시 (브론즈1,2,3,4,5 등등)
        print(rank4)
        if rank4 != 'Unranked':
          jumsu1 = rank1.find("div", {"class": "TierInfo"})
          jumsu2 = jumsu1.find("span", {"class": "LeaguePoints"})
          jumsu3 = jumsu2.text
          jumsu4 = jumsu3.strip()#점수표시 (11LP등등)
          print(jumsu4)

          winlose1 = jumsu1.find("span", {"class": "WinLose"})
          winlose2 = winlose1.find("span", {"class": "wins"})
          winlose2_1 = winlose1.find("span", {"class": "losses"})
          winlose2_2 = winlose1.find("span", {"class": "winratio"})

          winlose2txt = winlose2.text
          winlose2_1txt = winlose2_1.text
          winlose2_2txt = winlose2_2.text #승,패,승률 나타냄  200W 150L Win Ratio 55% 등등

          print(winlose2txt + " " + winlose2_1txt + " " + winlose2_2txt)

        e=discord.Embed(title=learn[1]+'님의 롤 정보', description=learn[1]+'님의 롤 정보입니다.', color=0xffc0cb)

        if rank4=='Unranked':
            e.add_field(name=learn[1]+'님의 티어', value=rank4, inline=False)
            e.add_field(name=learn[1]+'님은 언랭', value='언랭은 더이성 정보를 제공하지 않습니다.', inline=False)
            await message.channel.send(embed=e)
        else:
            e.add_field(name=learn[1]+'님의 티어', value=rank4, inline=False)
            e.add_field(name=learn[1]+'님의 LP(점수)', value=jumsu4, inline=False)
            e.add_field(name=learn[1]+'님의 승패 정보', value=winlose2txt+" "+winlose2_1txt, inline=False)
            e.add_field(name=learn[1]+'님의 승률', value=winlose2_2txt, inline=False)
            e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
            await message.channel.send(embed=e)

    if message.content.startswith("초롱아 배그솔로"):
        learn = message.content.split('초롱아 배그솔로 ')
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/"+enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        solo1 = bsObj.find("div", {"class": "overview"})
        solo2 = solo1.text
        solo3 = solo2.strip()

        e=discord.Embed(title=learn[1]+'님의 배그솔로 전적', description=learn[1]+'님의 배그솔로 전적입니다.', color=0xffc0cb)
        if solo3 == "No record":
            print("솔로 경기가 없습니다.")
            e.add_field(name=learn[1]+'님 배그를 한판이라도 플레이 해주세요', value=learn[1]+'님은 솔로 경기를 안하셨습니다.', color=0xffc0cb)
            await message.channel.send(embed=e)
        else:
            solo4 = solo1.find("span", {"class": "value"})
            soloratting = solo4.text
            solorank0_1 = solo1.find("div", {"class": "grade-info"})
            solorank0_2 = solorank0_1.text
            solorank = solorank0_2.strip()

            print("레이팅 : " + soloratting)
            print("등급 : " + solorank)
            print("")
            e.add_field(name='레이팅', value=soloratting, inline=False)
            e.add_field(name='등급', value=solorank, inline=False)

            soloKD1 = bsObj.find("div", {"class": "kd stats-item stats-top-graph"})
            soloKD2 = soloKD1.find("p", {"class": "value"})
            soloKD3 = soloKD2.text
            soloKD = soloKD3.strip()  # -------킬뎃(2.0---------
            soloSky1 = soloKD1.find("span", {"class": "top"})
            soloSky2 = soloSky1.text  # -------상위10.24%---------

            print("킬뎃 : " + soloKD)
            print("킬뎃상위 : " + soloSky2)
            print("")
            e.add_field(name='킬뎃, 킬뎃상위', value=soloKD+" "+soloSky2, inline=False)
            e.add_field(name='킬뎃상위', value=soloSky2, inline=False)

            soloWinRat1 = bsObj.find("div", {"class": "stats"})  # 박스
            soloWinRat2 = soloWinRat1.find("div", {"class": "winratio stats-item stats-top-graph"})
            soloWinRat3 = soloWinRat2.find("p", {"class": "value"})
            soloWinRat = soloWinRat3.text.strip()  # -------승률---------
            soloWinRatSky1 = soloWinRat2.find("span", {"class": "top"})
            soloWinRatSky = soloWinRatSky1.text.strip()  # -------상위?%---------
            e.add_field(name='승률, 승률상위', value=soloWinRat+" "+soloWinRatSky, inline=False)
            e.add_field(name='승률상위', value=soloWinRatSky, inline=False)

            soloHead1 = soloWinRat1.find("div", {"class": "headshots stats-item stats-top-graph"})
            soloHead2 = soloHead1.find("p", {"class": "value"})
            soloHead = soloHead2.text.strip()  # -------헤드샷---------
            soloHeadSky1 = soloHead1.find("span", {"class": "top"})
            soloHeadSky = soloHeadSky1.text.strip()  # # -------상위?%---------

            print("헤드샷 : " + soloHead)
            print("헤드샷상위 : " + soloHeadSky)
            print("")
            e.add_field(name='헤드샷, 헤드샷상위', value=soloHead+" "+soloHeadSky, inline=False)
            e.add_field(name='헤드샷상위', value=soloHeadSky, inline=False)
            e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
            await message.channel.send(embed=e)

    if message.content.startswith("초롱아 배그듀오"):
        learn = message.content.split("초롱아 배그듀오 ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/" + enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        duoCenter1 = bsObj.find("section", {"class": "duo modeItem"})
        duoRecord1 = duoCenter1.find("div", {"class": "overview"})
        duoRecord = duoRecord1.text.strip()  # ----기록이없습니다 문구----
        print(duoRecord)
        
        e=discord.Embed(title=learn[1]+'님의 배그 듀오 전적', description=learn[1]+'님의 배그 듀오 전적입니다.', color=0xffc0cb)
        if duoRecord == 'No record':
            print(learn[1]+'님의 듀오 전적이 없습니다.')
            e.add_field(name=learn[1]+'님 배그 듀오를 한판이라도 플레이 해주세요.', value=learn[1]+'님의 배그 듀오 전적이 없습니다.')
            await message.channel.send(embed=e)
        else:
            duoRat1 = duoRecord1.find("span", {"class": "value"})
            duoRat = duoRat1.text.strip()
            duoRank1 = duoRecord1.find("p", {"class": "grade-name"})
            duoRank = duoRank1.text.strip()
            print(duoRank)
            e.add_field(name='레이팅', value=duoRat, inline=False)
            e.add_field(name='등급', value=duoRank, inline=False)


            duoStat = duoCenter1.find("div", {"class": "stats"})

            duoKD1 = duoStat.find("div", {"class": "kd stats-item stats-top-graph"})
            duoKD2 = duoKD1.find("p", {"class": "value"})
            duoKD = duoKD2.text.strip()
            duoKdSky1 = duoStat.find("span", {"class": "top"})
            duoKdSky = duoKdSky1.text.strip()
            print(duoKD)
            print(duoKdSky)
            e.add_field(name='킬뎃,킬뎃상위', value=duoKD+" "+duoKdSky, inline=False)

            duoWinRat1 = duoStat.find("div", {"class": "winratio stats-item stats-top-graph"})
            duoWinRat2 = duoWinRat1.find("p", {"class": "value"})
            duoWinRat = duoWinRat2.text.strip()
            duoWinRatSky1 = duoWinRat1.find("span", {"class": "top"})
            duoWinRatSky = duoWinRatSky1.text.strip()
            print(duoWinRat)
            print(duoWinRatSky)
            e.add_field(name='승률,승률상위', value=duoWinRat + " " + duoWinRatSky, inline=False)

            duoHead1 = duoStat.find("div", {"class": "headshots"})
            duoHead2 = duoHead1.find("p", {"class": "value"})
            duoHead = duoHead2.text.strip()
            duoHeadSky1 = duoHead1.find("span", {"class": "top"})
            duoHeadSky = duoHeadSky1.text.strip()
            print(duoHead)
            print(duoHeadSky)
            e.add_field(name='헤드샷,헤드샷상위', value=duoHead + " " + duoHeadSky, inline=False)
            e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
            await message.channel.send(embed=e)

    if message.content.startswith("초롱아 배그스쿼드"):
        learn = message.content.split("초롱아 배그스쿼드 ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://dak.gg/profile/" + enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        duoCenter1 = bsObj.find("section", {"class": "squad modeItem"})
        duoRecord1 = duoCenter1.find("div", {"class": "overview"})
        duoRecord = duoRecord1.text.strip()  # ----기록이없습니다 문구----
        print(duoRecord)

        e=discord.Embed(title=learn[1]+'님의 배그스쿼드 전적', description=learn[1]+'님의 배그스쿼드 전적입니다.', color=0xffc0cb)

        if duoRecord == 'No record':
            print('스쿼드 경기가 없습니다.')
            e.add_field(name=learn[1]+'님 배그스쿼드를 한판이라도 플레이 해주세요', value=learn[1]+'님의 배그 전적이 없습니다.', inline=False)
            await message.channel.send(embed=e)
        else:
            duoRat1 = duoRecord1.find("span", {"class": "value"})
            duoRat = duoRat1.text.strip()  # ----레이팅----
            duoRank1 = duoRecord1.find("p", {"class": "grade-name"})
            duoRank = duoRank1.text.strip()  # ----등급----
            print(duoRank)
            e.add_field(name='레이팅', value=duoRat, inline=False)
            e.add_field(name='등급', value=duoRank, inline=False)


            duoStat = duoCenter1.find("div", {"class": "stats"})

            duoKD1 = duoStat.find("div", {"class": "kd stats-item stats-top-graph"})
            duoKD2 = duoKD1.find("p", {"class": "value"})
            duoKD = duoKD2.text.strip()  # ----킬뎃----
            duoKdSky1 = duoStat.find("span", {"class": "top"})
            duoKdSky = duoKdSky1.text.strip()  # ----킬뎃 상위?%----
            print(duoKD)
            print(duoKdSky)
            e.add_field(name='킬뎃,킬뎃상위', value=duoKD+" "+duoKdSky, inline=False)

            duoWinRat1 = duoStat.find("div", {"class": "winratio stats-item stats-top-graph"})
            duoWinRat2 = duoWinRat1.find("p", {"class": "value"})
            duoWinRat = duoWinRat2.text.strip()  # ----승률----
            duoWinRatSky1 = duoWinRat1.find("span", {"class": "top"})
            duoWinRatSky = duoWinRatSky1.text.strip()  # ----승률 상위?%----
            print(duoWinRat)
            print(duoWinRatSky)
            e.add_field(name='승률,승률상위', value=duoWinRat + " " + duoWinRatSky, inline=False)

            duoHead1 = duoStat.find("div", {"class": "headshots"})
            duoHead2 = duoHead1.find("p", {"class": "value"})
            duoHead = duoHead2.text.strip()  # ----헤드샷----
            duoHeadSky1 = duoHead1.find("span", {"class": "top"})
            duoHeadSky = duoHeadSky1.text.strip()  # ----헤드샷 상위?%----
            print(duoHead)
            print(duoHeadSky)
            e.add_field(name='헤드샷,헤드샷상위', value=duoHead + " " + duoHeadSky, inline=False)
            e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
            await message.channel.send(embed=e)

    if message.content.startswith('초롱아 코로나'):
        url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98"
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")

        main1 = bsObj.find("div", {"class":"circle red level5"})
        main2 = main1.find("strong", {"class":"num"})
        main3 = main2.text

        main4 = bsObj.find("div", {"class":"circle blue level5"})
        main5 = main4.find("strong", {"class":"num"})
        main6 = main5.text

        main7 = bsObj.find("div", {"class":"circle orange level5"})
        main8 = main7.find("strong", {"class":"num"})
        main9 = main8.text

        main10 = bsObj.find("div", {"class":"circle black level3"})
        main11 = main10.find("strong", {"class":"num"})
        main12 = main11.text

        e = discord.Embed(title='국내 COVID-19(코로나) 현황', description='대한민국 COVID-19(코로나) 현황입니다.', color=0xffc0cb)
        e.add_field(name='확진자', value=main3+'명', inline=False)
        e.add_field(name='격리해제', value=main6+'명', inline=False)
        e.add_field(name='검사진행', value=main9+'명', inline=False)
        e.add_field(name='사망자', value=main12+'명', inline=False)
        e.set_footer(text='확인자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)



    if message.content == '초롱아 서버':
        e = discord.Embed(title='초롱봇이 가입된 서버', description='초롱봇은 이런서버에 가입되어 있어요.', color=0xffc0cb)
        for i,s in enumerate(client.guilds):
            e.add_field(name=i+1, value=s.name, inline=False)
            e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
    for i in range(0,2):
        if message.content == a[i]:
            await message.channel.send(random.choice(b[i]))

    if message.content.startswith('초롱아 복권'):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                
            count = count + 1
            Text = Text + " " + str(number[i])
        print(Text.strip())
        e = discord.Embed(title='복권 숫자', description='로또 랜덤 번호이다.', color=0xffc0cb)
        e.add_field(name='랜덤 로또 번호이다.', value=Text.strip(), inline=False)
        e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)

    if message.content.startswith("초롱아 단어"):
        learn = message.content.split("초롱아 단어 ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://stdict.korean.go.kr/search/searchResult.do?pageSize=10&searchKeyword="+enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")

        word1 = bsObj.find("a", {"class":"t_blue1"})
        word2 = word1.text
        
        mean1 = bsObj.find("font", {"class":"dataLine"})
        mean2 = mean1.text
        print(word2 + mean2)

        e=discord.Embed(title=learn[1]+'의 단어뜻', description=learn[1]+'의 단어뜻 입니다.', color=0xffc0cb)
        e.add_field(name=word2, value=mean2, inline=False)
        e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)

    if message.content.startswith("초롱아 전화번호"):
        learn = message.content.split("초롱아 전화번호 ")
        location = learn[1]
        enc_location = urllib.parse.quote(location)
        url = "https://search.naver.com/search.naver?sm=top_hty&fbm=1&ie=utf8&query="+enc_location
        html = urllib.request.urlopen(url)
        bsObj = bs4.BeautifulSoup(html, "html.parser")

        callnumber1 = bsObj.find("div", {"class":"txt"})
        callnumber2 = callnumber1.text

        e = discord.Embed(title=learn[1]+'의 전화번호', descripiton=learn[1]+'의 전화번호입니다.', color=0xffc0cb)
        e.add_field(name=learn[1]+' 전화번호', value=callnumber2, inline=False)
        e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)
    
    if message.content.startswith("초롱아 핑"):
        ping = client.latency
        e = discord.Embed(title='퐁!', description='핑! 퐁!', color=0xffc0cb)
        e.add_field(name='당신의 핑', value=str(round(ping*1000))+'ms', inline=False)
        e.set_footer(text='사용자:%s#%s' % (message.author.name, message.author.discriminator), icon_url=message.author.avatar_url)
        await message.channel.send(embed=e)

    

    



    
    



    
    

        


    
access_token = os.environ["TOKEN"]
client.run(TOKEN)
