import requests
from bs4 import BeautifulSoup

#
# req = requests.get('https://en.wikipedia.org/wiki/Python_(programming_language)')
# soup = BeautifulSoup(req.text, "lxml")
# print('title ', soup.title)
# print('h1 ',soup.h1)
# # <h1 class="firstHeading" id="firstHeading" lang="en">Python (programming language)</h1>
#
# print('h1 string ',soup.h1.string)
# # 'Python (programming language)'
#
# print('h1 class ',soup.h1['class'])
# # ['firstHeading']
#
# print('h1 id ',soup.h1['id'])
# # 'firstHeading'
#
# print('h1 attr ',soup.h1.attrs)
# # {'class': ['firstHeading'], 'id': 'firstHeading', 'lang': 'en'}
#
#
# print(soup.h1)
# # <h1 class="firstHeading, mainHeading">Python - Programming Language</h1>


print('=================')
req = requests.get('https://fr.windfinder.com/tide/saint_lunaire')
req = requests.get('http://www.horaire-maree.fr/maree/Saint-Lunaire/')
soup = BeautifulSoup(req.text,"lxml")
print(soup.find(id='i_donnesJour'))