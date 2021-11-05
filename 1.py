def su(n):
    b=0
    if n<0:
        n=-n
        b=1
    a=0
    for i in range (1,n+1):
        if i%2==1:
            a=a+i
    if b==1:
        return -a+1
    return a

def av(n):
    if n==1:
        return 0
    else:
        d=0
        if n<0:
            n=-n
            d=1
        b=0
        c=0
        for i in range (1,n+1):
            if i%2==0:
                c=c+1
                b=b+i
        if d==1:
            b=-(b/(c+1))
        else:
            b=b/c
        return b

n=int(input("Write a number: "))
print("Sum of odd numbers 1 up to {} :".format(n),su(n))
print("Average of even numbers 1 up to {} :".format(n),av(n))