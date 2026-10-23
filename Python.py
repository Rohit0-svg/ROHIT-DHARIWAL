#electricity bill calculator
import random

metre_units = random.randint(0,700)
print(f"Your metre units is :{metre_units}")
unit = int(input("Enter you eletricity units (shown on metre) :"))
bill = 0
if (unit == metre_units):
    if (unit < 0):
        print("jee incoming to u")
    elif (unit <= 100):
        bill = unit * 3
    elif (unit <= 200):
        bill = (100 * 3) + ((unit-100) * 5)
    elif (unit <= 500):
        bill = (100 * 3) + (100 * 5) + ((unit - 200) * 7)
    elif(unit > 500):
        bill = (100 * 3) + (100 * 5) + (300 * 7) + ((unit - 500) * 10)
    bill += 50
    print(f"your bill is of amount Rs :{bill} (inc all tax and service charge)")
else:
    print("----------------Are you trying to save bucks--------------------")



#reult analysis
marks = list(map(int, input("enter your marks(0-100): ").split()))
fail = 0
for i in range(len(marks)):
    if(marks[i] < 40):
        fail += 1
result = ''
if (fail == 0):
    result = 'Pass'
elif(fail > 2):
    result = 'Fail'
else:
    result = 'Reappear'

total = sum(marks)/5
division = ''
if (total < 40):
    division = 'No Division'
elif (total > 40 and total < 50):
    division = 'Third'
if (total > 50  and total < 60):
    division = 'Second'
if (total > 60):
    division = 'First'

print(f"RESULT :{result} | PERCENTAGE :{total} | DIVISION :{division}")
