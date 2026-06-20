#my simple calculator 
while True:

  symbol = input("Enter an arithmetic operator: +,-,*,/ ")
  a = int(input("Enter first number:"))
  b = int(input ("Enter second number:"))
  if symbol == "+" :
    z = a + b
    print(F"you answer is {z}")
  elif symbol == "-":
    z = a - b
    print(F"your answer is {z}")
  elif symbol == "*" :
    z = a * b
    print(F"your answer is {z}")
  elif symbol == "/" :
    z = a / b
    print(F"your answer is {z}")
  else: 
    print(F"invalid operator")
  again = input("do yo want to keep running this program? (yes/no)")
    
  if again == "no" :
    
     break
print("Thank you")