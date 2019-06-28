import requests
import bs4
from bs4 import BeautifulSoup
import re
from pynput.mouse import Button, Controller
from selenium import webdriver
from time import sleep
import lxml.html
import json

class Importar():
	def criaBanco():
			paginaWeb = "https://pr.olx.com.br/regiao-de-curitiba-e-paranagua/autos-e-pecas/carros-vans-e-utilitarios"
			html = requests.get("https://pr.olx.com.br/regiao-de-curitiba-e-paranagua/autos-e-pecas/carros-vans-e-utilitarios")
			doc = lxml.html.fromstring(html.content)
			titles = doc.xpath("//a[@class='OLXad-list-link']/@title")
			links = doc.xpath("//a[@class='OLXad-list-link']/@href")
			prices = doc.xpath("//p[@class='OLXad-list-price']")
			descricoes = doc.xpath("//p[@class='text detail-specific']")

			titulosFinal = []
			for title in titles:
				titulosFinal.append(title.lstrip().rstrip())


			linksFinal = []
			for link in links:
				linksFinal.append(link.lstrip().rstrip())


			pricesFinal = []
			for price in prices:
				pricesFinal.append(price.text_content())

			descricaoFinal = []
			for descricao in descricoes:
				descricaoFinal.append(str(descricao.text_content()).rstrip().lstrip().strip())



			output = []
			for info in zip(titulosFinal, linksFinal, pricesFinal, descricaoFinal):
				anunciosOLX = {}
				anunciosOLX['titulosAnuncios'] = info[0]
				anunciosOLX['linksAnuncios'] = info[1]
				anunciosOLX['precosAnuncios'] = info[2]
				anunciosOLX['descricaoAnuncios'] = info[3]
				output.append(anunciosOLX)


			with open('db_anuncios.json', 'w') as f:
			        json.dump(output, f)


			return print("BANCO SALVO COM SUCESSO!")
