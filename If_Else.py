# if...else conditional

age = int(input("Enter your age: "));

if age >= 18:
    print("You are eligible to vote.");
else: 
    print("You are ineligible to vote.");

# another example

class_1 = input("Enter your class: ");
section = input("Enter your section: ");

if class_1 == "10" and section == "D":
    print("Excellent!");
else:
    print("Sorry!");

# Positive,negative,odd,even
    
a = int(input("Enter a number "));

if a > 0: 
    print("Your number", a, "is positive");
elif a < 0: 
    print("Your number", a, "is negative");
elif a == 0: 
    print("Your number", a, "is neither positive nor negative, it is zero");

b = a % 2 
    
if b == 0: 
    print("Your number", a, "is even");
elif b == 1: 
    print("Your number", a, "is odd");
    
# Special Characters

Ch = input("Enter a character ");

if Ch >= "A" and Ch <= "Z":
    print(Ch, "is an uppercase character.")
elif Ch >= "a" and Ch <= "z":
    print(Ch, "is an lowercase character.")
elif Ch >= "0" or Ch <= "9":
    print(Ch, "is a digit.")
else:
    print(Ch, "is a special character.")
    
# Vowels 

l = input("Enter a letter ");
l1 = l.upper();

if l1 == 'A' or l1 == 'E' or l1 == 'I' or l1 == 'O' or l1 == 'U':
    print(l, "is a vowel.");    
else:    
    print(l, "is a consonant.");
    
# National Elections

age = int(input("Enter your age: "));
nat = input("Enter your nationality: ");
nat1 = nat.upper()
       
if age >= 18 and nat1 == "INDIAN":
    print("You are eligible to vote in Indian elections.");
elif age < 18 and nat1 == "INDIAN":
    print("You will be eligible to vote in Indian elections in some years.");
elif age >= 18 and not(nat1 == "INDIAN"):
    print("You are eligible to vote, but not in Indian elections.");
elif age < 18 and not(nat1 == "INDIAN"):
    print("You will be eligible to vote in some years, but not in Indian elections.");    
else: 
    print("Error Invalid Data");