""" 
Bank System Features:
Parent Class:User
    i). Holds deatils about an user
    ii). Has a function to show user details
Child Class: Bank
    i). Stores details about the account balance
    ii). Stores deatils about the amount
    iii). Allows for deposits, withdraw,view_balance
"""
#Parent Class
class User:
    def __init__(self,name,age,gender):
        self.name=name
        self.age = age
        self.gender=gender
    
    def user_details(self):
        user = {'name':self.name,'age':self.age,'gender':self.gender}
        return f"User details {user}"


class Bank(User):
    def __init__(self,name,age,gender):
        #used to avoid writing self.name, self.age and self.gender again as we did in the parent class
        super().__init__(name,age,gender)
        self.balance = 0
    
    def deposits(self,amount):
        self.balance = self.balance + float(amount)
        print(f"Your current account balance is {self.balance}")
    
    def withdraw(self,amount):
        self.amount = float(amount)
        if(self.amount > self.balance):
            print(f'Insuffient Funds.Your current balance is {self.balance}')
        else:
            self.balance = self.balance - self.amount
            print(f'You have withdrawn {self.amount}. Current Balance is {self.balance}')
    
    def view_balance(self):
        user_details = self.user_details()
        print(f'{user_details}: Current Balance is {self.balance}')

user = Bank('fridah',27,'female')
user.deposits(800)
user.withdraw(100)
user.view_balance()