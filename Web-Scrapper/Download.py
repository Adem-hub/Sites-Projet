
import requests
import urllib.request
import os
from PIL import Image
import shutil
if __name__ == '__main__':

    def dossier():

        os.chdir("C://Users//Ridha//Desktop//Web-Scrapper")
    dossier()


import MangaFoxScrapper as MF
import MangaReaderScrapper as MR
import MangaZuki as MZ
import MangaNelo as ML
import LelScan as LS
import ScanVf as SV
import ScanOp as SO
import LabayScan as LBS
import ScanTrad as ST
import Lirescan as LIS
import lectureenligne as LL
import mangairo as MI
import frscan as FC
import lenscanv as LSS
import scan1 as SC
import Scanfr as SF
import scanmanga as SM
import WakaScan as WS

path = r"C:\Users\Ridha\Desktop\MangaScrapper"


def Download(download_url,name):
    if download_url != "Fin du Manga":

        if download_url != "https://s3.mangareader.net/images/erogesopt.jpg":

            req = urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})

            web_byte = urllib.request.urlopen(req).read()

            open(name + '.jpg','wb').write(web_byte)

def Compression():

    os.mkdir("Compr")

    ListeNon = []
    for elt in os.listdir():
        try:
            print(elt)
            im = Image.open(elt)
            im.save("Compr/" + elt,quality = 50, optimize = True)
        except:
            try:
                shutil.copy(elt,"Compr/" + elt)
            except:
                print("Erreur pour elt")

                ListeNon.append(elt)
    return ListeNon




