'''
1. Class : thinking about class it is like a blueprint for creating object
2. Object : thinking about object it is like a real world entity or thing or instance of a class

What are the pillar of oops : 
1. Abstraction: 
   - Hiding complex implementation details and showing only the essential information to the user.
   - To implement abstraction, you use `abstract class` and `ABC (Abstract Base Class)` module in Python.
   - Example: Using an ATM — you don't need to know how money is dispensed inside; you just interact with a simple interface.
'''
from abc import ABC,abstractmethod
class BankAccount(ABC):
    def __init__(self,holder,balance):
        self.holder = holder
        self.balance = balance

    @abstractmethod
    def withdraw(self,amount):
        pass

    @abstractmethod
    def deposite(self,amount):
        pass

    @abstractmethod
    def check_balance(self):
        pass

class CurrentAccount(BankAccount):
    def __init__(self, holder, balance):
        super().__init__(holder,balance)
    
    def withdraw(self, amount):
        self.balance -= amount
        print(f"${amount} is withdraw from you account and current balance is : ${self.balance}")
    
    def deposite(self, amount):
        self.balance += amount
        print(f"${amount} ammount is created to your account and current balance is : ${self.balance}")

    def check_balance(self):
        print(f"thank you for checking balance your current balance is ${self.balance}")
        
current = CurrentAccount("James Smith",100000)
current.deposite(100)
current.withdraw(300)
current.check_balance()


'''
2. Polymorphism : 
- Ploymorphism means one entity having different forms 
- In programming having one function or method and it is behave different depends on the object that is called.
- Same method name, but different behavior based on the object.

-- a human can run but a dog can run here run is same method but having different behavior

Types :
a. Runtime Polymorphism : child class changes the behavior of parent class method.Method Overloading , Decided at compile time (before running the program).
b. Compiledtime Polymorphism : Two function with same name but different arguments. Method Overriding , Decided at runtime (while running the program).
'''
class BankAccount:
    def __init__(self,holder,balance):
        self.holder = holder
        self.balance = balance
    
    def calculate_interest(self):
        print("calculating generic interest rate.")

class SavingAccount(BankAccount):
    def __init__(self,holder,balance):
        super().__init__(holder,balance)
    
    def calculate_interest(self):
        print(f"calculate interest rate on the saving account : {self.balance * 0.8}")

class CurrentAccount(BankAccount):
    def __init__(self, holder, balance):
        super().__init__(holder, balance)
    
    def calculate_interest(self):
        print(f"calculate interest rate on the current account : {self.balance * 0.3}")

saving = SavingAccount("John Kali",5000)
saving.calculate_interest()

current = CurrentAccount("Pratik Jain",6000)
current.calculate_interest()
        

'''
3. Inheritance : Creating new class based on the existing classes  or you are inheriting the child class into the parent class.
- Types Single , Multiple , Multilevel Inheritance.
- It motivates code reusability.
- Inheritance allows a new class to inherit the properties and behaviors of an existing class, promoting code reusability.


4. Encapsulation :
Binding data or method into the single logic unit class class and preventing direct access to the data
'''
class BankAccount:
    def __init__(self,holder,balance,age):
        self.holder = holder
        self.__balance = balance # private
        self._age = age  # protected

    def get_balance(self):
        return self.__balance
    
class SavingAccount(BankAccount):
    def __init__(self, holder, balance, age):
        super().__init__(holder, balance, age)
    
    def calculate_interest(self):
        print(f"calculate interest rate on the saving account : {self.get_balance() * 0.8}")
    
saving = SavingAccount("James smith",80000,45)
saving.calculate_interest()



