# Strings

# String is data type that stores a sequence of characters.

name = "Junaid"
print(name)


# Strings Method

str = "my name is Junaid"

print(len(str))
print(str.endswith("id"))
print(str.capitalize())
print(str.replace("Junaid", "Usama"))
print(str.find("name"))
print(str.count("m"))


# Qs. Write a program to input user first name & print its length.

name = input("Enter your first name: ")
print(len(name))


# Qs. Write a program to find the occurrence of '$' in a String.

str = "Hello, $I am a $ Symbol"
print(str.count("$"))



# Conditional Statements

age = 24

if(age>=18):
    print("You can Vote")
else:
    print("You Can't Vote")


# Qs. Grade Student Based on marks

marks = int(input("Enter your marks: "))

if(marks>=90):
    print("A")
elif(marks>=80 and marks<90):
    print("B")
elif(marks>=70 and marks<80):
    print("C")
else:
    print("D") 


# Qs. WAP to check if a number entered by the user is odd or even.

num = int(input("Enter Your number: "))

if(num%2==0):
    print(f"{num} is Even Number")
else:
    print(f"{num} is Odd Number")


# Qs. WAP to find the greatest of 3 numbers entered by the user.

num_one = int(input("Enter your first number: "))
num_two = int(input("Enter your second number: "))
num_three = int(input("Enter your third number: "))

if(num_one>num_two and num_one>num_three):
    print(f"{num_one} is greatest number")
elif(num_two>num_one and num_two>num_three):
    print(f"{num_two} is greatest number")
else:
    print(f"{num_three} is greatest number")


# Qs. WAP to check if a number is a multiple of 7 or not.

number = int(input("Enter your number: "))

if(number%7 == 0):
    print(f"{number} is a multiple of 7")
else:
    print(f"{number} is not a multiple of 7")
