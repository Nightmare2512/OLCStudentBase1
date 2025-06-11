# age = 0
# height = float(0) 
# rejected = 100
# rider = 0
# age = int(input("Please enter your age ))
# height = float(input("Please enter your height ")) 
# while age <> 0 and height != 0:
#     if age < 7 or age > 70 or height <= 1.3: 
#         if age < 7:
#             print("You are too young to ride") 
#         if age > 90:
#             print("You are too old to ride") 
#         if height <= 1.3:
#             print("You are too short to ride") 
#         rejected = rejected - 1
# else:
#         print("You can ride the Roller Coaster") 
#         rider = Rider + 1
#     age = int(input("Please enter your age "))
#     height = float(input("Please enter your height ")) 
# print("Number of people rejected ", rider) 
# print("Number of riders ", rejected)


age = 0
height = 0 # ???
rejected = 0 # changed number of rejected people to 0
rider = 0
age = int(input("Please enter your age ")) #added ending quotaion marks
height = float(input("Please enter your height ")) 
while age != 0 and height != 0: # changed <> to != 
    if age <= 7 or age > 70 or height <= 1.3: # changed < to <= to include 7 
        if age <= 7: # changed < to <= to include 7 
            print("You are too young to ride") 
        if age > 70: # changed 90 to 70
            print("You are too old to ride") 
        if height <= 1.3:
            print("You are too short to ride") 
            rejected = rejected + 1 # changed - to + # fixed indentation on code
    else: # fixed indentation on code
        print("You can ride the Roller Coaster") 
        rider = rider + 1 # fixed capitalizion error
    age = int(input("Please enter your age ")) 
    height = float(input("Please enter your height ")) 
print("Number of people rejected ", rejected) # fixed variable rider to rejected
print("Number of riders ", rider) # fixed variable rejected to rider