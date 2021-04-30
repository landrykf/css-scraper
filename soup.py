import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import cssutils
#Supprimer les messages d'erreur et d'avertissement
import logging
cssutils.log.setLevel(logging.CRITICAL)

import json

pages = ['index.html','portfolio.html','contact.html','projetPortfolio.html', 'jsBreaker.html']

for i in pages:
    
    url = 'http://koffi.me/views/' + (i)

    response = requests.get(url)
    #je parse la réponse de ma requete get 
    soup = BeautifulSoup(response.text, 'lxml')

    css_files = []
    links = soup.find_all("link")
    for css in links:
        if css.attrs.get("href"):
            #si link a l'attribut 'href'.
            css_url = urljoin(url, css.attrs.get("href"))
            css_files.append(css_url)


for i in css_files:
    data = []
    #lien des fichiers css
    print(i)
    data.append(i)

    css_urls = i
    response = requests.get(css_urls)
    css = response.content

    sheet = cssutils.parseString(css)
    #dictionnaire des attributs
    results = {}
    for rule in sheet:
        if rule.type == rule.STYLE_RULE:
            for prop in rule.style:
                if prop.name:
                    # print(rule.style)
                    results[rule.selectorText] = [prop.name + ' : ' + prop.value]
    data.append(results)
    # print(results)
    print(data)


with open("scraper.json", "w") as writeJSON:
    json.dump(data, writeJSON, ensure_ascii=False)

