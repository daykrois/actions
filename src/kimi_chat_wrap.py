import json
import requests

from get_token import get_token


url = 'https://kimi.moonshot.cn/api/chat/co7u8recp7f6lq3osvv0/completion/stream'

# 获取access_token
access_token,refresh_token = get_token()

def kimi_chat(content):
    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Authorization": "Bearer " + access_token,
        "Referer": "https://kimi.moonshot.cn/chat/co7u8recp7f6lq3osvv0",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36 Edg/123.0.0.0"
    }
    data = {
        "messages": [
            {
                "role": "user",
                "content": content
            }
        ],
        "refs": [],
        "use_search": False
    }
    # 初始化一个空列表来存储事件数据
    collected_events = []
    # 这是一个server send events 流式数据
    response = requests.post(url, headers=headers,json=data,stream=True)
    if response.iter_content(1024):
        for event in response.iter_lines():
            event = event.decode('utf-8').strip()
            if event:
                event = event.replace('data: ', '', 1)
                json_data = json.loads(event)
                if 'text' in json_data:
                    collected_events.append(json_data['text'])

    reply = ''.join(collected_events)
    return reply
