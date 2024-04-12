import os
import requests

# 通过refresh_token获取access_token和refresh_token
def get_token():
    refresh_token = os.getenv('refresh_token')
    get_token_url = 'https://kimi.moonshot.cn/api/auth/token/refresh'
    headers = {
        'Authorization': 'Bearer '+ refresh_token,
    }
    response = requests.get(get_token_url,headers=headers)
    access_token = response.json()['access_token']
    refresh_token = response.json()['refresh_token']
    return access_token,refresh_token
