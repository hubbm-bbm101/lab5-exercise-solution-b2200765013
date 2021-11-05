def su(n):
    a=0
    for i in range (1,n+1):
        if i%2==1:
            a=a+i
    return a

def av(n):
    b=0
    c=0
    for i in range (1,n+1):
        if i%2==0:
            c=c+1
            b=b+i
    b=b/c
    return b

n=int(input("Write a number: "))
print("Sum of odd numbers 1 up to {} :".format(n),su(n))
print("Average of even numbers 1 up to {} :".format(n),av(n))