import requests
import urllib.request
import os
from PIL import Image
import shutil
from bs4 import BeautifulSoup

# Veuillez séléctionner le mode visionnage en :"style de liste"

url="https://wakascan.com/manga/naruto/volume-01/?style=list"
trunk="https://wakascan.com/manga/"

pub=["https://wakascan.com/wp-content/uploads/2019/10/5da324df427a0968436766-75x106.jpg",
"https://wakascan.com/wp-content/uploads/2019/07/wakascanlogo2.png",
"https://wakascan.com/wp-content/uploads/2019/08/mini_000-75x106.jpg",
"https://wakascan.com/wp-content/uploads/2019/08/103797l-75x106.jpg",
"https://wakascan.com/wp-content/uploads/2019/08/208542l-75x106.jpg",
"'https://wakascan.com/wp-content/uploads/2019/08/15171l-75x106.jpg",
"https://wakascan.com/wp-content/uploads/2019/08/cover_2-75x106.jpg",
"https://wakascan.com/wp-content/uploads/2019/08/179370l-75x106.jpg",
"https://wakascan.com/wp-content/uploads/2019/10/5d9a24fb73e7e038027387-1-75x106.jpg",
"https://wakascan.com/wp-content/uploads/2019/08/5c5a887512a8e692972550-75x106.jpg",
"https://wakascan.com/wp-content/uploads/2019/07/5c841d307da6a283994253.jpg",
"https://wakascan.com/wp-content/uploads/2019/07/maou_ni_natte_node_dungeon_tsukutte_jingai_musume_to_honobono_suru_1190.jpg",
"https://wakascan.com/wp-content/uploads/2019/08/01_24-75x106.jpg",
"https://wakascan.com/wp-content/uploads/2019/07/5c96cd29b76dc302115698-75x106.jpg",
"https://wakascan.com/wp-content/uploads/2019/07/211038.jpg",
'https://wakascan.com/wp-content/uploads/2019/08/0003_78-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/5cda8213e080b869229449-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/hypersonic-music-club-crunchy-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/2_09c-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/cover_4-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/07/978-4-08-870762-4-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/jknf_raiden_18_03.knf_raiden-18_03_00-75x106.jpg', 'https://wakascan.com/wp-content/uploads/2019/08/135769l-75x106.jpg'
'https://wakascan.com/wp-content/uploads/2019/08/205419l-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/07/166254-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/5c3683cd38178899751948-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/meitantei_conan_-_zero_no_tea_time_8577-75x106.jpg'
'https://wakascan.com/wp-content/uploads/2019/08/157307l-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/dragonsrioting200x0-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/165482l-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/198159l-75x106.jpg'
'https://wakascan.com/wp-content/uploads/2019/08/83160l-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/163821l-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/area.no_.kishi_.600.940479-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/167329l-75x106.jpg'
'https://wakascan.com/wp-content/uploads/2019/07/5cb0c11de5dc1954508403.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/0002_8-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/cover_18-75x106.jpg',
'https://wakascan.com/wp-content/uploads/2019/08/113411l-75x106.jpg'
]

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens=listimg(soup)
    return [soup,ListeLiens]


def listimg(soup):
    L=[]
    LL=[]
    listeimg=list(soup.findAll('img'))
    for link in listeimg:
        if 'src' in link.attrs:
            if  str(link['src'])[-3:] == "jpg" or "png":
                L.append(link['src'])
    for i in range(len(pub)):
        if pub[i] in L:
            L.remove(pub[i])
    for elem in L:
        a=elem[7:]
        LL.append(a)
    LL.pop(-1)
    LL.pop(-1)
    LL.pop(-1)
    LL.pop(-1)
    return LL


def soop(url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        return soup




def Next(url):
    NextUrl=""
    url1=url.split('/')[5]
    url2=int(url1.split('-')[1])+1
    url4=url1.split('-')[0]
    url3=url.split('/')[4]
    NextUrl=trunk+url3+"/"+url4+"-"+str(f"{url2:02d}")+"/"+"?style=list"
    return NextUrl
