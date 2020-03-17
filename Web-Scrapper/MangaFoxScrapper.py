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

path = r" C:\Users\Ridha\Desktop\MangaScrapper"
CompteurParcours = 0
Titre = "Manga2"
url = "https://ww3.mangafox.online/the-top-clan-leader-in-history/chapter-74-1192366631948209"

"""

Navigation dans la page Web

"""


url = "https://ww3.mangafox.online/favorite-part/chapter-1-324246019529673"




"""

Recherche de l'image dans la page web

"""


"""
Ici, la fonction Navigate prend l'url en argument et donne en sortie le soup ainsi que la la Liste des images du chapitre . Si l'url est different de Fin du Manga, alors on prend le soup de la page , c'est à dire son contenu en html. On va ensuite utliser la fonction RecupListeLiens et recuperer justement une liste qui contient toutes les url des images du chapitre.
"""

def Navigate(url):
    if url != "Fin du Manga":
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")
        ListeLiens = RecupListeLiens(soup)
    return [soup, ListeLiens]
"""

La fonction RecupListeLiens fonctionne assez facilement ,elle prend le soup de la page en argument et nous renvoie une liste avec les liens des images. On va chercher tout les img dans le soup . Si il contient 'class' comme attribut et que l'objet de class est 'load_img', on  ajoute à la liste ListeLiens le src de la balise img donc l'url de l'image. On fait une boucle et on ajoute donc toutes les images du chapitre.
"""
def RecupListeLiens(soup):
    Img = soup.findAll('img')
    #Creation liste vide
    ListeLiens = []
    for item in Img:
        if 'class' in item.attrs and item['class'] == ['load_img']:
            ListeLiens.append(item['src'])
    return ListeLiens







"""

Manga Fox : Suivant .find(class="next_prev") puis enfant btn"

Boucle sur les scr de class="list_img"

"""

"""
NextUrl est au depart un string vide
La fonction Next permet de changer de Chapitre et nous renvoie l'url du prochain chapitre.
Elle va chercher tout les a dans le soup. Si le texte de la balise <a> correspond à "Next", on prend le href et donc l'url de la page suivante et l'associe à la variable NextUrl. Si il n'y a pas ce texte, la variable reste un str vide , on va donc l'associer au str 'Fin du Manga' et à la fin print le NextUrl
"""

def Next(soup):
    trunk = "https://ww3.mangafox.online"
    NextUrl = ""
    A = soup.findAll('a')
    L = []
    for a in A:
        if a.text == "Next":
            NextUrl = a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl



