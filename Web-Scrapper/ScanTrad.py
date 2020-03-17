import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
if __name__ == '__main__':
    def dossier():
        os.chdir("C://Users//Ridha//Desktop//Web-Scrapper")

    dossier()


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
        if 'id'in item.attrs and 'scimg' in item['id']:
            a= "https://scantrad.net/"+item['data-src']
            ListeLiens.append(a)
    if not ListeLiens ==[]:
        ListeLiens.remove(ListeLiens[1])

    return ListeLiens

def Next(soup,numero,url):
    NextUrl=""
    def urli(numero,url):
        numero= url.split('/')[-1]
        numero=int(numero)
        numero=numero+1
        return numero
    if RecupListeLiens(soup)==[]:
        NextUrl="Fin du Manga"
        print("Fin du Manga")
    else:
        moit="https://scantrad.net/mangas/"
        ake=url.split(moit)[1]
        oaa=ake.split('/')[0]
        numero=urli(numero,url)
        NextUrl= moit+oaa+"/"+str(numero)
        print(moit+oaa+"/"+str(numero-1))
    return [NextUrl,numero]