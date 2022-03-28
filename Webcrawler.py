import requests
from bs4 import BeautifulSoup

def web(page, WebUrl):
    if(page > 0):
        url = WebUrl
        code = requests.get(url)
        plain = code.text
        s = BeautifulSoup(plain, "html.parser")
        # for link in s.findAll('a', {'class': 's-access-detail-page'}):
        for link in s.findAll('a'):
            # tet=link.get('title')
            # print(tet)
            tet_2 = link.get('href')
            print(tet_2)

web(1, 'https://www.gsmarena.com/samsung_galaxy_f23-11406.php')