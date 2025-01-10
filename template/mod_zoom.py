#!/usr/bin/env python3
import os
import utils

R = '\033[31m'  # punainen
G = '\033[32m'  # vihreä
C = '\033[36m'  # syväsininen
W = '\033[0m'   # valkoinen

with open('template/zoom/index_temp.html', 'r') as temp_index:
    temp_index_data = temp_index.read()
    if os.getenv("DEBUG_HTTP"):
        temp_index_data = temp_index_data.replace('window.location = "https:" + restOfUrl;', '')

with open('template/zoom/index.html', 'w') as updated_index:
    updated_index.write(temp_index_data)
