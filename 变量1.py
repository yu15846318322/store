'''
    低级版本：
        while
        1、用户输入一个值
        2、判断值是多少
        if >随机数:猜对了
        else:猜错了
'''
import random
# 1.让系统产生一个随机数

data = random.randint(0,200) # 22
# 2.循环的让用户去猜

i = 1
while i <= 20:
    num = input("请输入你要猜的数字：") # "22" "23"
    num = int(num) # "22"  --> 22
    if num > data:
        print("大了！")
    elif num < data:
        print("小了！")
    else:
        print("恭喜，猜对了！本次猜对数字为：",data)
        break #终止循环





