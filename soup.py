import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import cssutils
#Supprimer les messages d'erreur et d'avertissement
import logging
cssutils.log.setLevel(logging.CRITICAL)

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
    #lien des fichiers css
    print(i)

    css_urls = i
    response = requests.get(css_urls)
    css = response.content

    sheet = cssutils.parseString(css)
    # print(sheet)
    #dictionnaire des attributs
    results = {}
    for rule in sheet:
        if rule.type == rule.STYLE_RULE:
            for prop in rule.style:
                # print(prop)
                if prop.name:
                    results[rule.selectorText] = [prop.name + ' : ' + prop.value]
    print(results)

# with open("css_files.txt", "w") as f:
#     for css_file in css_files:
#         print(css_file, file=f)
