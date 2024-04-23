import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

url = "https://www.nature.com/search?q=autonomous%20vehicle%20vision&order=relevance&date_range=2021-2024"

#If there is no such folder, the script will create one automatically
folder_location = '/home/alexandre/Documents/PI/pdf'
if not os.path.exists(folder_location):os.mkdir(folder_location)

response = requests.get(url)

if (response.status_code != 200):
    raise Exception('[ERROR] Não foi possível acessar a url: ' + str(response.status_code) + ': ' + str(response.reason))

soup= BeautifulSoup(response.text, "html.parser")   
#filtro = soup.select("a[href$='articles']")  

# Use o método find para buscar o primeiro elemento com a classe "exemplo"
elemento = soup.find(class_="href")

# Verifique se o elemento foi encontrado
if elemento:
    print("Elemento encontrado:", elemento)
    # Faça algo com o elemento, como imprimir seu conteúdo
    print("Conteúdo do elemento:", elemento.text)
else:
    print("Elemento não encontrado.")

for link in soup.select("a[href]"):
    #Name the pdf files using the last portion of each link which are unique in this case
    filename = os.path.join(folder_location,link['href'].split('/')[-1])
    with open(filename, 'wb') as f:
        f.write(requests.get(urljoin(url,link['href'])).content)
