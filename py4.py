'''
姐就是女王:
随机选择人物： 1、普通没有技能
2、稀有英雄初始值为30。3、传奇英雄不会减少只会增加
需求：
初始值为：10
随机生成三个数字
随机选择一个数字
选择的数字和初始值进行计算（随机加减）
计算过后大于100则任务成功
计算过后小于或等于0则任务失败
'''

import random
list1 = ["普通","稀有","传奇"]

name = list1[random.randint(0,len(list1)-1)]
print(name)
num = 50
if name =="普通":
    while True :
        i = 0
        list2 = []
        while i < 3:
            i = i +1
            a = random.randint(5,20)
            list2.append(a)
        print(list2)
        num1 = list2[random.randint(0,len(list2)-1)]
        print(num1)
        list3 = [1,2]
        name2 = list3[random.randint(0,len(list3)-1)]
        if name2 ==1:
            num = num1 -num
            print(num)
        if num > 100:
            print("任务成功，你的分数是",num)
            break
        elif num <= 0:
            print("任务失败，你的分数是",num)
            break
num = 30
if name =="稀有":
    while True:
        i = 0
        list2 = []
        while i < 3:
            i = i + 1
            a = random.randint(5, 20)
            list2.append(a)
        print(list2)
        num1 = list2[random.randint(0, len(list2) - 1)]
        print(num1)
        list3 = [1, 2]
        name2 = list3[random.randint(0, len(list3) - 1)]
        if name2 == 1:
            num = num1 - num
            print(num)
        if num > 100:
            print("任务成功，你的分数是", num)
            break
        elif num <= 0:
            print("任务失败，你的分数是", num)
            break
num = 50
if name == "传奇":
    while True:
        i = 0
        list2 = []
        while i < 3:
            i = i + 1
            a = random.randint(5, 20)
            list2.append(a)
        print(list2)
        num1 = list2[random.randint(0, len(list2) - 1)]
        print(num1)
        list3 = [1, 2]
        name2 = list3[random.randint(0, len(list3) - 1)]
        if name2 == 1:
            num = num1 - num
            print(num)
        if num > 100:
            print("任务成功，你的分数是", num)
            break
        elif num <= 0:
            print("任务失败，你的分数是", num)
            break

