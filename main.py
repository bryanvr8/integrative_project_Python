import pandas as pd
import requests
from bs4 import BeautifulSoup

listanomes = []
listadesc = []
listaprecos = []

r = requests.get("http://127.0.0.1:5501/index.html")
soup = BeautifulSoup(r.content, "html.parser")

s = soup.find('div', class_="swiper-wrapper")

tituloproduto = s.find_all('a')
for c in tituloproduto:
    listanomes.append(c.text)

precoproduto = s.find_all("b")
for c in precoproduto:
    listaprecos.append(c.text)

# descricaop = s.find_all('p')
# for c in descricaop:
#     listadesc.append(c.text)
#
# qntdp = s.find_all('h3')
# for c in qntdp:
#     listaquantidade.append(c.text)

lista = {"Produto": listanomes, "Preço": listaprecos}
listalegal = pd.DataFrame(lista)
listalegal.to_excel("pi.xls")
print(listalegal)

