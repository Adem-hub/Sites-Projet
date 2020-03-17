import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import os
if __name__ == '__main__':
    def dossier():
        os.chdir("C://Users//Ridha//Desktop//Web-Scrapper")
    dossier()


#Ne marche que sur MangaReader


"""

Initialisation

"""

path = r"C:\Users\Ridha\Desktop\MangaScrapper"
CompteurParcours = 0
Titre = "Manga"



"""

Navigation dans la page Web

"""

trunk = "https://www.mangareader.net"


url = trunk + "/tate-no-yuusha-no-nariagari/1/2"




"""

Recherche de l'image dans la page web

"""

"""
Dans le Navigate de MangaReader, c est different des autes car il ne contient pas toutes les images dans un seul chapitre, il faut Naviguer page par page.Elle prend en entrée l'url du chapitre. On recupere à l'aide de cette fonction le soup ainsi que l image de la page. Si dans le soup, il n'y a pas le texte 'is not released', On va alors chercher le premier 'img' dans le soup.Cet img contient l image de la page . Cependant , elle est contenue dans le src de img. On va alors le recuperer et  l'associer à la variable download_url. Si la page ne contient pas le texte 'is not released', on print 'Fin du Manga' et download_url = "Fin du Manga"
"""
def Navigate(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    if soup.text.find("is not released") <0:
        Im = soup.findAll('img')[0]
        link = Im['src']
        download_url = [link]
    else:
        print("Fin du manga")
        download_url = "Fin du Manga"
    return [soup, download_url]


"""
Cette fonction Next prend en argument la soup de l'url et renvoie l'url de la page suivante.On associe d'abord NextUrl à un string vide. Au debut , on va chercher toutes les divs dans le soup. On va alors chercher la div qui contient l'url. Pour cela , on va verifier pour chaque div si l'attribut id est dedans et si l'objet de cet attribut est 'imgholder'. Si c'est le cas, on associe NextUrl à un trunk qui represente le debut de l'url du site qui ne changera pas , et on lui ajoute le href de la balise <a> de la div.
Si id n'est pas dans les attributs de la div , cela veut dire que la page n'existe pas et on asscocie NextUrl à Fin du Manga.
A la fin , on print NextUrl pour savoir ou on en est lorsquon va download sur la page Download.py
"""
def Next(soup):
    NextUrl = ""
    Div = soup.findAll("div")
    for item in Div:
        if 'id' in item.attrs and item['id'] == 'imgholder':
            NextUrl = trunk + item.a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl







