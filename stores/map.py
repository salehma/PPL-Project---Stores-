from math import sqrt

import folium
from folium import plugins
import ipywidgets
import geocoder
import geopy
import numpy as np
import pandas as pd
import requests
import urllib.parse

# address = 'Beer Sheva, Alexander Yanai'
# url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) + '?format=json'
#
# response = requests.get(url).json()
# print((response))
# print(response[0]["lat"])
# print(response[0]["lon"])

import requests

address = 'באר שבע אלכסנדר ינאי 17'

response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address='+address+'&key=AIzaSyCLs_mIGVefgGgw8Ea3BFgQE9LtxRZux-4')

resp_json_payload = response.json()

print(resp_json_payload['results'][0]['geometry']['location'])
