#!/usr/bin/env python3

import os
import time
import json
import requests
import pyperclip

API_KEY = os.environ.get('API_KEY')
# API_KEY = ""


def google_url_shorten(url):
    req_url = "https://www.googleapis.com/urlshortener/v1/url?" + str(API_KEY)
    payload = {'longUrl': url}
    headers = {'content-type': 'application/json'}
    r = requests.post(req_url, data=json.dumps(payload), headers=headers)
    resp = json.loads(r.text)
    return resp["id"]


recent_value = ""
while True:
    tmp_value = pyperclip.paste()
    if (tmp_value != recent_value and not tmp_value.startswith("https://goo.gl") and not tmp_value.startswith("https://git")):
        recent_value = tmp_value
        url = str(recent_value)
        if url.startswith("http://") or url.startswith("https://") or url.startswith("www."):
            pyperclip.copy(google_url_shorten(url))
    time.sleep(0.5)
