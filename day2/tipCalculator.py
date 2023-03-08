# # String positions
# print("Hello"[0])
# print("Hello"[-1])

# # Casting - Coverting a data type into another data type
# print(int("123") + int("456"))

# # Float
# num = 3.1416

# # Casting to int will truncate the decimal points
# print(int(num))

# # Casting int to sting to use the len function
# print(len(str(num)))

# # Data types

# num_char = len(input("What is your name? "))

# print(type(num_char))
# print("Your name has " + str(num_char) + " characters.")

# # Operators
# sum = 3 + 5
# res = 7 - 4
# mul = 3 * 2
# div = 6 / 3
# expo = 2 ** 2

# hei = 1.75

# ex = hei * 2

# '''
# PEMDAS
# ()
# **
# */
# +-
# '''

# op = 3 * (3 + 3) / 3 - 3

# print(ex)

# Number rounding
num = 8 / 3 
print(round(num))
print(round(num, 2))

# Floor

num2 = 8 // 3
print(num2)

# format strings
score = 3
height = 1.80
print(f"Your score is", score)
print(f"Your score is {score} and your height is {height}")
