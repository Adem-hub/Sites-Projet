# Les imports
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os


url="http://lelscanv.com/scan-one-piece/970"
trunk="http://lelscanv.com"
def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = Lien(url)
    return [soup,ListeLiens]

def listimg(soup):
    img = soup.findAll('img')[0]
    urlim=trunk+img['src']
    return urlim



def Nextscan(soup,url):
    L=[]
    lien=""
    urll=url.split('/')[3]
    a=soup.findAll('div')[4]
    b=a.findAll('a')
    for link in b:
        if urll in link['href']:
            lien=link['href']
            L.append(lien)
    L.pop(1)
    return list(L)

def Lien(url):
    soup = soop(url)
    L=Nextscan(soup,url)
    LL=[]
    for i in range(0,len(L)):
        soup=soop(L[i])
        img=listimg(soup)
        LL.append(img)
    LL.pop(-1)
    LL.pop(-1)
    LL.pop(1)
    return list(LL)

def soop(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup





def Next(soup,url):
    NextUrl=""
    A=soup.findAll('a')
    url1=url.split('/')[-1]
    url3=url.split('/')[-2]
    url2=int(url1)+1
    for a in A:
        if url3+"/"+str(url2) in a['href']:
            NextUrl=a['href']
        if NextUrl == "":
            NextUrl="Fin du manga"
    return NextUrl

