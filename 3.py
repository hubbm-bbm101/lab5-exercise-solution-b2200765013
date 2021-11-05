import random
n=random.randint(0,100)
a=int(input("Enter a number: "))
while n!=a:
    if n<a:
        a=int(input("Decrease your number :"))
    else:
        a=int(input("Increase your number :"))
print("Right guess!")