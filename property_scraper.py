from dataclasses import dataclass
from bs4 import BeautifulSoup
import re
from pathlib import Path


@dataclass
class PropertyData(object):

    def __init__(self, html_file):
        if html_file.exists():
            with open(html_file) as html:
                source = html.read()

        self.data = BeautifulSoup(source, 'lxml')

    def get_address(self):
        # Address
        print('Block 1 (Address): ' + " ".join(
            self.data.find('h1', attrs={'itemprop': 'streetAddress'}).text.split(',')[:-1]))
        return " ".join(self.data.find('h1', attrs={'itemprop': 'streetAddress'}).text.split(',')[:-1])

    def get_postcode(self):
        # Postcode

        print('Block 2 (Postcode): ' + self.data.find('h1', attrs={'itemprop': 'streetAddress'}).text.split(',')[-1])

    def get_price(self):
        # Price
        print('Block 3 (Price): ' + self.data.find(name='div', attrs={'style': 'font-size:24px'}).find('span').text[2:])

    def get_date_added(self):
        # Date added
        print('Block 4 (Date added): ' + self.data.find(text=re.compile('Added on')).text)

    def get_property_type(self):
        # Property type
        print('Block 5 (Property type): ' + self.data.find(text='PROPERTY TYPE').find_parent(name='div').find_parent(
            name='div').find_next_sibling(name='div').text)

    def get_bedrooms(self):
        # Bedrooms
        print('Block 6 (Bedrooms): ' +
              self.data.find(text='BEDROOMS').find_parent(name='div').find_parent(name='div').find_next_sibling(
                  name='div').text[
                  -1])

    def get_bathrooms(self):
        # Bathrooms
        print('Block 7 (Bathrooms): ' +
              self.data.find(text='BATHROOMS').find_parent(name='div').find_parent(name='div').find_next_sibling(
                  name='div').text[
                  -1])

    def get_tenure(self):
        # Tenure
        print(
            'Block 8 (Tenure): ' + self.data.find('button', attrs={'aria-label': re.compile('tenure')}).find_next(
                'p').text)
