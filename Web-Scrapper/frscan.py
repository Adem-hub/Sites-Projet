# Les imports
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os


def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = listimg(soup)
    return [soup,ListeLiens]

def listimg(soup):
    Listimgs = []
    img= soup.findAll('img')
    for link in img:
        if 'class' in link.attrs:
            if link['class']==['img-responsive']:
                a= link['data-src']
                Listimgs.append(a)
    return Listimgs

def Next(soup,numero,url):
    NextUrl=""
    moit="https://www.frscan.me/manga"
    def urli(numero,url):
        numero= url.split('/')[-1]
        numero=int(numero)
        numero=numero+1
        return numero
    if listimg(soup)==[]:
        NextUrl="Fin du Manga"
        print("Fin du Manga")
    else:
        moit="https://www.frscan.me/manga/"
        numero=urli(numero,url)
        NextUrl= moit+str(url.split('/')[-3])+"/"+str(numero)+"/"+str(1)
        print(NextUrl)
    return [NextUrl,numero]

url="https://www.frscan.me/manga/shingeki-no-kyojin/126/1"