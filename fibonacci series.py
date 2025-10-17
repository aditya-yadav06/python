#fibonacci series code:::
#logic--take 2 initial numbers and then update them .
a=0
b=1
x=int(input("Enter how many terms u want to print:"))
count=0                                              #count helps us to reach n:
while count<x:
    print(a,end=" ")
    next_num=a+b
    a=b
    b=next_num
    count+=1
#code completed...
