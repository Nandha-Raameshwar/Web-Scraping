import requests
import re
from bs4 import BeautifulSoup
import csv

r = requests.get('https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_1')


AllContent = BeautifulSoup(r.content, 'html.parser')

ProductName = AllContent.find_all('span', class_='a-size-medium a-color-base a-text-normal')

ProductRating = AllContent.find_all('span', class_='a-icon-alt')

ProductHref = AllContent.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')

ProductDetails = []
ProductDetailsHref = []
ProductDetail = []



for row in AllContent.find_all('span', class_='a-size-medium a-color-base a-text-normal'):
        ProductDetails.append(row.text)


for i in AllContent.find_all('span', class_='a-icon-alt'):
    ProductDetail.append(i.text)

for j in ProductHref:
    ProductDetailsHref.append(j['href'])


#for k in ProductPrice:
    #ProductPriceList.append(ProductPrice.text)

'''
print(ProductDetails)
print(ProductDetail)
print(ProductDetailsHref)
'''

result = list(map(lambda a, b, c: [a, b, c], ProductDetails, ProductDetail, ProductDetailsHref))
print(result)

Title = [['Product Name'], ['Rating'], ['Link']]

myFile = open('AmazonWebScraping.csv', 'w', newline='')
writer = csv.writer(myFile)
writer.writerow(Title)
writer.writerows(result)

myFile.close()
myFile = open('AmazonWebScraping.csv', 'r')
print("The content of the csv file is:")
print(myFile.read())
myFile.close()

#Appending the Page 2++
'''import requests
import re
from bs4 import BeautifulSoup
import csv

r = requests.get('https://www.amazon.in/s?k=bags&page=2&crid=2M096C61O4MLT&qid=1667136373&sprefix=ba%2Caps%2C283&ref=sr_pg_2')


AllContent = BeautifulSoup(r.content, 'html.parser')

ProductName = AllContent.find_all('span', class_='a-size-medium a-color-base a-text-normal')

ProductRating = AllContent.find_all('span', class_='a-icon-alt')

ProductHref = AllContent.find_all('a', class_='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal')

ProductDetails = []
ProductDetailsHref = []
ProductDetail = []



for row in AllContent.find_all('span', class_='a-size-medium a-color-base a-text-normal'):
        ProductDetails.append(row.text)


for i in AllContent.find_all('span', class_='a-icon-alt'):
    ProductDetail.append(i.text)

for j in ProductHref:
    ProductDetailsHref.append(j['href'])


#for k in ProductPrice:
    #ProductPriceList.append(ProductPrice.text)


print(ProductDetails)
print(ProductDetail)
print(ProductDetailsHref)


result = list(map(lambda a, b, c: [a, b, c], ProductDetails, ProductDetail, ProductDetailsHref))
print(result)

Title = [['Product Name'], ['Rating'], ['Link']]

myFile = open('AmazonWebScraping.csv', 'a', newline='')
writer = csv.writer(myFile)
writer.writerows(result)

myFile.close()
myFile = open('AmazonWebScraping.csv', 'r')
print("The content of the csv file is:")
print(myFile.read())
myFile.close()
'''
