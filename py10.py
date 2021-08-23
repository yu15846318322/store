class cup:
    __height = 0
    __volume = 0
    __color = ""
    __Material = ""
    __deposit = ""

    def height(self,height):
        self.__height = height
    def volume(self,volume):
        self.__volume = volume
    def color(self,color):
        self.__color = color
    def material(self,material):
        self.__Material = material
    def deposit(self,deposit):
        self.__deposit = deposit

    def describe(self):
        print("这个水杯高度是",self.__height,"cm,容积是",self.__volume,"ml,颜色是",self.__color,"色,材质是",self.__Material,"可用来装",self.__deposit)
        print("==========================================================================================")
c = cup()
c.height(30)
c.volume(3000)
c.color("red")
c.material("塑料")
c.deposit("牛奶，咖啡，可乐......")
c.describe()


class computer:
    __c_name = ""
    __Screen = 0
    __price = 0
    __cpu = ""
    __Memory = ""
    __Standby_time = 0

    def c_name(self,c_name):
        self.__c_name = c_name
    def screen(self,screen):
        self.__screen = screen

    def price(self,price):
        self.__price = price

    def cpu(self,cpu):
        self.__cpu = cpu
    def memory(self,memory):
        self.__memory = memory
    def standby_time(self,standby_time):
        self.__standby_time = standby_time
    def model(self):
        print("这台电脑尺寸是",self.__screen,"英寸,价格是",self.__price,"元,CPU型号是",self.__cpu,"内存大小是",self.__memory,"待机时长是",self.__standby_time,"秒")


    def type(self):
        print("我正在用",self.__c_name,"打字")
    def play(self,game):
        print("我正在",self.__c_name,"玩游戏",game)
    def watch(self,watching):
        print("我正在",self.__c_name,"看视频",watching)
        print("==================================================")



p = computer()
p.c_name("dell")
p.screen(14)
p.price(5000)
p.cpu("bnio9999")
p.memory(800)
p.standby_time(80)
p.model()
p.type()
p.play("英雄联盟")
p.watch("笔记")


class ac:
    __brand = ""
    __price = 0
    def setbrand(self,brand):
        self.__brand = brand
    def getbrand(self):
        print(self.__brand)

    def  setprice(self,price):
        self.__price = price
    def getprice(self):
        print(self.__price)

    def open(self):
        print("空调开机了！")
    def close(self,time):
        print("空调将在",time,"分钟后自动关闭")
        print("================================")
a = ac()
a.setbrand("联想")
a.getbrand()
a.setprice(3000)
a.getprice()
a.open()
a.close(1)


class student:
    __name = ""
    __age = ""
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age
    def showme(self):
        print("大家好,我叫",self.__name,",今年",self.__age,"岁了！")
    def compare(self,student):
        if self.__age > student.getage():
            print("我比同桌大",(self.__age - student.getage()),"岁")
        elif self.__age < student.getage():
            print("我同桌小",(student.getage()-self.__age),"岁")
        else:
            print("我俩一样大")


s = student()
s.setname("张三")
s.setage(21)

s1 = student()
s1.setname("李四")
s1.setage(30)

s.compare(s1)
s1.compare(s)
s.showme()
print('========================')

class person():
    __name = ""
    __sex = ""
    __age = ""
    __phonemoney = 0
    __phonebrand = ""
    __phonesize = 0
    __scrensize = 0
    __time = 0
    __scores = 0
    def setname(self,name):
        self.__name = name
    def getname(self):
        return self.__name
    def setsex(self,sex):
        self.__sex = sex
    def getsex(self):
        return self.__sex
    def setage(self,age):
        self.__age = age
    def getage(self):
        return self.__age
    def setphonemoney(self,phonemoney):
        self.__phonemoney = phonemoney
    def getphonemoney(self):
        return self.__phonemoney
    def setphonebrand(self,phonebrand):
        self.__phonebrand =phonebrand
    def getphonebrand(self):
        return self.__phonebrand
    def setphonesize(self,phonesize):
        self.__phonesize = phonesize
    def getphonesize(self):
        return self.__phonesize
    def setscrensize(self,scrensize):
        self.__scrensize = scrensize
    def getscrensize(self):
        return self.__scrensize
    def settime(self,time):
        self.__time = time
    def gettime(self,time):
        return self.__time
    def setscores(self,scores):
        self.__scores = scores
    def getscores(self):
        return self.__scores
    def sendmessage(self,sendmessage):
        print("短信内容是",sendmessage,"")
    def converdation(self,phonenumber,time):
        if phonenumber == 0:
            print("您所拨打的电话为空号")
        elif self.__phonemoney < 1:
            print("您的话费余额不足")
        else:
            print("拨通电话")
            if time > 0 and time <=10:
                self.__phonemoney -= time
                self.__scores+= time *15
                print("花费",self.__phonemoney,'积分',self.__scores)
            elif time > 10 and time <= 20:
                self.__phonemoney-=time *0.8
                self.__scores+= time *39
                print("花费",self.__phonemoney,"积分",self.__scores)
            else:
                self.__phonemoney-= time *0.65
                self.__scores+= time *48
                print("花费",self.__phonemoney,"积分",self.__scores)
    def show(self):
        print("我叫",self.getname(),"，今年",self.getage(),"岁，性别",self.getsex(),"我使用的手机是",self.getphonebrand())
p = person()
p.setname("王五")
p.setage(24)
p.setsex('man')
p.setphonebrand('oppofind4')
p.settime('7h')
p.setphonesize('5.5')
p.setphonemoney(50)
p.setscrensize(7000)
p.setscores(128)
p.sendmessage('ghghgh')
p.converdation('454545454',10)
p.show()
print("==============================")



















