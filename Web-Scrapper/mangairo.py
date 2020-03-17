import requests
import urllib.request
import os
from PIL import Image
import shutil
from bs4 import BeautifulSoup


url="https://mangairo.com/series-1288913053/chapter-39"
trunk="https://mangairo.com/"
pub=['https://mangairo.com/themes/home/images/clickhere.png',
'https://avt.mkklcdnv3.com/avatar_225/21637-fq918022.jpg',
'https://avt.mkklcdnv3.com/avatar_225_new/787-ef919381.jpg',
'https://avt.mkklcdnv3.com/avatar_225_new/3750-ei922314.jpg',
'https://avt.mkklcdnv3.com/avatar_225/18522-kemono_jihen.jpg',
'https://avt.mkklcdnv3.com/avatar_225_new/243-uz918840.jpg',
'https://avt.mkklcdnv3.com/avatar_225_new/356-ok918957.jpg',
'https://avt.mkklcdnv3.com/avatar_225_new/2377-xr920975.jpg',
'https://avt.mkklcdnv3.com/avatar_225_new/3410-rv921996.jpg',
'https://avt.mkklcdnv3.com/avatar_225_new/3563-od922144.jpg',
'https://avt.mkklcdnv3.com/avatar_225/20765-number_girl.jpg',
'https://avt.mkklcdnv3.com/avatar_225_new/2616-xc921213.jpg']
def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens=listimg(soup)
    return [soup,ListeLiens]

def listimg(soup):
    L=[]
    listeimg=list(soup.findAll('img'))
    for link in listeimg:
        if 'src' in link.attrs:
            if  str(link['src'])[-3:] == "jpg" or "png":
                L.append(link['src'])
    for i in range(len(pub)):
        if pub[i] in L:
            L.remove(pub[i])
    if 'https://avt.mkklcdnv3.com/content/nextchap.png' in L:
        print("Le chapitre recherché n'est pas encore sorti :)")
    return L

def soop(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

def Next(url):
    NextUrl=""
    url1=int(url.split('-')[-1])+1
    url2=url.split('/')[-2]
    NextUrl=trunk+url2+"/"+"chapter-"+str(url1)
    soup=soop(NextUrl)
    if listimg(soup)==['https://avt.mkklcdnv3.com/content/nextchap.png']:
        NextUrl="Fin du Manga"
    return NextUrl

