
import requests
from bs4 import BeautifulSoup


category = input('Enter an item you want to search for (e.g. "phone"): ').encode()
response = requests.get('https://avito.ru/rossiya', params= {'q': category})
print('=====Retrieving data=====')
print(response.status_code)

soup = BeautifulSoup(response.content, 'html.parser')
ads = soup.find_all('div', attrs={'class': 'item_table-wrapper'})
for item in ads:
    title = item.find('span', {'itemprop': 'name'}).text.strip()
    price = item.find('meta', {'itemprop': 'price'}).get('content')
    link = item.find('a', {'class': 'snippet-link', 'itemprop': 'url'}).get('href')
    city = item.find('span', {'class': 'item-address__string'}).text.strip()
    print('TITLE IS: ', title)
    print('PRICE IS:', price, 'RUB')
    print('LOCATION IS:', city)
    print('LINK IS:', 'avito.ru' + link)
    print('-----------')
