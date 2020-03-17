# Les imports
import re
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os



def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens=liste(Nextscan(soup,url))
    return [soup,ListeLiens]


def soop(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup

url="https://scansmangas.xyz/scan-naruto-684/"
trunk="https://scansmangas.xyz"
def listimg(soup):
    L=[]
    a=soup.findAll('div')[17]
    listeimg=a.findAll('img')
    num=len(listeimg)
    for i in range(0,num):
        abc=a.findAll('img')[i]
        L.append(abc['src'])
    return L

def Next(soup,url):
    NextUrl=""
    A=soup.findAll('option')
    urll=int(int(re.search(r'\d+', url).group()))+1
    for a in A:
        if str(urll) in a['value']:
            NextUrl=a['value']
        elif NextUrl == "":
            NextUrl="Fin du manga"
    return NextUrl


def Listeimg(url):
    soup=soop(url)
    L=[]
    lien=""
    a=soup.findAll('img')
    for link in a:
        if trunk in link['src']:
            lien=link['src']
            L.append(lien)
    if L==[]:
        print("Rip")
    else:
        L.pop(-1)

    return (L[1])

def Nextscan(soup,url):
    L=[]
    lien=""
    urll=url.split('/')[3]
    urlll=url.split('-')[2]
    a=soup.findAll('div')[15]
    b=a.findAll('a')
    for link in b:
        if urlll in link['href']:
            lien=link['href']
            L.append(lien)
    return list(L)

def liste(liste):
    LL=[]
    for item in liste:
        a=Listeimg(item)
        LL.append(a)
    return LL




