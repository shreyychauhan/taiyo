import requests
from bs4 import BeautifulSoup
import csv
# Make a request
page = requests.get(
    "https://fred.stlouisfed.org/categories")

soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as empty list
categories = []

# Extract and store in top_items  
x = soup.select('div.thumbnail')
for categ in x:
    money = categ.select('h4 > a')[0].text.strip()
    banking = categ.select('p.description')[0].text.strip()
    finance = categ.select('h4.price')[0].text.strip()
    
    categories.append({
        "money": money,
        "banking": banking,
        "finance": finance,
    })


keys = categories[0].keys()

with open('categories.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(categories)