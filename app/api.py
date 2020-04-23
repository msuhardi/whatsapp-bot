# app/api.py

from app import app

import http.client
import json
import requests

ENCODING_FORMAT = 'utf-8'

# Covid-19 API Connection Object
COVID_API_URL = 'covid-193.p.rapidapi.com'
conn = http.client.HTTPSConnection(COVID_API_URL)
headers = {
    'x-rapidapi-host': COVID_API_URL,
    'x-rapidapi-key': app.config['RAPID_API_KEY']
}

SURABAYA_COVID_API_URL = 'https://analytics.surabaya.go.id'
SURABAYA_COVID_API_ENDPOINT = '/api/public/dashboard/797390d1-16ca-4cc0-878e-3171ca57c19e/card/'
DATA_MAP = {
    '266': 'Kumulatif Konfirmasi',
    '272': 'Konfirmasi Dalam Perawatan',
    '278': 'Konfirmasi Meninggal',
    '275': 'Konfirmasi Sembuh'
}
SURABAYA_AREA_CASE_ID = '194'

def get_stats(country):
    conn.request("GET", "/statistics?country=% s"% country, headers=headers)
    res = conn.getresponse()

    if res.status == 200:
        data = res.read().decode(ENCODING_FORMAT)
        json_result = json.loads(data)

        return json_result

    return None

def get_surabaya_stats():
    result = {}

    for id in DATA_MAP.keys():
        r = requests.get(url = "% s% s% s"% (SURABAYA_COVID_API_URL, SURABAYA_COVID_API_ENDPOINT, id))
        data = r.json()

        if data:
            stats = data["data"]["insights"][0]
            result[DATA_MAP[id]] = { 
                "last_value": stats["last-value"],
                "previous_value": stats["previous-value"],
                "change": stats["last-change"]
            }    
        
    return result        