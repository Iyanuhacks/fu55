import time

from colorama import Fore, Back, Style

import pyfiglet

result = pyfiglet.figlet_format("passgen v 1.0")
print(Fore.RED,result)
input("start generating  password?[Y/N]:")
print("please😫🙏🙏💓 wait")
time.sleep(4)
import string
from random import *
characters = string.ascii_letters + string.punctuation  + string.digits
password =  "".join(choice(characters) for x in range(randint(12, 16)))

print(Fore.BLUE,password)
print("password generated successfully")

about=("ABOUT:passgen is a password generator that generate password that cannot be cracked or break by brutes force,dictionary attacks and other types of password cracking tool.it is created in python by iyanuhacks")
print("if you are  having issues with this tool you can report at my GitHub repo")
print(Fore.GREEN,about)
print("N O T E:-to make sure the password work properly do not click on any phishing link.thanks the 2nd version of this tool will soon be out,it will possess many features than this and this version may be outdated" )

 
input("enter any  key 🔑 to exit:")
result = pyfiglet.figlet_format("bye👋   script  by 【I】【y】【a】【n】【u】【h】【a】【c】【k】【s】", font = "digital")
print(result)