class Site:

    def __init__(self,url,Titre):
        self.url = url
        self.soup = ""
        self.ListeLiens = []
        self.Titre = Titre
        self.chapter = ""
        self.compteur = 0
        self.numero=0
        self.Liste=[]

    def Initialisation(self):

        os.chdir(path)
        if self.Titre not in os.listdir():
            os.mkdir(self.Titre)
        os.chdir(self.Titre)
        with open('Titre.txt','w+') as file:
            file.write(self.Titre)


    def Navigate(self):

        if 'mangafox' in self.url:
            [self.soup,self.ListeLiens] = MF.Navigate(self.url)
        if 'manganelo' in self.url:
            [self.soup,self.ListeLiens] = ML.Navigate(self.url)
        if 'mangareader' in self.url:
            [self.soup,self.ListeLiens] = MR.Navigate(self.url)
        if 'mangazuki' in self.url:
            [self.soup,self.ListeLiens] = MZ.Navigate(self.url)
        if 'https://www.lelscan-vf.com' in self.url:
            [self.soup,self.ListeLiens] = LS.Navigate(self.url)
        if 'https://www.scan-vf' in self.url:
            [self.soup,self.ListeLiens] = SV.Navigate(self.url)
        if 'scan-op' in self.url:
            [self.soup,self.ListeLiens] = SO.Navigate(self.url)
        if 'labayscan' in self.url:
            [self.soup,self.ListeLiens] = LBS.Navigate(self.url)
        if 'scantrad' in self.url:
            [self.soup,self.ListeLiens] = ST.Navigate(self.url)
        if 'lirescan' in self.url:
            [self.soup,self.ListeLiens] = LIS.Navigate(self.url)
        if 'https://www.lecture-en-ligne.com' in self.url:
            [self.soup,self.ListeLiens] = LL.Navigate(self.url)
        if 'https://mangairo.com' in self.url:
            [self.soup,self.ListeLiens] = MI.Navigate(self.url)
        if 'https://www.frscan.me' in self.url:
            [self.soup,self.ListeLiens] = FS.Navigate(self.url)
        if 'http://lelscanv.com' in self.url:
            [self.soup,self.ListeLiens] = LSS.Navigate(self.url)
        if 'https://www.scan-1.com' in self.url:
            [self.soup,self.ListeLiens] = SC.Navigate(self.url)
        if 'https://www.scan-fr.co' in self.url:
            [self.soup,self.ListeLiens] =SF.Navigate(self.url)
        if 'https://scansmangas.xyz' in self.url:
            [self.soup,self.ListeLiens] = SM.Navigate(self.url)
        if 'https://wakascan.com' in self.url:
            [self.soup,self.ListeLiens] = WS.Navigate(self.url)



    def Next(self):
        if self.url != "Fin du Manga":
            with open("LastUrl.txt","w+") as file:
                file.write(self.url)
        if 'mangafox' in self.url:
            self.url = MF.Next(self.soup)
        if 'manganelo' in self.url:
            self.url = ML.Next(self.soup)
        if 'mangareader' in self.url:
            self.url = MR.Next(self.soup)
        if 'mangazuki' in self.url:
            self.url = MZ.Next(self.soup)
        if 'www.lelscan-vf.com' in self.url:
            [self.url,self.numero] = LS.Next(self.soup, self.numero,self.url)
        if 'https://www.scan-vf' in self.url:
            [self.url,self.numero] = SV.Next(self.soup, self.numero,self.url)
        if 'scan-op' in self.url:
            [self.url,self.numero] = SO.Next(self.soup, self.numero,self.url)
        if 'labayscan' in self.url:
            [self.url,self.numero] = LBS.Next(self.soup, self.numero,self.url)
        if 'scantrad' in self.url:
            [self.url,self.numero] = ST.Next(self.soup, self.numero,self.url)
        if 'lirescan' in self.url:
            [self.url,self.numero] = LIS.Next(self.soup, self.numero,self.url)

        if 'https://www.lecture-en-ligne.com' in self.url:
            self.url = LL.Next(self.url)
        if 'https://mangairo.com' in self.url:
            self.url= MI.Next(self.url)
        if 'https://www.frscan.me' in self.url:
            [self.url,self.numero]= FS.Next(self.soup,self.numero,self.url)
        if 'http://lelscanv.com' in self.url:
            self.url= LSS.Next(self.soup,self.url)
        if 'https://www.scan-1.com' in self.url:
            [self.url,self.numero]= SC.Next(self.soup,self.numero,self.url)
        if 'https://www.scan-fr.co' in self.url:
            [self.url,self.numero] =SF.Next(self.soup,self.numero,self.url)
        if 'https://scansmangas.xyz' in self.url:
            self.url = SM.Nect(self.soup,self.url)
        if 'https://wakascan.com' in self.url:
            self.url= WS.Next(self.url)



    def Chapter(self):
        if 'mangafox' in self.url:
            n = self.url.find('/chapter')
            m = self.url[n+1:].find('-')
            self.chapter = self.url[n+1:n+m+3]
        if 'manganelo' in self.url :
            n = self.url.find("/chapter")
            m = self.url[n+1:].find('/c')
            self.chapter = url[n+m+2:]
        if 'mangareader' in self.url:
            n= self.url.find('reader')
            m=self.url[n:].find('/')
            l = self.url[n+m+1:].find('/')
            k = self.url[n+m+1+l+1:].find('/')
            nom = self.url[n+m+1:m+n+k+l+2]
            nom.replace('/','_')
            self.url = nom
        if 'mangazuki' in self.url:
            n = self.url.find("chapter")
            self.chapter = self.url[n:-1]

    def DownloadListe(self):
        for lien in self.ListeLiens:
            if self.Liste.count(lien)>0:
                self.url="Fin du Manga"
                print("Fin du Manga")
            else:
                self.compteur +=1
                Download(lien,f"{self.compteur:05d}")
                self.Liste.append(lien)

    def InitSoup(self):
        self.Initialisation()
        while self.url != "Fin du Manga":
            self.Navigate()
            self.DownloadListe()
            self.Next()




    def ReprendreSoup(self):
        ba=['scan-vf','labay','scan-op','scantrad','lirescan']
        os.chdir(self.Titre)
        for item in ba:
            if item not in self.url:
                self.Navigate()
                self.Next()
        while self.url != "Fin du Manga":
            self.Navigate()
            self.DownloadListe()
            self.Next()
        os.chdir("..")



def Reprise():
    os.chdir(path)
    ListeSite = []

    for dossier in os.listdir():
        if os.path.isdir(dossier):
            os.chdir(dossier)
            with open("LastUrl.txt","r") as file:
                url = file.read()
            with open("Titre.txt","r") as file:
                Titre = file.read()
            Sitee = Site(url,Titre)
            ListeSite.append(Sitee)
            os.chdir("..")
    for site in ListeSite:
        site.ReprendreSoup()
    return ListeSite

def BoucleCompr():
    os.chdir(path)
    for dossier in os.listdir():
        if os.path.isdir(dossier):
            os.chdir(dossier)
            Compression()
            os.chdir("..")
