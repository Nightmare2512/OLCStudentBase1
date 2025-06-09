
# In [1]:    # Task 2.1
#           Program Code
#           Output:
# All code should have appropriate comments and all identifiers should be appropriately named. [4]

# Task 5.1
# Write a shift() function that has the parameter char passed to it. 
# The function must shift a lower-case letter down the alphabet sequence 
# by one position (a → b ... → y → z → a) and do nothing to other characters.   

def shift(char):
    alpha = 'abcdefghijklmnopqrstuvwxyz'

    oidx = alpha.find(char)

    newindex = (oidx + 1) %26

    return alpha[newindex]











                                                                                                                                    #   [4]

# Task 5.2
# Write a function encrypt() that has the parameters message and positions 
# passed to it. The function must use the shift() function to encrypt the
#  message argument by shifting all the lower-case letters in the message 
# down the alphabet sequence by the number of positions given in the positions argument. 
# The function should ignore all other characters.                     [7]

 
# Task 5.3
# Write a function shift_up() that has the parameter char passed to it. 
# The function must shift a lower-case letter up the alphabet sequence by 
# one position (a ← b ... ← y ← z ← a) and do nothing to other characters.                                                                                                                                         [2]

# Task 5.4
# Write a function decrypt() that has the parameters ciphertext and 
# positions passed to it. The function must use the shift_up() function 
# to decrypt the ciphertext argument by shifting all the letters up the 
# alphabet sequence by the number of positions given in the positions argument. 
# The function should ignore all other characters.                                                     [1]

# Task 5.5
# Create a simple text-based user interface to:
# • request the user to enter ‘E’ to encrypt a message or ‘D’ to
#  decrypt a ciphertext (case insensitive) and to re-enter 
# if the input is not ‘E’, ‘D’, ‘e’ or ‘d’

# • request the user to enter the message or the ciphertext
# • request the user to enter the number of positions to shift the 
# letters and the user to re-enter the number if the input is not a positive integer

# • output the encrypted message and write the encrypted message to the file 
# encrypted.txt, if the user requested to encrypt a message

# • output the decrypted ciphertext if the user requested to decrypt a message.

# Your program should use the encrypt() and decrypt() functions. 
# Test your program with the following input:

#                         a, E, This is the seCret me55age!, -1, 12   

#  Save your JupyterLab notebook for Task 5 [7]