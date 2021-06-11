## Comp. Science Assignment 2 Grade X

#Q1

a = int(input("Enter a number: "));
b = int(input("Enter another number: "));

if a > b:
    print(a, "is the larger number.");
elif a < b:
    print(b, "is the larger number.");
else:
    print("Both are equal.");
    
#Q2    

a = int(input("Enter a number: "));

if a > 0: 
    print("Your number", a, "is positive");
elif a < 0: 
    print("Your number", a, "is negative");
elif a == 0: 
    print("Your number", a, "is neither positive nor negative, it is zero");

#Q3

a = int(input("Enter a number "));

b = a % 2 
    
if b == 0: 
    print("Your number", a, "is even");
elif b == 1: 
    print("Your number", a, "is odd");

#Q4

age = int(input("Enter your age: "));
nat = input("Enter your nationality: ");
nat1 = nat.upper()
       
if age >= 18 and nat1 == "INDIAN":
    print("You are eligible to vote.");   
else: 
    print("You are ineligible to vote.");     
    
#Q5

l = input("Enter a letter ");
l1 = l.upper();

if l1 == 'A' or l1 == 'E' or l1 == 'I' or l1 == 'O' or l1 == 'U':
    print(l, "is a vowel.");    
else:    
    print(l, "is a consonant.");
    
#Q6

a = int(input("Enter a number: "));
b = int(input("Enter another number: "));

c = b % a

if c == 0: 
    print(b, "is a multiple of", a);
else:
    print(b, "is not a multiple of", a);      
    
#Q7

a = int(input("Enter a number: "));
b = int(input("Enter another number: "));

c = b % a

if a == 0 or b == 0:
    print("0 is a multiple of all numbers");
elif c == 0: 
    print(b, "is a multiple of", a);
else:
    print(b, "is not a multiple of", a);

#Q8

print("Enter marks for each subject out of 40 marks.")
eng = int(input("Enter your marks in English: "));
iil = int(input("Enter your marks in IInd Language: "));
sst = int(input("Enter your marks in Social Science: "));
sci = int(input("Enter your marks in Science: "));
mth = int(input("Enter your marks in Mathematics: "));

if eng > 40 or iil > 40 or sst > 40 or sci > 40 or mth > 40:
    print("Error: Maximum marks are FORTY!")
else:     
    tot = eng + iil + sst + sci + mth
    per = (tot/(40*5))*100

    print("Your total marks are", tot);
    print("Your total percentage is", per);

    if per >= 90:
        print("Your grade is A!");
    elif per >= 80:
        print("Your grade is B!");
    elif per >= 70:
        print("Your grade is C!");
    elif per < 70:
        print("Your grade is D!");

#Q9

Basic_Salary = int(input("Enter your basic salary: "));

HRA = Basic_Salary * (45/100)  
DA = Basic_Salary * (55/100)
PF = Basic_Salary * (23/100)

if Basic_Salary >= 70000:
    IT = Basic_Salary * (45/100)  
elif Basic_Salary >= 50000:
    IT = Basic_Salary * (35/100)  
elif Basic_Salary >= 30000:
    IT = Basic_Salary * (25/100)  
else:
    IT = 0  

Salary_in_Hand = Basic_Salary + HRA + DA - PF - IT

print("Your basic salary is", Basic_Salary);
print("Your House Rent Allowance is", HRA);
print("Your Dearness Allowance is", DA);
print("Your Provident Fund is", PF);
print("Your Income Tax is", IT);
print("Your salary in hand is", Salary_in_Hand);

#Q10

print("\t\t\t\t\t\tTEMPERATURE CONVERTER");

temp = int(input("Enter temperature: "));

print(" 1 From C to F \n 2 from F to C ")

opt = int(input("Pick your option - 1 or 2: "));

opt1 = (temp * (9/5)) + 32
opt2 = (temp - 32) * (5/9)

if opt == 1:
    print(opt1,"F");
elif opt == 2:
    print(opt2,"C");

#Q11

Ch = input("Enter a character ");

if Ch >= "A" and Ch <= "Z":
    print(Ch, "is an uppercase character.");
elif Ch >= "a" and Ch <= "z":
    print(Ch, "is a lowercase character.");
elif Ch >= "0" and Ch <= "9":
    print(Ch, "is a digit.");
else:
    print(Ch, "is a special character.");
    
#Q12

print("\t\t\t\t\t\tELECTRICITY BILL");

unit = int(input("No. of units = "));

unit1 = 50 * 0.50
unit2 = 100 * 0.75
unit3 = 100 * 1.20
unit4 = (unit - 250) * 1.50

unit5 = unit1
unit6 = unit1 + unit2
unit7 = unit1 + unit2 + unit3
unit8 = unit1 + unit2 + unit3 + unit4

if unit <= 50:
    print("The electricity bill is ₹",unit5);
elif unit <= 150:
    print("The electricity bill is ₹",unit6);
elif unit <= 250:
    print("The electricity bill is ₹",unit7);    
elif unit > 250:
    print("The electricity bill is ₹",unit8);
