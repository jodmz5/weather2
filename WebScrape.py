import requests
from bs4 import BeautifulSoup as bs
from write import turtlefun
from datetime import date

weatherURL="https://weather.com/weather/today/l/dfce35747a4e6e70de0e4883cfaecf6ae21820b2979ba9e1e3e16192cabdbdef"
pageweather=requests.get(weatherURL)
soup=bs(pageweather.content,'html5lib')

UURL='https://markets.businessinsider.com/commodities/uranium-price'
pageU=requests.get(UURL)
soup2=bs(pageU.content,'html5lib')

#Real Temperature
real=str(soup.find(class_='today_nowcard-temp'))
temp=real.replace('<div class="today_nowcard-temp"><span class="">','')
tempreal=int(temp.replace('<sup>°</sup></span></div>',''))
print(tempreal)
#Feels Like Temperature
feels=str(soup.find(class_='deg-feels'))
feels1=feels.replace('<span class="deg-feels" classname="deg-feels">','')
tempfeels=int(feels1.replace('<sup>°</sup></span>',''))
print(tempfeels)
#Uranium Price
price=str(soup2.find(class_='push-data'))
price1=price.replace('<span class="push-data" data-animation="animationType:background" data-format="minimumFractionDigits:2;maximumFractionDigits:2" data-jsvalue="0.0000">','')
priceUlbs=float(price1.replace('</span>',''))
priceUkg1=(priceUlbs*(1/0.453592))
priceUkg=round(priceUkg1,2)
print(priceUkg)

today=date.today()
d1=today.strftime("%m/%d/%Y")
print(d1)

turtlefun(tempreal,tempfeels,priceUkg,d1)
