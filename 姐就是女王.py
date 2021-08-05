'''

'''

import random

character = ["1.普通","2.稀有英雄","3.传奇英雄"]
print("--------姐就是女王----------")
i = 0
while i<3:
    i +=1
    choose =int(input("请选择角色："))
    a = random.randint(1,200)
    b = random.randint(1,200)
    c = random.randint(1,200)
    rnum = [a,b,c]
    if choose ==1:
        print("普通英雄")
        init = 10
        d = random.choice(rnum)
        e = random.randint(0,1)
        if e == 0:
            init +=d
            if init > 100:
               print("任务成功!")
            elif init <= 0:
               print("任务失败！")
        elif e == 1:
            print("稀有英雄")
            init -=d
            if init > 100:
                print("任务成功！")
            elif init <= 0:
                print("任务失败！")
        elif choose ==2:
            print("传奇英雄")
            init1 = 30
            f = random.choice(rnum)
            g = random.randint(0,1)
            if g == 0:
                init1 += f
                if init1 > 100:
                    print("任务成功！")
                elif init <= 0:
                    print("任务失败！")
    elif choose == 2:
        print("传奇英雄")
        init1 = 30
        f = random.choice(rnum)
        g = random.randint(0,1)
        if g == 0:
            init += f
            if init1 > 100:
                print("任务成功！")
            elif init1 <= 0:
                print("任务失败！")
        elif g == 1:
            init1 -= f
            if init1 > 100:
                print("任务成功！")
            elif init1 <= 0:
                print("任务失败！")
    elif choose ==3:
        init2 = 10
        h = random.choice(rnum)
        init2 += h
        if init2 > 100:
            print("任务成功！")
        else:
            print("任务失败！")
print("-----------------------------")



