'''
Latihan
1. get api sportsdb, daftar pemain suatu klub
2. input = klub apa? barca
3. daftar pemain : nama, posisi, usia, negara
4. save barca.xlsx, barca.json, barca.csv
'''

import requests    
klub = input('ketik klub: ')
url = f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}'
data = requests.get(url)
suatu = data.json()['player']
title = ['nama','posisi','umur','kewarganegaraan']


c = []    # bikin template
for i in suatu:
    duh = [i['strPlayer'],i['strPosition'],i['strNationality']]
    c.append(duh)
    
uzur = []  # bikin umur
for i in suatu:
    dih = (i['dateBorn'][0:4])
    lah = (2019 - int(dih))
    uzur.append(lah)
    
d = []
for i in range(len(uzur)):
    c[i].insert(2,uzur[i])

for i in c:
    d.append(dict(zip(title,i)))


import json
with open('klub.json','w')as y:
    json.dump(d,y)

import csv
with open('klub.csv','w',newline='') as x:
    kolom = title
    a = csv.DictWriter(x, fieldnames=kolom, delimiter=',')
    a.writeheader()
    a.writerows(d)

import xlsxwriter
file = xlsxwriter.Workbook('klub.xlsx')
sheet = file.add_worksheet('SheetAwal')
# write col
for i in title:
    sheet.write(0, title.index(i),i)
# write data
row = 1
for w,x,y,z in c:
    sheet.write(row,0,w)
    sheet.write(row,1,x)
    sheet.write(row,2,y)
    sheet.write(row,3,z)
    row += 1
file.close()