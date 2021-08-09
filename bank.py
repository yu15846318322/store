
import random

bank_name= "中国工商银行起码路支行"#写死的银行地址
print("--------------------------------")
print("|------工商银行账户管理系统------|")
print("|------------------------------|")
print("|*1、开户     ------------------|")
print("|*2、存钱     ------------------|")
print("|*3、取款     ------------------|")
print("|*4、转账     ------------------|")
print("|*5、查询     ------------------|")
print("|*6、退出     ------------------|")
print("--------------------------------")

bank={}
def bank_adduser(account,username,password,country,province,street,door,money):
    if len(bank) >= 100:
        return 3

    bank[account] = {
        "username":username,
        "password": password,
        "country": country,
        "province": province,
        "street": street,
        "door": door,
        "money": money,
        "bank_name": bank_name
    }
    return 1

def adduser():
    username=input("请输入你的开户名：")
    password=input("请输入你的密码：")
    country=input("请输入你的国籍：")
    province=input("请输入你的省份：")
    street=input("请输入你的街道：")
    door=input("请输入你的门牌号：")
    money=input("请输入你要存款金额：")
    account=random.randint(10000000,99999999)

    status=bank_adduser(account,username,password,country,province,street,door,money)

    if status ==3:
        print("对不起，该银行的用户已满，请到其他银行办理")
    elif status ==1:
        print("开户成功！以下是你的个人开户信息：")
        info='''
        =====个人信息======
        用户名:%s
        用户密码:%s
        账号:%s
        地址信息
            国家:%s
            省份:%s
            街道:%s
            门牌号:%s
        当前账户余额:%s
        开户行名称:%s
        ==================
        '''
        print(info%(username,password,account,country,province,street,door,money,bank_name))

    elif status == 2:
        print("对不起，该用户已存在！请稍后重试！！！")



def bank_drawcash(account,password,cash):
    user = bank.get(account)
    if not user:
        return 1
    if password != bank[account]["password"]:
        return 2

    return 0

def drawcash():
    account = input("请输入你的账号：")
    password = input("请输入你的账户密码：")
    cash = input("请输入你存款金额：")
    status = bank_drawcash(account, password, cash)
    if status == 1:
        print("对不起，您的账号不存在，请重新输入！")
    elif status == 2:
        print("对不起，您的密码不对，请重新输入！")

    elif status == 0:
        bank[account]["money"] = bank[account]["money"] + cash
        acc_balance = bank[account]["money"]
        print("存款成功，请拿好您的小票！")
        info ='''
        =======存款信息=======
        账号：%s
        存款金额：%s
        账户余额：%s
        =====================
        '''
        print(info % (account,cash,acc_balance))








while True:
    num=input("请输入您要办的业务：")
    if num  == "1":
        adduser()
        print(bank)
    elif num == "2":
        drawcash()
    elif num == "3":
        print("取钱")
    elif num == "4":
        print("转账")
    elif num == "5":
        print("查询")
    elif num == "6":
        print("再见")
        break
    else:
        print("别瞎搞")
        break