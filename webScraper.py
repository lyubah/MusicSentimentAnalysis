import config
import re
import requests;
from bs4 import BeautifulSoup

base_root = 'https://genius.com/'
token=config.token

def urlify(song_title, artist_name):
    artist = artist_name.lower()
    song = song_title.lower()
    artist = re.sub(r'[^\w\s]', '', artist)
    song = re.sub(r'[^\w\s]', '', song)
    artist = artist_name.capitalize()
    url = artist+'-'+song+'-'+'lyrics'
    url= base_root+ url.replace(" ", '-')
    print(url)
    return url 

def pathify(song_title, artist_name):
    artist = artist_name.lower()
    artist = artist_name.capitalize()
    song = song_title.lower()
    url = artist+'-'+song+'-'+'lyrics'
    url= url.replace(" ", '-')
    return url 

def clean_lyrics(lyrics):
    lyrics=re.sub(">",'',lyrics)
    lyrics=re.sub("Lyrics",' ',lyrics)
    lyrics=re.sub("2Embed",' ',lyrics)
    lyrics=re.sub("\n",' ',lyrics)
    lyrics = re.sub(r'[\(\[].*?[\)\]]', ' ', lyrics)
    lyrics = re.sub('Embed','', lyrics)
    return lyrics

def get_lyrics(token , song_title, artist_name):
    headers = {'Authorization': 'Bearer '+ token }
    url = urlify(song_title, artist_name)
    headers= {'Authorization': 'Bearer '+ token }
    response = requests.get(url, headers=headers)
    path = pathify(song_title, artist_name)
    html = BeautifulSoup(response.text.replace('<br/','\n'), 'html.parser')
    div = html.find("div", class_=re.compile("^lyrics$|Lyrics__Root"))
    #fix this 
    if div is None:
            print("Couldn't find the lyric's section. "
                      "Please check spelling, or  report this if the song has lyrics.\n"
                      "Song URL:", url)
            return None
    lyrics = div.get_text()
    return lyrics 


def writeLyrics(lyrics):
    # file = open('lyrics.txt','wb')
    # file.write(lyrics.encode())
    # file.close()
    result = dict()
    result['lyrics']=lyrics
    return result

def webScrape(song_title, artist_name):
    lyrics = get_lyrics(token , song_title, artist_name)
    lyrics = clean_lyrics(lyrics)
    #returns dictionary object
    lyrics = writeLyrics(lyrics)
    return lyrics
