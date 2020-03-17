# Les imports
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os



url="https://www.scan-1.com/naruto/chapitre-1/54"



def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = listimg(soup)
    return [soup,ListeLiens]

def listimg(soup):
    L = []
    images = soup.findAll('img')
    for lien in images:
        if 'class' in lien.attrs:
            if lien['class']==['img-responsive']:
                a= lien['data-src']
                L.append(a)
    return L

def Next(soup,numero,url):
    NextUrl=""
    moit="https://www.scan-1.com/"
    def urli(numero,url):
        numero= url.split('-')[4]
        numero=int(numero.split('/')[0])
        numero=numero+1
        return numero
    if listimg(soup)==[]:
        NextUrl="Fin du Manga"
        print("Fin du Manga")
    else:
        moit="https://www.scan-1.com/"
        numero=urli(numero,url)
        NextUrl= moit+str(url.split('/')[-3])+"/"+"chapitre-"+str(numero)+"/"+str(1)
        print(NextUrl)
    return [NextUrl,numero]