import time
import random
data = random.randint(0,1000)
count = 0
i= 1
icon = 5000
while True:
    count = count + 1
    num = input ("请输入您要猜的数字：")
    num = int(num)
    if i<5:
        if num > data:
            icon = icon - 500
            print("大了"",剩余人民币：", icon)
        elif num < data:
            icon = icon - 500
            print("小了"",剩余人民币：", icon)
        else:
            icon = icon + 500
            print("恭喜，猜中了！本次幸运数字为：", data, ",本次猜了", count, "次！"",剩余人民币：", icon)
            a = input("请问是否继续游戏")
            if a == "y":
                data = random.randint(0, 1000)
            elif a == "n":
                break
    else:
        time.sleep(5)
        break
    i = i + 1