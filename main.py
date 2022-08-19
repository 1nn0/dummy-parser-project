# RightMove parser alpha

import requests
import bs4
from property_scraper import PropertyData
from pathlib import Path

# headers = {
#    "Accept" : "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
#    "Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
# }

# url = 'https://www.rightmove.co.uk/property-for-sale/find.html?minBedrooms=1&maxBedrooms=1&includeSSTC=false&keywords=&sortType=1&viewType=LIST&channel=BUY&index=0&radius=0.0&locationIdentifier=REGION%5E87490'
# sapmle_property_url = 'https://www.rightmove.co.uk/properties/125852372#/?channel=RES_BUY'

# r = requests.get(url=url, headers = headers)

# with open('result.htm', 'wb') as file:
#    file.write(r.content)

# r = requests.get(url=sapmle_property_url, headers = headers)

# with open('result_property.htm', 'wb') as file:
#   file.write(r.content)

# print(headers)


property_html = Path('result_property.htm')

test_dataclass = PropertyData(property_html)
print(test_dataclass.get_address())
test_dataclass.get_price()


def main():
    pass


if __name__ == '__main__':
    main()
