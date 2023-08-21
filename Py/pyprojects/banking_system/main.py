class User():
    def __init__(self,name,age,gender):
        self.name= name
        self.age = age
        self.gender = gender

    def show_details(self):
        print(f"Informations\n\nName = {self.name} \nAge = {self.age} \nGender = {self.gender}")
    
vini = User("Vini Muchulski",19,"Male")

vini.show_details()

#child class

class Bank(User):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)
        self.balance = 0

    def deposit(self, valor):
        self.balance = self.balance + valor
        print("Balance has been updated: $ ", self.balance)

    def withdraw(self, valor):
        if self.balance - valor <0:
            print(f"Insufficient Funds! Balance = $ {self.balance}")

        else:
            self.balance =self.balance -valor
            print("Balance has been updated: $ ", self.balance)

    def view_balance(self):
        self.show_details()
        print("Balance: $ ", self.balance)






apeiron = Bank("Apeiron",19,"RocketMan")
apeiron.show_details()
apeiron.deposit(500)
apeiron.withdraw(1000)
apeiron.withdraw(100)
apeiron.view_balance()
        