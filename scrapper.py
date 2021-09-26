import requests 
from bs4 import BeautifulSoup
import re

page = requests.get('https://www.continente.pt/pesquisa/?q=barril+cerveja')

soup = BeautifulSoup(page.text, 'html.parser')

prices_wrapper_class = soup.find(class_='prices-wrapper')

first_span = prices_wrapper_class.find_all('span')[0]

second_span = first_span.find_all('span')[0]

third_span = second_span.find_all('span')[0]

lines = third_span.text.split("\n")
non_empty_line = [line for line in lines if line.strip() != ""][0]

price = non_empty_line.replace(" ", "")


print('Preço Barril 5L Heineken: ' + price)
