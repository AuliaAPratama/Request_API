'''
python get request => API
urllib
requests
'''


'''
API to py
'''
# import requests
# url = 'http://jsonplaceholder.typicode.com/users'
# data = requests.get(url)
# print(data.json())
# print(type(data.json()))
# print(data.json()[::1])

'''
import data
'''
# import requests
# url = 'http://jsonplaceholder.typicode.com/users'
# data = requests.get(url)
# for i in data.json():
#     print(i['name'], 'lives in',i['address']['street'],'street')

'''
import by inputuser
'''
# import requests    
# klub = input('ketik klub: ')
# url = f'https://www.thesportsdb.com/api/v1/json/1/searchplayers.php?t={klub}'
# data = requests.get(url)
# players = data.json()['player']

# for name in players:
#     print(f"{name['strPlayer']} ({name['strPosition']})")

'''
import quotes
'''
# import requests
# url = 'http://quotes.rest/qod'
# data = requests.get(url)
# data = data.json()
# # print(data)
# print(data['contents']['quotes'][0]['quote'])

'''
import api & time
'''
# import requests
# x = '&appid=5a227057226696174b961d9b02fd5502'
# y = input('Ketik kota: ')
# url = f'http://api.openweathermap.org/data/2.5/weather?q={y}{x}'
# data = requests.get(url)
# data = data.json()
# sunrise = data['sys']['sunrise']
# sunset = data['sys']['sunset']

# from datetime import datetime
# from dateutil import tz
# myzone = tz.gettz('Asia/Jakarta')
# utc = datetime.utcfromtimestamp(int(sunrise))
# print(int(utc.strftime('%d'))+1)
# print(int(utc.strftime('%H'))+7)

