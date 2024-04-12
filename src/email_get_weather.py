from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib

from kimi_chat_wrap import kimi_chat
from weather import get_weather_info


# 发送邮箱账号
sender = os.getenv('email_username')
# 接受邮箱账号
receivers = [sender]

smtp_server = 'smtp.qq.com'
smtp_port = 587
smtp = smtplib.SMTP(smtp_server, smtp_port)
smtp.starttls()
# 邮箱授权码
email_code = os.getenv('email_code')
smtp.login(sender, email_code)

message = MIMEMultipart()
message['From'] = sender
message['To'] = ','.join(receivers) 
message['Subject'] = '天气预报'
url = 'https://wttr.in/tianjin?T&lang=zh-cn&format=j1'
html_content = get_weather_info(url)
get_weather = '通过下面的json帮我总结一下今天、明天、后天的天气详情'
reply = kimi_chat(get_weather + html_content)
email_content = MIMEText(reply)
message.attach(email_content)
smtp.sendmail(sender, receivers, message.as_string())
smtp.quit()