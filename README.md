# TelegramClone

一个将Telegram导出的聊天记录转换为WeClone项目所支持的csv格式的脚本。

食用方法：

将该脚本置于TG聊天数据的根目录

根目录文件大致为

├─chats 

├─css

├─images

├─js

├─.....



打开python脚本，更改第8行 my_name = "" 将你的Telegram名称填入引号中（不要填入TG用户名，而是填入TG昵称）。

安装依赖

pip install beautifulsoup4

运行即可。



运行后会在chats目录中，chat_01等文件夹内生成 export_weclone.csv 文件，将整个 chats 文件夹内的内容放入WeClone项目的 .\dataset\csv 文件夹中即可。

随后在WeClone项目中处理数据即可。

weclone-cli make-dataset