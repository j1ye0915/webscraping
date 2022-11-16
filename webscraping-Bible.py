from http import client
from multiprocessing.connection import Client
import random
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

#https://ebible.org/asv/JHN05.htm

random_chapter = random.randint(1,21)

if random_chapter < 10:
    random_chapter = '0' + str(random_chapter)
else:
    random_chapter = str(random_chapter)

webpage = 'https://ebible.org/asv/JHN' + random_chapter + '.htm'

print(webpage)

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}
req = Request(webpage, headers=headers)



webpage = urlopen(req).read()

soup = BeautifulSoup(webpage, "html.parser")

page_verses = soup.findAll('div',class_='p')

verse_list = []

for verse in page_verses:
    verse_list = verse.text.split('.')


myverse = 'Chapter:' + random_chapter + 'Verse:' + random.choice(verse_list[:len(verse_list)-2])



import keys2
from twilio.rest import Client

client = Client(keys2.accountSID,keys2.authToken)

TwilioNumber = "+12548700820"
myNumber = "+12547152277"

textmsg = client.messages.create(to=myNumber,from_=TwilioNumber,body=myverse)

print(textmsg.status)