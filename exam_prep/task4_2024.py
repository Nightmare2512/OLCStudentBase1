def div_2(number): 
    halved = int(number/2) 
    return halved 

#task 4.1 

def div_2(number): 
    halved = int(number/2) 
    return halved 

def odd_or_even(number):
    divided = int(number) % 2 #???? -
    if divided == 1 :
        return "Odd"
    else:
        return "Even"

# print(odd_or_even(4)) #testing
# print(odd_or_even(5)) #testing


#task 4.2

def div_2(number): 
    halved = int(number/2) 
    return halved 

def odd_or_even(number):
    divided = int(number) % 2
    if divided == 1 :
        return "Odd"
    else:
        return "Even"

def prime(number):
    if number < 2 :
        return "Not Prime"
    if number == 2 :
        return "Prime"
    if number > 2 :
        if odd_or_even(number) == "Even":
            return "Not Prime"
    
    for i in range (3, div_2(number) + 1):
        if number % i == 0:
            return "Not Prime"
        
    return "Prime"
            
# print(prime(2))#testing
# print(prime(11))#testing
# print(prime(27))#testing
# print(prime(55))#testing

#task 4.3



def div_2(number): 
    halved = int(number/2) 
    return halved 

def odd_or_even(number):
    divided = int(number) % 2 
    if divided == 1 :
        return "Odd"
    else:
        return "Even"

def div_2(number): 
    halved = int(number/2) 
    return halved 

def odd_or_even(number):
    divided = int(number) % 2
    if divided == 1 :
        return "Odd"
    else:
        return "Even"

def prime(number):
    if number < 2 :
        return "Not Prime"
    if number == 2 :
        return "Prime"
    if number > 2 :
        if odd_or_even(number) == "Even":
            return "Not Prime"
    
    for i in range (3, div_2(number) + 1):
        if i % 2:
            return "Not Prime"
        
    return "Prime"



number = input("input a Whole number only")

if number.isdigit:
    prime(number)
