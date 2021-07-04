
import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://forecast.weather.gov/MapClick.php?lat=39.95222000000007&lon=-75.16217999999998#.XwK12CgzbIU')

soup = BeautifulSoup(page.content,'html.parser')

week = soup.find(id="seven-day-forecast-body")

item = week.find_all(class_= 'tombstone-container')

print(item[0].find(class_ ='period-name').get_text())
print(item[0].find(class_ ='short-desc').get_text())
print(item[0].find(class_ ='temp').get_text())

period_name = [a.find(class_ ='period-name').get_text() for a in item]
short_description = [a.find(class_ ='short-desc').get_text() for a in item]
temperature = [a.find(class_ ='temp').get_text() for a in item]

#print(period_name)
#print(short_description)
#print(temperature)


weather_stuff = pd.DataFrame(
    {'period':period_name,
     'description':short_description,
     'temp':temperature

    }
)

print(weather_stuff)


weather_stuff.to_csv('weather.csv')
