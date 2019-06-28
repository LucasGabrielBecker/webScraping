import requests
import bs4
from bs4 import BeautifulSoup
import re
from pynput.mouse import Button, Controller
from selenium import webdriver
from time import sleep
import lxml.html
from scrapingSavingMongodb import Importar
#classe do preço "OLXad-list-price"

def juntaAnuncio(execucoes):
    repetir = True
    vezesRodadas = 0
    página = 1
    while repetir == True:
        # driver = webdriver.Firefox()
        if página > 1:
            paginaWeb = requests.get("https://pr.olx.com.br/regiao-de-curitiba-e-paranagua/autos-e-pecas/carros-vans-e-utilitarios?o={}".format(str(página)))
        else:
            paginaWeb = requests.get("https://pr.olx.com.br/regiao-de-curitiba-e-paranagua/autos-e-pecas/carros-vans-e-utilitarios")
        doc = lxml.html.fromstring(paginaWeb.content)
        sleep(3)
        # print("Abrindo página web: {}".format(paginaWeb.text()[:20]))
        data = requests.get("https://pr.olx.com.br/regiao-de-curitiba-e-paranagua/autos-e-pecas/carros-vans-e-utilitarios")
        soup = BeautifulSoup(data.text, 'html.parser')
        carro = soup.find_all('h2', {"class":"OLXad-list-title"})
        soup = soup.find('h2', {"class":"OLXad-list-title"}).text
        # descricoes = doc.xpath("//p[@class='text detail-specific']") #encontrar botao proxima pagina
        # proxPagina = driver.find_element_by_css_selector('.next > a:nth-child(1)')
        anuncios = []
        for i in range(len(carro)):
            anuncios.append(carro[i].text.lstrip().rstrip())

        # proxPagina.click()
        sleep(3)
        #Salvando arquivo -----------------
        arquivo = open("links.txt", 'w')
        for anuncio in anuncios:
            arquivo.write(anuncio+"\n")    #Pula linha por anuncio
        # arquivo.save()
        arquivo.close()
        vezesRodadas += 1
        página += 1
        if vezesRodadas > execucoes:
            repetir == False
            break


juntaAnuncio(5)
#alterando vezes em que será repetido o programa
Importar.criaBanco()
