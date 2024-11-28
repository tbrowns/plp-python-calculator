# Calculator Program

print(15*"*", "Calculator", 15*"*")

num1 = int(input("Enter a the first number:"))
num2 = int(input("Enter a the second number:"))
op = input("Enter a mathematical operation(+, /, *, -):")

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="/":
    print(num1//num2)
elif op=="*":
    print(num1*num2)