from cgitb import text
from urllib import request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import csv


url = 'https://registrar.web.baylor.edu/exams-grading/fall-2022-final-exam-schedule'
# Request in case 404 Forbidden error
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3'}


req = Request(url,headers=headers)

webpage =  urlopen(req).read()

soup = BeautifulSoup(webpage,"html.parser")

table = soup.findAll("table")

final_tables = table[1]

all_rows = final_tables.findAll('tr')

myclasses_file = open('class.csv','r')
myclasses = csv.reader(myclasses_file,delimiter='0')

for rec in myclasses:
    day = rec[0]
    time = rec[1]

for row in all_rows:
    cell = row.findAll('cell')
    if cell:
        sch_day = cell[0].text
        sch_time = cell[1].text
        sch_exam_day = cell[2].text
        sch_exam_time = cell[3].text

    if day == sch_day and sch_time == time:
        print(f"Exam Day: {sch_exam_day} for class: {day}")
        print(f"Exam Time: {sch_exam_time} for class: {time}")
        print()
    input()


