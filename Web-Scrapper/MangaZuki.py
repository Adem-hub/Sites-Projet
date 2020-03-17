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


path = r"C:\Users\Ridha\Desktop\MangaScrapper"
CompteurParcours = 0


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
Le RecupListeLiens fonctionne sensiblement pareil que les autres. il prend la soup de la page en argument. On va chercher toutes les divs de cette soup. Pour chaque div de la page, on verifie si classeDownload est True ou False. Si elle est True,On ajoute à la liste L les ou la div en question. Pour chaque element de la Liste L, on va recuperer toutes les balises img  dans la liste ListeLiens. Enfin , pour chaque balise img contenu dans la liste ListeLiens, on boucle  et on ajoute le src de l'image en question à la liste ListeLiens. A la fin , on aura les images de tout le chapitre et on va renvoyer la ListeLiens .
"""
def RecupListeLiens(soup):
    Div = soup.findAll('div')
    L = []
    for item in Div:
        if ClasseDownload(item):
            L.append(item)
    ListeTag = []
    for item in L:
        ListeTag.append(item.find('img'))
    ListeLiens = []
    for item in ListeTag:
        t = item['src']
        n = t.find('https')
        ListeLiens.append(item['src'][n:])
    return ListeLiens


"""
On cree une variable NextUrl qui correspond a un str vide
La fonction Next permet de changer de chapitre . Elle prend  en argument le soup de la page. On cherche tout les a de la page. Pour chaque <a>, si la l'attribut class existe et cet attribut a pour objet 'btn''next_page', on associe la variable NextUrl a l'href donc l'url de la balise a . Si la varaible NextUrl reste un str vide, On associe la variable NextUrl à 'Fin du Manga' . A la fin , on affiche le lien de la page et on le return.
"""
def Next(soup):
    NextUrl = ""
    A = soup.findAll('a')
    L = []
    for a in A:
        if 'class' in a.attrs and a['class'] == ['btn','next_page']:
            NextUrl = a['href']
    if NextUrl == "":
        NextUrl = "Fin du Manga"
    print(NextUrl)
    return NextUrl

"""
ClasseDownload prend item en argument et item correspond à chaque div de la soup. au debut , la variable bool est False mais si la div contient class en attribut et que cette classe a pour objet 'page_break', alors le bool est True et donc on le return.
"""
def ClasseDownload(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['page-break'])
    return bool
"""
Les deux fonctions suivantes ne sont pas utilisées , mais elles fonctionnent  du meme principe que ClasseDownload()
"""
def ClasseNextDiv(item):
    bool = False
    bool = 'class' in item.attrs and (item['class'] == ['navi-change-chapter-btn'] or item['class'] == ['btn-navigation-chap'])
    return bool

def ClasseNextListe(tag):
    bool = False
    bool = 'class' in tag.attrs  and (tag['class'] ==['navi-change-chapter-btn-next','a-h'] or tag['class'] == ['next'])
    return bool


