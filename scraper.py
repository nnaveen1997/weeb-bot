from bs4 import BeautifulSoup
import requests
import db_connection

db = db_connection
r = db.getConnection()

html_text = requests.get('https://myanimelist.net/anime/49926/Kimetsu_no_Yaiba__Mugen_Ressha-hen?q=kimetsu&cat=anime').text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
# print(soup.prettify())

def checkNewEpisode():
    episode = soup.find('li', class_ = 'btn-anime')
    # print(episode)
    episode_number = episode.a['href'].split('/')[-1]
    # print(episode_number)
    return episode_number

def setKey(episode_number):
    r.set('chapter', episode_number)

def getKey():
    chapter = r.get('chapter')
    print(chapter)

if __name__ == '__main__':
    episode_number = checkNewEpisode()
    setKey(episode_number)
    getKey()