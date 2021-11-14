from bs4 import BeautifulSoup
import requests

def scrapeSearch(anime):
    html_text = requests.get(f'https://ww1.gogoanime2.org/search/{anime}').text

    soup = BeautifulSoup(html_text, 'lxml')

    title_list = soup.find_all('div', class_ = 'img')

    if not title_list:
        return f'{anime} is invalid'

    anime_names = []
    for title in title_list:
        search_name = title.a['href'].split('/')[-1]
        anime_names.append(search_name)

    titles_str = ''
    for title in anime_names:
        titles_str += title + '\n'

    return titles_str
    
