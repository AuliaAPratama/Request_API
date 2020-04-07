'''
API kurs mata uang
'''

import requests    
kode = input('ketik bank: ')
data = requests.get(f'https://kurs.web.id/api/v1/{kode}')
data1 = requests.get('https://blockchain.info/ticker')
error_code = data.json()['error']

if error_code == 'true':
    print('bank tidak ada')
else:
    print('1.USD>IDR\n2.IDR>USD\n3.USD>Bitcoin\n4.Bitcoin>USD\n5.IDR>Bitcoin\n6.Bitcoin>IDR')
    quest = int(input('masukan 1/2/3/4/5/6: '))
    kurs_jual = float(data.json()['jual'])
    kurs_beli = float(data.json()['beli'])
    value = data1.json()['USD']['buy']
    if quest == 1:
        nominal = float(input('masukan nominal USD: '))
        convert_result = (nominal * kurs_jual)
        print(f'{nominal} USD = Rp {round(convert_result,2)}')
        print(f'{kode.upper()}: kurs jual = {kurs_jual} dan kurs beli = {kurs_beli}')
    elif quest == 2:
        nominal = float(input('masukan nominal Rp: '))
        convert_result = (nominal / kurs_beli)
        print(f'{nominal} Rp = USD {round(convert_result,2)}')
        print(f'{kode.upper()}: kurs jual = {kurs_jual} dan kurs beli = {kurs_beli}')
    elif quest == 3:
        nominal = float(input('masukan nominal USD: '))
        convert_result = (nominal / value)
        print(f'{nominal} USD = Bitcoin {convert_result}')
    elif quest == 4:
        nominal = float(input('masukan nominal Bitcoin: '))
        convert_result = (nominal * value)
        print(f'{nominal} Bitcoin = USD {convert_result}')
    elif quest == 5:
        nominal = float(input('masukan nominal IDR: '))
        idr_to_usd = (nominal/kurs_beli)
        convert_result = (idr_to_usd/value)
        print(f'{nominal} IDR = Bitcoin {convert_result}')
    elif quest == 6:
        nominal = float(input('masukan nominal Bitcoin: '))
        bit_to_usd = (nominal*kurs_jual)
        convert_result = (bit_to_usd*value)
        print(f'{nominal} Bitcoin = IDR {convert_result}')
    else:
        print('tidak ada menu pilihan') 
  