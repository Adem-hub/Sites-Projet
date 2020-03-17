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

url="http://labayscan.com/scans/solo-leveling-scan-86-vf/"
path = r"C:\Users\Ridha\Desktop\MangaScrapper"
CompteurParcours = 0




def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup,ListeLiens]


def RecupListeLiens(soup):
    ListeLiens=[]
    images = soup.findAll('img')
    for item in images:
        if 'alt'in item.attrs and item['alt']== "Responsive image":
            a= item['src']
            ListeLiens.append(a)
    return ListeLiens

def Next(soup,numero,url):
    NextUrl=""
    if RecupListeLiens(soup)== []:
        NextUrl= "Fin du Manga"
        print("Fin du Manga")
    else:
        a= soup.findAll('a')
        for item in a:
            if item.text =="Suiv":
                NextUrl= item['href']
        if NextUrl == "#latest_mangas":
            def urli(numero,url):
                numero= url.split('-')[-4]
                numero=int(numero)
                numero=numero+1
                return numero
            moit="http://labayscan.com/scans/"
            ake=url.split(moit)[1]
            oaa=ake.split('/')[0]
            title= oaa.split('-scan')[0]
            numero=urli(numero,url)
            NextUrl= moit+title+"-scan-"+str(numero)+"-vf/"
            print(moit+title+"-scan-"+str(numero-1)+"-vf/")
    return [NextUrl,numero]



