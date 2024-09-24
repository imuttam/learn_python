import requests
import json

BASE_URL = 'https://bhagavadgitaapi.in/slok'

chapter = int(input('Enter chapter: '))
slok = int(input('Enter slok: '))

response = requests.get(f'{BASE_URL}/{chapter}/{slok}')

json_data = json.loads(response.content.decode('utf-8'))

verse = json_data['slok']
meaning = json_data['chinmay']
sankar = json_data['sankar']

print(verse)
print()
print(meaning)
print(sankar)
