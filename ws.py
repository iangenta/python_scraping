from bs4 import BeautifulSoup
import requests

URL_BASE = 'https://scrapepark.org/courses/spanish/'

# html
pedido = requests.get(URL_BASE)
html = pedido.text

#parser
soup = BeautifulSoup(html, 'html.parser')

#h2
all_h2 = soup.find_all('h2')
for h2 in all_h2:
    print(h2.get_text(strip=True))
    
# taking jpgs
src_all = soup.find_all(src=True)

for e in src_all:
    if e['src'].endswith('.jpg'):
        print(e)
        
#download images

url_img = []  

for i, image in enumerate(src_all):
    if image['src'].endswith('.png'):
        print(image['src'])
        r  = requests.get(f'https://scrapepark.org/courses/spanish/{image["src"]}') 
        with open(f'imagen_{i}.png','wb') as f:
            f.write(r.content)     