#!/usr/bin/env python3
import requests
import uuid
import sys
import re
import builtins

def lataaKuvaUrlista(url, polku):
    if not url.startswith('http'):
        return None
    kuvan_data = requests.get(url).content
    tiedostonPolku = polku + '/' + str(uuid.uuid1()) + '.jpg'
    with open(tiedostonPolku, 'wb') as kasittelija:
        kasittelija.write(kuvan_data)
    return tiedostonPolku

def tulosta(teksti, **args):
    if sys.stdout.isatty():
        builtins.print(teksti, flush=True, **args)
    else:
        builtins.print(re.sub(r'\33\[\d+m', ' ', teksti), flush=True, **args)
