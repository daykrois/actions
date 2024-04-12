import requests


# 获取天气信息
def get_weather_info(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }
    response = requests.get(url,headers=headers)
    if(response.status_code == 200):
        return response.text
    else:
        return "获取天气信息失败"