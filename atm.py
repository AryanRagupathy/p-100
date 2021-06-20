class atm(object):

    def __init__(self,cardNumber,pinNumber,name,currency,balance):
        self.cardNumber=cardNumber
        self.pinNumber=pinNumber
        self.name=name
        self.currency=currency
        self.balance=balance

    def cashWithdrawal(self):
        cash = int(input("Enter the amount that you want to withdraw (in " + self.currency + "): "))
        print(self.name + ", " + self.currency, cash, " withdrawn!")
        self.balance = self.balance - cash
        print("")
    

    def balanceEnquiry(self):
        print("You have " + self.currency, self.balance, "in the bank.")
        print("")

    def getInfo(self):
        print("Name: " + self.name)
        print("ATM Card Number:", self.cardNumber)
        print("PIN Number:", self.pinNumber)
        print("Currency in your country: " + self.currency)
        print("Your Balance:", self.balance)
        print("")


user1 = atm(123456789, 88888, "Aryan", "Rs.", 10000)
user1.getInfo()
user1.cashWithdrawal()
user1.balanceEnquiry()

user2 = atm(987654321, 33333, "Ashwin", "$", 14000)
user2.getInfo()
user2.cashWithdrawal()
user2.balanceEnquiry()