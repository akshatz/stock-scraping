import requests 
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
rows = soup.find_all(class_='total_row_world')
data = [[td.text.strip() for td in row.find_all('td')] for row in rows]
for l in data:
    print(l)