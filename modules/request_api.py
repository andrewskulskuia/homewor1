import requests
#підключаемо read_json
from .read_json import read_json
#підключаемо json
import json
#
data_api = read_json(name_file= 'config_api.json')
#ми робимо щоб api_key був API_KEY
API_KEY = data_api['api_key']
#ми робимо щоб city_name був CITY_NAME
CITY_NAME = data_api['city_name']
#це наша можна сказати бібліотука з якої бере дані response
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}"
#вона робить так щоб збирати дані з URL
response = requests.get(URL)
#тут написано що якщо програма напище 200 то дані прийшли добре я якщо інще то ні
if response.status_code == 200:
    #робимо щоб  пичаталися дані 
    data_dict = json.loads(response.content)
    #а тут щоб було красиво в стовбчик
    print(json.dumps(data_dict, indent= 4))