'''
Task 4 - 2023 Paper - Development of Program
Open the file SPLIT_SENTENCE.py. You will see the following function that 
takes a string of words, passed as the parameter word_string, splits it 
into individual words and stores these words in a list. 
It returns the list of words. 

You can assume the string does not contain punctuation marks.
'''



def split_sentence(word_string):
    list_sentence = word_string.split(" ")
    return list_sentence
#task 4.1

# function (word_string= input("write a sentence"))

# to print out
print(split_sentence("This is a sentence to split"))

# or to store into another variable
x = split_sentence("This is a sentence to split")


def check_list(word_check, sentence):
    if word_check in split_sentence(sentence):
        return "Yes"
    else:
        return "No"


# print(check_list(input("what word do you what to check"))) #testing