num1=0
num2=0
sum1=input("enter a number:")
sum2=input("enter second number:")
reult=input("enter the operator: *,/,+,-")
if reult=="+":
    num1=int(sum1)
    num2=int(sum2)
    print(num1+num2)
if reult=="-":
    num1=int(sum1)
    num2=int(sum2)
    print(num1-num2)
if reult=="*":
    num1=int(sum1)
    num2=int(sum2)
    print(num1*num2)

try:
    if reult=="/":
      num1=int(sum1)
      num2=int(sum2)
      division=num1/num2
      print(division)
except  ZeroDivisionError :
     print("cant divide by zero")
except ValueError:
    print("invalid input")

