print("Welcome to the tip calculator")
bill=float(input("What was the total bill:"))
tips=float(input("how much tip would you like to give? 10,12,15? "))
person=int(input("how many people split the bill: "))
percentage=(tips/100)*bill+bill
each_person=(percentage/person) 
print("each person should pay: ",each_person)