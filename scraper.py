import db_connection
from bs4 import BeautifulSoup
import requests

db = db_connection
r = db.getConnection()

def scrape(anime_name):
    html_text = requests.get(f'https://ww.gogoanime2.org/anime/{anime_name}').text

    soup = BeautifulSoup(html_text, 'lxml')
    
    episodes_container = soup.find_all('div', class_ = 'name')
    if episodes_container:
        episodes = episodes_container[-1]
    else:
        return -1

    latest = episodes.text.split()[-1]
    return latest

def setKey(anime_name, latest_ep):
    r.set(anime_name, latest_ep)

def getKey(anime_name):
    episode = r.get(anime_name)
    if episode:
        return episode
    return -1
    
def checkNewEpisode(anime_name):
    latest_ep = scrape(anime_name)
    if latest_ep == -1:
        return f"{anime_name} doesn't exist"

    curr_episode = getKey(anime_name)

    if int(latest_ep) > int(curr_episode):
        setKey(anime_name, latest_ep)
        return f'New episode is out : {latest_ep}'
    else:
        return f'Waiting for new episode to release\nCurrent Episode : {curr_episode}'