from bs4 import BeautifulSoup as bs 
import pandas as pd
import requests

urlopen = requests.get('https://www.trendyol.com/kadin-gunluk-ayakkabi-x-g1-c1352').text

soup = bs(urlopen,'html.parser')


productPrice = soup.find_all("div", class_= "prc-box-sllng prc-box-sllng-w-dscntd")
productPriceList = []
for i in productPrice:
    productPriceList.append(i.text)


productName = soup.find_all("span", class_= "hasRatings")
productNameList = []
for i in range(len(productPriceList)):
    productNameList.append(productName[i].text)

table_dict = {'Product_name': productNameList, 'Product_price': productPriceList}

# as table
df = pd.DataFrame(table_dict)

# save to file
df.to_json('trendyol-products.json', orient='records')

