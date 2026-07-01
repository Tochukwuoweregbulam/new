from abc import ABC, abstractmethod

class Users(ABC):

   @abstractmethod
   def login (self):
      pass
   @abstractmethod
   def logout(self):
      pass

class Students(Users):
    def login (self):
        print("Welcome Students")

    def logout(self):
        print("Goodbye Students")

class Teachers(Users):
    def login(self):
        print("Welcome Teachers")
    def logout(self):
        print("Goodbye Teachers")


teachers = Teachers()
teachers.login()