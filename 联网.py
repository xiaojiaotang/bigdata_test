# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:49:58 2018

@author: lenovo
"""

import urllib.request as r
import json
city=input("请输入")
address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996"
#获取网页信息
info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
#转化为json文件
data=json.loads(info)
print(data)
id=data["weather"][0]["id"]
temp=data["main"]["temp"]
temp_max=data["main"]["temp_max"]
pressure=data["main"]["pressure"]
print("用户"+str(id)+"\n","当前温度"+str(temp),"最高温度"+str(temp_max),"气压"+str(pressure))