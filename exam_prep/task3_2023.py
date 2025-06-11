#task3.1


import random
questions = 10
answer_list = []
correct = 0
incorrect = 0
total_mark = 0
for x in range(questions): # fixed extra -1 causing only 9 questions instead of 10
    num1 = random.randint(1, 50)
    num2 = random.randint(1, 50)
    answer =  num1 + num2
    print("What is", num1, "+", num2, "?")
    user_answer = int(input()) # forced user_answer to bee int
    if user_answer == answer:
        answer_list = answer_list + ["Correct"] # fixed wrong quotion mark #moved code outside of if loop as if answer is right it is right not depeding on marks
        if num1 > 25 and num2 > 25: # changed or to and to fix only one >25 number needed for 2 marks error
            total_mark = total_mark + 2
        else:
            total_mark = total_mark + 1
    else:
        answer_list = answer_list + ["Incorrect"]
list_length = len(answer_list) #removed wrong - 1 sign
for i in range(list_length):
    if answer_list[i] == "Correct":  # fixed fwrong identifier X to i
        correct = correct + 1 # changed - to + to show the right number for correct
if correct  == 1: # changed message to correct to represent the correct value
    message = "answer."
else:
    message = "answers."
print("Your total mark is", total_mark, "and you had", correct, "correct", message)
