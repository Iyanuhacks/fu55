import time
import pyfiglet
import colorama
import json
import requests
from colorama import Fore, Back, Style
result = pyfiglet.figlet_format("annoyingiptracker", font = "slant")
print(Fore.BLUE,result)
print(Fore.GREEN)
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("                   \n about: annoying_iptracker \n             ")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
print("created by:iyanuhacks")
print("github:https://github.com/iyanuhacks")
print("team :naija-Anon-Force")
print("team github:https://github.com/iyanuhacks/Naija-Anon-Force/")
print("whatsapp:07040435646")
print(Fore.RED)
input("enter [Y/N] for open console or back: ")
# Your API key, available from your account page
YOUR_GEOLOCATION_KEY = '707d2d78a8434919990183169e47248f'

# IP address 
ip_address = input("input ip address of victim:")

response = requests.get('https://ipgeolocation.abstractapi.com/v1/?api_key=' + YOUR_GEOLOCATION_KEY + '&ip_address=' + ip_address)
result = json.loads(response.content)
print("City:" + result ['city'])
print("city_geoname_id:")
print(result ['city_geoname_id'])
print("region:" + result ['region'])
print("region_iso_code:" + result ['region_iso_code'])
print("region-geoname_id:")
print(result ['region_geoname_id'])
print("postal_code:" + result ['postal_code'])
print("country:" + result  ['country'])
print("country_code:" + result  ['country_code'])
print("country_geoname_id:")
print(result ['country_geoname_id'])
print("country_is_eu:")
print(result ['country_is_eu'])
print("continent:" + result ['continent'])
print("continent_code:" + result  ['continent_code'])
print("continent_geo_id:")
print(result  ['continent_geoname_id'])
print("longitude:")
print(result ['longitude'])
print("latitude:")
print(result ['latitude'])
print( result ['security'])
print( result ['timezone'])
print( result ['flag'])
print( result ['currency'])
print( result ['connection'])

