# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 16:49:58 2018

@author: lenovo
"""

import urllib.request as r
import json
city=input("请输入地名")
address="http://api.openweathermap.org/data/2.5/forecast?q={},cn&mode=json&lang=zh_cn&&APPID=6a67ed641c0fda8b69715c43518b6996&units=metric" 
#获取网页信息
info=r.urlopen(address.format(city)).read().decode('utf-8','ignore')
#转化为json文件
data=json.loads(info)
all_data=[]
for i in range(38):
    date=data["list"][i]["dt_txt"]
    temp=data["list"][i]["main"]["temp"]
    temp_max=data["list"][i]["main"]["temp_max"]
    temp_min=data["list"][i]["main"]["temp_min"]
    pressure=data["list"][i]["main"]["pressure"]
    test="日期"+str(date)+"\n","当前温度"+str(temp)+"\n","最高温度"+str(temp_max)+"\n","最低温度"+str(temp_min)+"\n","气压"+str(pressure)
    all_data.append(test)
print(all_data)
print(all_data[3],all_data[10],all_data[17])


