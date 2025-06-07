import os
import csv
from bs4 import BeautifulSoup
from datetime import datetime

# 配置
base_dir = './chats'  # 你的chats文件夹路径
my_name = ""   # 你在Telegram里的用户名

# 遍历整个 chats 目录
for chat_folder in os.listdir(base_dir):
    chat_path = os.path.join(base_dir, chat_folder)
    if not os.path.isdir(chat_path):
        continue

    data = []
    idx = 1

    for file in os.listdir(chat_path):
        if file.startswith('messages') and file.endswith('.html'):
            file_path = os.path.join(chat_path, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                soup = BeautifulSoup(f, 'html.parser')

            messages = soup.find_all("div", class_="message")

            for message in messages:
                if 'service' in message.get('class', []):
                    continue

                from_name_tag = message.find("div", class_="from_name")
                text_tag = message.find("div", class_="text")
                date_tag = message.find("div", class_="pull_right date details")

                if not from_name_tag or not text_tag or not date_tag:
                    continue

                speaker = from_name_tag.get_text(strip=True)
                text = text_tag.get_text(strip=True)
                timestamp = date_tag['title']

                time_obj = datetime.strptime(timestamp.split(' ')[0] + ' ' + timestamp.split(' ')[1], '%d.%m.%Y %H:%M:%S')
                time_str = time_obj.strftime('%Y-%m-%d %H:%M:%S')

                is_sender = 1 if speaker == my_name else 0

                data.append({
                    'id': idx,
                    'MsgSvrID': '',  # Telegram 没有，置空
                    'type_name': '文本',
                    'is_sender': is_sender,
                    'talker': '',     # Telegram 没有，置空
                    'room_name': '',  # Telegram 没有，置空
                    'msg': text,
                    'src': '',        # Telegram 没有，置空
                    'CreateTime': time_str
                })

                idx += 1

    # 仅在有数据时保存csv
    if data:
        output_file = os.path.join(chat_path, 'export_weclone.csv')
        with open(output_file, 'w', encoding='utf-8', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=['id', 'MsgSvrID', 'type_name', 'is_sender', 'talker', 'room_name', 'msg', 'src', 'CreateTime'])
            writer.writeheader()
            writer.writerows(data)

        print(f"{chat_folder}: 已保存 {len(data)} 条记录到 {output_file}")
