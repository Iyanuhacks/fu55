import sys
import os
import time
import pyfiglet
import colorama
import json
import requests
from colorama import Fore, Back, Style
result = pyfiglet.figlet_format("AIT", font = "slant")
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
# Function for implementing the loading animation
def load_animation():
  
    # String to be displayed when the application is loading
    load_str = "starting your AIT console application..."
    ls_len = len(load_str)
  
  
    # String for creating the rotating line
    animation = "|/-\\"
    anicount = 0
      
    # used to keep the track of
    # the duration of animation
    counttime = 0        
      
    # pointer for travelling the loading string
    i = 0                     
  
    while (counttime != 100):
          
        # used to change the animation speed
        # smaller the value, faster will be the animation
        time.sleep(0.075) 
                              
        # converting the string to list
        # as string is immutable
        load_str_list = list(load_str) 
          
        # x->obtaining the ASCII code
        x = ord(load_str_list[i])
          
        # y->for storing altered ASCII code
        y = 0                             
  
        # if the character is "." or " ", keep it unaltered
        # switch uppercase to lowercase and vice-versa 
        if x != 32 and x != 46:             
            if x>90:
                y = x-32
            else:
                y = x + 32
            load_str_list[i]= chr(y)
          
        # for storing the resultant string
        res =''             
        for j in range(ls_len):
            res = res + load_str_list[j]
              
        # displaying the resultant string
        sys.stdout.write("\r"+res + animation[anicount])
        sys.stdout.flush()
  
        # Assigning loading string
        # to the resultant string
        load_str = res
  
          
        anicount = (anicount + 1)% 4
        i =(i + 1)% ls_len
        counttime = counttime + 1
      
    # for windows OS
    if os.name =="nt":
        os.system("cls")
          
    # for linux / Mac OS
    else:
        os.system("clear")
  
# Driver program
if __name__ == '__main__': 
    load_animation()
  
   
# Your API key, available from your account page
YOUR_GEOLOCATION_KEY = '707d2d78a8434919990183169e47248f'


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

