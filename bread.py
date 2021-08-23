
import threading
import time

bread = 0

class cook(threading.Thread):
    username = ""
    bread = 0

    def run(self) -> None:
        global bread
        num = 0
        while True:

            if self.bread < 500:
                self.bread += 1
                bread +=1
                num +=1
                print("厨师:",self.username,"做了面包")
                print("篮子里",self.bread,"个")
            elif bread == 500:
                time.sleep(2)
                break


class curtomer(threading.Thread):
    username = ""
    money = 3000
    count = 500

    def run(self) -> None:
        global count
        global money
        while True:
                if self.count >= 1:
                    self.count -=1
                    self.money -=3

                    print("顾客:",self.username,"已买")
                else:
                    if self.money ==0:
                        print("顾客：",self.username,"买了",self.count,"个")
                        break



cook1 = cook()
cook2 = cook()
cook3 = cook()
cook1.username = "张三"
cook2.username = "李四"
cook3.username = "王五"
shopping1 = curtomer()
shopping2 = curtomer()
shopping3 = curtomer()
shopping4 = curtomer()
shopping5 = curtomer()
shopping1.username = "A"
shopping2.username = "B"
shopping3.username = "C"
shopping4.username = "D"
shopping5.username = "E"
cook1.start()
cook2.start()
cook3.start()
shopping1.start()
shopping2.start()
shopping3.start()
shopping4.start()
shopping5.start()