# -*- coding: utf-8 -*-
"""
Created on Sat Jun  2 15:08:34 2018

@author: lenovo
"""

msg={"地址":"四川省乐山市。。。",
 "手机号码":"1526555546",
 "寄信人":"yabgs"}
print(msg["地址"])
print(msg["手机号码"])
print(msg["寄信人"])

people={"name":"xiaoming",
        "high":"165",
        "age":"21",
        "sex":"man"
        }
print(people["name"])
print(people["high"])
print(people["age"])
print(people["sex"])



xzq={"name":"xuezhiqian",
     "songs":["1","2","3","4"],
     "nicheng":"xiaoxue",
     "renshiguodegirl":"ksh"}
songs=xzq["songs"]
print(songs)
print(len(songs))
print(max(xzq["songs"]))



weath={"天气":["小雨","多云","晴朗","暴雨","晴朗"],
        "温度":[12,15,11,16,14],
        "日期":["星期一","星期二","星期三","星期四","星期五"]}
 

print(weath["天气"])
print(max(weath["温度"])) 


city=input("请输入")
print(city)
address="http://api.openweathermap.org/data/2.5/weather?q={}&mode=json&units=metric&lang=zh_cn&APPID=6a67ed641c0fda8b69715c43518b6996"
print(address.format(city))
print("欢迎使用全球天气APP")
print("1.查看当前城市天气，2.查看其它城市天气，3.保存当前城市")
menno=input("请输入菜单")
if menno=="1":
    print("1.查看当前城市天气")
if menno=="2":
    print("2.查看其它城市天气")
if menno=="3":
    print("3.保存当前城市")











