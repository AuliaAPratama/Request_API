'''
Pilih menu makanan
zomato
'''

import requests

aa = input('Selamat datang, mau makan apa saat ini? : ')
b = aa.split(' ')
makan = '%20'.join(b)


host = f'https://developers.zomato.com/api/v2.1/search?entity_id=74&entity_type=city&q={makan}'

apikey = '83deb9a6b329b4199616485b0a202bd3'
headers = {
    'user-key': apikey
}

data = requests.get(host,headers=headers)
resto = data.json()['restaurants']
for i in range(len(resto)):
    nama = resto[i]['restaurant']['name']
    locate = resto[i]['restaurant']['location']['address']
    print(f'{i+1}, Nama resto: {nama}\n Lokasi: {locate}')