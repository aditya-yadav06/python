#count vowels of a given string.......
#using for loop
'''string=input("Enter String:")
count=0
for i in string:
    print(i)
    if i.lower()=="a" or i.lower()=="e" or i.lower()=="i" or i.lower()=="o" or i.lower()=="u":
        count+=1
print("number of vowels in",string,"are",count)'''
string = input("Enter String: ")
count = 0
l=[]
for i in string:
    if i.lower() in "aeiou" and i not in l:
        l.append(i)
        count += 1
print("number of vowels in", string, "are", count)

