import time
from unicodedata import name
import psutil #pip install psutil
import pypresence #pip install pypresence
import json
with open ("rpc.json", encoding="utf-8") as rpcdata:
    rpc_data=json.load(rpcdata)
rpc = pypresence.Presence(int(rpc_data["id"]))
data = None
rpc.connect()
exe=["excel.exe"]#自己添加要註冊的遊戲或應用程序，詳細名稱可在test.py取得
while True:
    for proc in psutil.process_iter():
        for i in exe:
            if i == proc.name().lower():
                data=rpc_data["rpc_index"][i]
    if data:
        rpc.update(**data)
    else:
        rpc.update(**rpc_data["rpc_index"]["event"], buttons=[rpc_data["rpc_button"]])#預設狀態
    time.sleep(10)
    
