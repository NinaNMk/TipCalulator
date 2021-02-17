a= float (input("What was the total bill?"))
b=float(input("What per tip would you like to give? 10,12 or 15?"))
c=float(input("How many people to split the bill?"))


d=b/100 #for %

a1=a*d #for the 12% of 34 -> 4,08
a2=a+a1 #34+4,08

total=(a2/c)

print(f" Each person should pay:{round(total)}")
 