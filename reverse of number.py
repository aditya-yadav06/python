#programm to reverse a number...
#Logic-1
'''n=int(input("enter the number than that u want to reverse:"))
p=n
i=0
count=0
#programme to count number of digits in code..
while n>0:
    n=n//10
    count+=1
while p>0:
    d=p%10
    i+=d*(10**(count-1))
    count-=1
    p=p//10
print("Reverse number is:",i)'''
#print("hi")
#------------------------------------------------------------------------------------------
#logic-2
n=int(input("enter the number than that u want to reverse:"))
i=0
while n>0:
    d=n%10
    i=i*10+d
    n=n//10
print("reverse number is:",i)
