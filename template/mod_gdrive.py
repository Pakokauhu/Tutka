#!/usr/bin/env python3
import os
import utils

R = '\033[31m' # punainen
G = '\033[32m' # vihreä
C = '\033[36m' # syväsininen
W = '\033[0m'  # valkoinen

redirect = os.getenv('REDIRECT')

if redirect is None:
    redirect = input(G + '[+]' + C + ' Syötä GDrive-tiedoston URL : ' + W)
else:
    utils.print(f'{G}[+] {C}GDrive-tiedoston URL :{W} ' + redirect)
        
with open('template/gdrive/index_temp.html', 'r') as temp_index:
    temp_index_data = temp_index.read()
    temp_index_data = temp_index_data.replace('REDIRECT_URL', redirect)
    if os.getenv("DEBUG_HTTP"):
        temp_index_data = temp_index_data.replace('window.location = "https:" + restOfUrl;', '')

with open('template/gdrive/index.html', 'w') as updated_index:
    updated_index.write(temp_index_data)
