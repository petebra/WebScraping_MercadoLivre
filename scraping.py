import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

url_base = 'https://lista.mercadolivre.com.br/'
productName = input('Type here the product you wanna search -> ')
table = [[]]
header = ['Product', 'Value']
count = 1

response = requests.get(url_base + productName)

site = BeautifulSoup(response.text, 'html.parser')

for product in site.select('.ui-search-result__content-wrapper'):
    title = product.select_one('.ui-search-item__group__element')
    value = product.select_one('.price-tag-amount')

    table.append([title.text, value.text])
    count += 1

print(tabulate(table, headers=header, tablefmt='pretty', colalign=('left',)))