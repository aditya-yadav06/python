#programm to check palindrome number......
n=int(input("enter a number to check for palindrome:"))
p=n #value of n changes during reversal so p keeps the orignal value to compare later.
#code for reverse of a number....
i=0
while n>0:
    d=n%10        #extracting last digit.
    i=i*10+d      #code logic.
    n=n//10     #changing value of n to extract the next digits...
#reverse programm completed and value is stored in i.
#check for palindrome.
if p==i:
    print("This is a palindrome number.")
else:
    print("This is not a palindrome number.")
