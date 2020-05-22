from urllib.request import urlopen
from urllib.request import HTTPError
import urllib.request
from bs4 import BeautifulSoup

def namu(message):
    location = urllib.parse.quote(message)
    url = 'https://namu.wiki/w/'+location
    hdr = {'User-Agent': 'Mozilla/5.0'}
    req = urllib.request.Request(url,headers=hdr)
    try:
        response = urlopen(req)
    except:
        return 0
    soup = BeautifulSoup(response,'html.parser')
    ans = soup.find('div',class_='wiki-heading-content').text[:500]
    return ans+'...\n'+url

class Melon:
    def __init__(self):
        url = 'http://www.melon.com/chart/index.htm'
        hdr = {'User-Agent':'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=hdr)
        response = urlopen(req)
        soup = BeautifulSoup(response, 'html.parser')
        tag = []
        a = []
        b = []
        for t in soup.find_all('tr', class_='lst50'):
            tag.extend(t.find('div',class_='wrap_song_info').find_all('a')[:1])
            a.extend(t.find('div',class_='ellipsis rank01').find_all('a')[2:])
            b.extend(t.find('div', class_='ellipsis rank02').find_all('a')[:3])
        if __name__=="__main__":
            for i in range(50):
                print(i+1, tag[i].text,a[i].text,b[i].text)
        self.tag=tag
        self.a=a
        self.b=b

class genie:
    def __init__(self):
        url = 'https://www.genie.co.kr/chart/top200?ditc=D&ymd=20200504&hh=13&rtm=Y&pg=1'
        hdr = {'User-Agent':'Mozilla/5.0'}
        req = urllib.request.Request(url, headers=hdr)
        response = urlopen(req)
        soup = BeautifulSoup(response, 'html.parser')
        tag = []
        a = []
        for t in soup.find_all('div', class_='music-list-wrap'):
            tag.extend(t.find('a', class_='title ellipsis')[:1])
            a.extend(t.find('a', class_='artist ellipsis')[2:])
        if __name__=="__main__":
            for i in range(50):
                print(i+1,tag[i].text,a[i].text)
        self.tag=tag
        self.a=a