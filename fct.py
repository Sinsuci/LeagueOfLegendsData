import requests
from bs4 import BeautifulSoup
import re



def clean_txt(a) :
    chara_delete = ["\n","\r"," ","%"]
    for z in chara_delete :
        a = a.replace(z,"")
    return a

def winrateTO100(a) :
    entier = int(float(a)*100)
    deci = (int(float(a)*1000) - entier*10) / 10
    wr = entier + deci
    return wr

