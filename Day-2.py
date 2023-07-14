#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

a=input("Whats the total bill: ")
b=input("How many total people there: ")
c=input("Tip percentage: ")
d=round((float(a)/int(b)) * ((float(c)/100)+1), 2);
print(f"Total bill per person: {d}");
