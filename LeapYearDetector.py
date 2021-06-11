# Leap Year Detector

print("\t\t\t LEAP YEAR DETECTOR");

y = int(input("Enter a year: "));

l1 = y % 4
l2 = y % 100
l3 = y % 400

if l1 == 0:
    if l2 == 0:
        if l3 == 0:
            print(y, "is a leap year.");
        else:
            print(y, "is not a leap year.");
    else: print(y, "is a leap year.");
else: 
    print(y, "is not a leap year.");