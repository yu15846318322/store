
data = {"昌平线":{"十三陵":["十三陵水库","沙河水库"]
                    ,
            "沙河":["海底捞","呷哺呷哺"]
        },
        "13号线":{
            "流星花园":["0001","0002"],
            "育荣教育园区":["0003","0004"],

        }
        }

def print_place(choice):
    for i in choice:
        print(i)


for i in data:
    print(i)


while True:
    city1 = input("请输入地铁：")
    if city1 in data:
        print_place(data[city1])
        city2 = input("请输入小区：")
        if city2 in data[city1]:
            print_place(data[city1][city2])
            city3 = input("请输入门牌号：")
            if city3 in data[city1][city2]:
                print(city3)




        break
    else:
        print("当前不存在！")




#乘法口诀
for i in range(1,10):
  for j in range(1,i+1):
     print(j,'*',i,'=',j*i,end=' ')
  print()

n = int(input('请输入一个数字：'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,'*',i,'=',j*i,end=' ')
    print()