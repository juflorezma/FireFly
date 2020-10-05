import requests
import random 

num = random.randint(0,1)

token = '1174140518:AAFcd69FXAcW4yr1ss4RoC7Mxc2IT7o-UP8'
url = f'https://api.telegram.org/bot{token}/getUpdates'

dic=requests.post(url).json()

lon = dic['result'][len(dic['result'])-1]['message']['location']['longitude']
lat = dic['result'][len(dic['result'])-1]['message']['location']['latitude']
id = dic['result'][len(dic['result'])-1]['message']['from']['id']

url = f'https://api.telegram.org/bot{token}/sendMessage'

if num ==0:
    text = 'Cerca a tu ubicacion(Longitud:'+ str(lon) + ', Latitude:'+ str(lat) +'), no hay un incendio'
else:
    noice1 = random.gauss(lon, 0.001)
    noice2 = random.gauss(lat, 0.001)
    text = 'Cerca a tu ubicacion(Longitud:'+ str(lon) + ', Latitude:'+ str(lat) +'), hay un incendio en las coordenadas: Longitud: '+ str(lon+noice1)+' y Latitud: '+str(lat+noice2)
data = {'chat_id':id , 'text': text}
requests.post(url, data).json()
