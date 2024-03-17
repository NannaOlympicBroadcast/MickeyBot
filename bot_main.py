import os
import random
import sys
import time

from botpy.message import DirectMessage
import botpy
from botpy.types.message import Message
import psutil
import mickey
from io import StringIO

piclist = ["R-C.jpg", "R-C (1).jpg", "R-C (2).jpg", "22fb-1c9a28967bf92453bff2669842119cc1.jpg"]

def remove_first_line_from_string(s):
    """
    去除多行字符串的第一行并返回剩余的字符串。

    参数:
    s (str): 输入的多行字符串。

    返回:
    str: 去除第一行后的字符串。
    """
    lines = s.splitlines()  # 将字符串分割成行列表
    remaining_lines = lines[1:]  # 去除第一行
    return '\n'.join(remaining_lines)  # 将剩余的行重新组合成一个字符串并返回

class MyClient(botpy.Client):
    async def on_direct_message_create(self, message: DirectMessage):
        words = message.content
        if len(message.attachments) > 0:
            print("with attachments:" + message.attachments)
        res = mickey.mickey_mouse(words)
        print("Private message " + message.id + " got response:" + res)
        await self.api.post_dms(guild_id=message.guild_id, content=res)

    async def on_at_message_create(self, message: Message):
        msg = str(message.content)
        if len(message.attachments) > 0:
            print("with attachments:" + message.attachments)
        index = msg.index(">")
        words = msg[index + 2:len(msg)]
        print("Message Received:" + words)
        if "/memorycheck" in words:
            mem_info = psutil.virtual_memory()
            res = "总内存：" + str(round(mem_info.total / (1024 ** 3), 2)) + "\n" + "已用内存：" + str(round(
                mem_info.used / (1024 ** 3), 2)) + "(" + str(
                round(100 * mem_info.used / mem_info.total, 2)) + "%)\n" + "CPU使用率：" + str(
                psutil.cpu_percent(interval=1))
            await self.api.post_message(channel_id=message.channel_id, content=res)
        elif "米斯卡，莫斯卡" in words or "/今日运势" in words:
            res = mickey.lucky_today()
            await self.api.post_message(channel_id=message.channel_id, content=res, file_image=random.choice(piclist))
        elif "/摸一摸" in words:
            res=mickey.touch_head()
            await self.api.post_message(channel_id=message.channel_id, content=res)
        elif "/Hello" in words:
            res=mickey.mickey_mouse("你好")
            await self.api.post_message(channel_id=message.channel_id, content=res, file_image=random.choice(piclist))
        elif "/CodeRunner" in words:
            code_str=remove_first_line_from_string(msg)
            os.chdir("./env")
            output = StringIO()
            err = StringIO()
            sys.stdout=output
            sys.stderr=err
            try:
                t1 = int(round(time.time() * 1000))
                exec(code_str)
                t2 = int(round(time.time() * 1000))
                res = "Running Finished in " + str(
                    t2 - t1) + "ms!\n遵守社区公约，禁止运行恶意代码\n结果为：\n" + output.getvalue()
                sys.stdout = sys.__stdout__
                sys.stderr = sys.__stderr__
                os.chdir("..")
                await self.api.post_message(channel_id=message.channel_id, content=res)
            except Exception as e:
                res="An error occurred!\n"
                sys.stdout = sys.__stdout__
                sys.stderr = sys.__stderr__
                os.chdir("..")
                await self.api.post_message(channel_id=message.channel_id, content=res+e.__class__.__name__)
        elif "/terminal" in words:
            os.chdir("./env")
            a = os.popen(words[words.index(" ")+1:])  # 使用a接收返回值
            res=a.read()
            os.chdir("..")
            await self.api.post_message(channel_id=message.channel_id, content="Results:\n"+res)# 读取输出内容
        else:
            res = mickey.mickey_mouse(words)
            await self.api.post_message(channel_id=message.channel_id, content=res)

intents = botpy.Intents(public_guild_messages=True, audio_action=True, direct_message=True)
client = MyClient(intents=intents)
client.run(appid="102087567", secret="dGuYCqU8mQ5kP4jO3iN3jP5lR7nTArYF")
