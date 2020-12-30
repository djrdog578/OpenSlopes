from bs4 import BeautifulSoup
import requests
#https://opensnow.com/state

state = input("Type the abbreviation of the state you're looking in: ")

for i in state:
    source = requests.get("https://opensnow.com/state/" + state).text
    soup = BeautifulSoup(source, 'lxml')
    
name = input('What Slope are you looking for? ')
name = name.title()

status = soup.find(text=name).findNext(text='Status: ').findNext('span').text
snowFall = soup.find(text=name).find_next('div', {'class' : 'text highsnow'}).text

def remove(string): 
    return string.replace(" ", "")

print("This Resort Is: " + status)
print("It's getting" + remove(snowFall) + "Inches of snow in the next 5 days")

