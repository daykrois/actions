from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import requests

from kimi_chat_wrap import kimi_chat


url = 'https://wttr.in/tianjin?T&lang=zh-cn&format=j1'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}
def get_weather_info(url):
    response = requests.get(url,headers=headers)
    if(response.status_code == 200):
        return response.text
    else:
        return "获取天气信息失败"

sender = os.getenv('email_username')
receivers = [sender]

smtp_server = 'smtp.qq.com'
smtp_port = 587
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()
email_code = os.getenv('email_code')
smtp.login(sender, email_code)

message = MIMEMultipart()
message['From'] = sender
message['To'] = ','.join(receivers) 
message['Subject'] = '天气预报'

html_content = get_weather_info(url)
get_weather = '通过下面的json帮我总结一下今天、明天、后天的天气详情'
reply = kimi_chat(get_weather + html_content)
html_part = MIMEText(reply)
message.attach(html_part)
smtp.sendmail(sender, receivers, message.as_string())
smtp.quit()