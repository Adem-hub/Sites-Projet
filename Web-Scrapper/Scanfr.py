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


def Next(soup,numero,url):
    NextUrl=""
    moit="https://www.scan-fr.co/"
    def urli(numero,url):
        numero= url.split('/')[-2]
        numero=int(numero)
        numero=numero+1
        return numero
    if listimg(soup)==[]:
        NextUrl="Fin du Manga"
        print("Fin du Manga")
    else:
        moit="https://www.scan-fr.co/manga/"
        ake=url.split(moit)[1]
        numero=urli(numero,url)
        NextUrl= moit+str(url.split('/')[-3])+"/"+str(numero)+"/"+str(1)
        print(NextUrl)
    return [NextUrl,numero]

def listimg(soup):
    L = []
    images = soup.findAll('img')
    for lien in images:
        if 'class' in lien.attrs:
            if lien['class']==['img-responsive']:
                a= lien['data-src']
                L.append(a)
    return L