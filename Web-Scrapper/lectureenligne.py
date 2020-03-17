# Les imports
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os


url="https://www.lecture-en-ligne.com/chapter/24224"
trunk="https://www.lecture-en-ligne.com"

def listimg(soup):
    Listimgs = []
    img= soup.findAll('img')
    for link in img:
        if 'class' in link.attrs and link['class']==["lazy"]:
                a= link['data-src']
                a=a[1 : : ]
                a=a[1 : : ]
                Listimgs.append(trunk+a)
    return Listimgs



def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = listimg(soup)
    return [soup,ListeLiens]

def Next(soup):
    NextUrl=""
    a=soup.findAll('div')[17]
    b=a.findAll('a')[2]
    abc=b['href'][2:]
    NextUrl=trunk+abc
    return NextUrl


