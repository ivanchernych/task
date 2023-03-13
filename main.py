import sys
from io import BytesIO
import requests
from PIL import Image
from getting_coordinates import getting

symbol = ';'

print(f'адрес и SPN нужно вводит в одну строку через знак {symbol}')

ss = ' '.join(sys.argv[1:]).split(symbol)
toponym_to_find = ss[0]

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "40d1649f-0493-4b70-98ba-98533de7710b",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)

if not response:
    pass

tompony = getting(response)


map_params = {
    "ll": ",".join(tompony),
    "spn": ",".join(ss[1].split()),
    "l": "map",
    'pt': ",".join(tompony + ['pm2rdm'])
}

map_api_server = "http://static-maps.yandex.ru/1.x/"
response = requests.get(map_api_server, params=map_params)

Image.open(BytesIO(
    response.content)).show()
