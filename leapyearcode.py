#leap year code...
#logic is that if its divisible by 4 and not by 100 except if its divisible by 400
#this code is long in second loop check for divisibility by 400 because 100 and 4 are icluded
year=int(input("Enter year:"))
if (year%4==0 and year%100!=0) or (year%400==0):
    print(year,"is a leap year.")
else:
    print(year,"is not a leap year.")
