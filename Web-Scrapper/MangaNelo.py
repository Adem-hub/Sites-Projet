import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
if __name__ == '__main__':
    def dossier():
        os.chdir("C://Users//Ridha//Desktop//Web-Scrapper")

    dossier()

"""

Initialisation

"""


path = r"C:\Users\Ridha\Desktop\MangaScrapper"
CompteurParcours = 0


def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]

def RecupListeLiens(soup):
    ListeLiens=[]
    images = soup.findAll('img')
    for item in images:
        if 'alt'in item.attrs and 'MangaNelo.net' in item['alt']:
            a= item['src']
            ListeLiens.append(a)
    return ListeLiens





def Next(soup):
    NextUrl = ""
    A = soup.findAll('a')
    L = []
    for a in A:
        if a.text == "NEXT CHAPTER":
            NextUrl = a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl



