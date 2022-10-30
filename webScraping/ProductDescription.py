import requests
from bs4 import BeautifulSoup
import re
import csv

AllContents = requests.get('https://www.amazon.in/uppercase-Backpack-2500EBP1-repellent-sustainable/dp/B0B81YTTWS/ref=sr_1_1_sspa?crid=2M096C61O4MLT&keywords=bags&qid=1667138408&qu=eyJxc2MiOiI4LjAzIiwicXNhIjoiOC4wNSIsInFzcCI6IjYuNzUifQ%3D%3D&sprefix=ba%2Caps%2C283&sr=8-1-spons&th=1')

AllContent = BeautifulSoup(AllContents.content, 'html.parser')

ProductDiscription = AllContent.find_all(id='productDescription', string = re.compile('BackPack | Bag | bag | backPack '))



List = AllContent.find_all(id = 'detailBullets_feature_div')

Manufacture = AllContent.find('span', string = re.compile('Private | Pvt'))

ASIN = AllContent.find('span', string=re.compile('B0'))

productDescription = []

for i in ProductDiscription:
    productDescription.append(ProductDiscription)

productManufacture = []

productManufacture.append(Manufacture.text)

productAsin = []

productAsin.append(ASIN.text)



result = list(map(lambda a,b,c: [a,b,c], productDescription, productManufacture, productAsin))
title = ['Product Description', 'Manufacturer', 'ASIN']
print(result)


myFile = open('AmazonProductDescription.csv', 'w', newline='')
writer = csv.writer(myFile)
writer.writerows([title])
writer.writerows(result)

myFile.close()
myFile = open('AmazonProductDescription', 'r')
print("The content of the csv file is:")
print(myFile.read())
myFile.close()
