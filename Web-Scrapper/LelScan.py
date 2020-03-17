import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os


def Navigate(url):
    if url!="Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens= Trouve_les_liens_stp(soup)
    return [soup,ListeLiens]

def Trouve_les_liens_stp(soup):
    ListeLiens = []
    images = soup.findAll('img')
    for lien in images:
        if 'class' in lien.attrs:
            if lien['class']==['img-responsive']:
                a= lien['data-src']
                ListeLiens.append(a)
    return ListeLiens




def Next(soup,numero,url):
    NextUrl=""
    moit="https://www.lelscan-vf.com/manga/"
    def urli(numero,url):
        numero= url.split('/')[-1]
        numero=int(numero)
        numero=numero+1
        return numero
    if Trouve_les_liens_stp(soup)==[]:
        NextUrl="Fin du Manga"
        print("Fin du Manga")
    else:
        moit="https://www.lelscan-vf.com/manga/"
        ake=url.split(moit)[1]
        oaa=ake.split('/')[0]
        numero=urli(numero,url)
        NextUrl= moit+oaa+"/"+str(numero)
        print(moit+oaa+"/"+str(numero-1))
    return [NextUrl,numero]











