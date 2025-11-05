def calculator(a,b,c):
    if c=="+":
        return a+b
    elif c=="-":
        return a-b
    elif c=="*":
        return a*b
    elif c=="/":
        return a/b
    elif c=="**":
        return a**b
    elif c=="//":
        return a//b
    else:
        return "Unsupported operator"
print(calculator(2,4,"-"))

class bankAccount:
    def __init__(self, accountNumber, accountHolder):
        self.__accountNumber = accountNumber
        self.__accountHolder = accountHolder
        self.__balance = 0
    def deposited(self, deposit):
        self.__balance += deposit
        print(f"Deposited: ${self.__balance}")
    def withdrawl(self, withdraw):
        self.__balance -= withdraw
        print(f"Withdrawn: ${self.__balance}")
    def getAccountInfo(self):
        print(f"Account Number: {self.__accountNumber}")
        print(f"Account Holder: {self.__accountHolder}")
        print(f"Balance: {self.__balance}")
bankObj = bankAccount(12212, "pran")
bankObj.deposited(1000)
bankObj.withdrawl(500)
bankObj.getAccountInfo()