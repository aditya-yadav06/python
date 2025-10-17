#gcd of two numbers..
#logic find greater of the two numbers and use modulus till last non zero remainder:
#firstly for positive numbers only:
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
#first find the greater number:
if a<0 or b<0:
    print("Input must be positive for now.")
else:
    if a>b:
        greater_num=a
        smaller_num=b
    else:
        greater_num=b
        smaller_num=a
    while smaller_num>0:
        d=greater_num%smaller_num
        greater_num=smaller_num
        smaller_num=d
                                                     #This is code logic
        '''if d!=0:
            smaller_num=d
        else:
            break'''
    print("GCD of(",a,",",b,")=",greater_num)
"""other logic could be that we shift greater number to smaller number and then check for
smaller number not equal to zero(condition for while loop) and then print."""
