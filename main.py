num1=0
num2=0
num3=0
num4=0
sum1=input("enter a number:")
sum2=input("enter second number:")
sum3=input("enter third number:")
sum4=input("enter four number:")
reult=input("enter the operator: *,/,+,-")
if reult=="+":
    num1=int(sum1)
    num2=int(sum2)
    num3=int(sum3)
    num4=int(sum4)
    print(num1+num2+num3+num4)
if reult=="-":
    num1=int(sum1)
    num2=int(sum2)
    num3=int(sum3)
    num4=int(sum4)
    print(num1-num2-num3-num4)
if reult=="*":
    num1=int(sum1)
    num2=int(sum2)
    num3=int(sum3)
    num4=int(sum4) 
    print(num1*num2*num3*num4)

try:
    if reult=="/":
      num1=int(sum1)
      num2=int(sum2)
      num3=int(sum3)
      num4=int(sum4)   
      division=num1/num2
      print(division)
except  ZeroDivisionError :
     print("cant divide by zero")
except ValueError:
    print("invalid input")

