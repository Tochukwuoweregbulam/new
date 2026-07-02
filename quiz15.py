from abc import ABC, abstractmethod

class Users(ABC):

   def __init__(self):
       self.name = input("Please enter your name: ")

   @abstractmethod
   def login (self):
      pass
   @abstractmethod
   def logout(self):
      pass
class Result:
    def Get_User(self):
     user = input("Welcome, Are a teacher or student?")
     if user == "student":
         return Students()

     elif user == "teacher":
         return Teachers()



class Students(Users):
    def login (self):
        print("Welcome", self.name)

    def logout(self):
        print("Goodbye", self.name)

class Teachers(Users):
    def login(self):
        print("Welcome ")
    def logout(self):
        print("Goodbye Teachers")

result = Result()
person = result.Get_User()
person.login()
person.logout()
