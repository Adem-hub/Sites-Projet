import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os

if __name__ == '__main__':
    def dossier():
        os.chdir("C://Users//Ridha//Desktop//Web-Scrapper")

    dossier()

Part= "https://www.lirescan.me"

def Navigate(url):
    if url!="Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens= RecupLiens(soup)
    return [soup, ListeLiens]

def RecupLiens(soup):
    ListeLiens = []
    images = soup.findAll('img')
    for lien in images:
        if 'id'in lien.attrs and lien['id']=="image_scan":
            a= Part+lien['src']
            ListeLiens.append(a)
    return ListeLiens

def Next(soup,numero,url):
    NextUrl=""
    A= soup.findAll('a')
    for lk in A:
        if 'id' in lk.attrs and lk['id']=='next_link':
            NextUrl= Part + lk['href']
    if NextUrl == "":
        def urli(numero,url):
            numero= url.split('/')[-2]
            numero=int(numero)
            numero=numero+1
            return numero
        nah='-lecture-en-ligne/'
        Party= "https://www.lirescan.me/"
        kk= url.split(Party)[1]
        Titre= kk.split('-lecture-en-ligne')[0]
        numero=urli(numero,url)
        NextUrl= Party+Titre+nah+str(numero)+"/"
        print(Party+Titre+nah+str(numero-1)+"/")
    return [NextUrl,numero]

