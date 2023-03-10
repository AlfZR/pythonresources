print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# Lowered names
combined_string = name1 + name2
lower_name = combined_string.lower()
# TRUE

t = lower_name.count("t")
r = lower_name.count("r")
u = lower_name.count("u")
e = lower_name.count("e")

tsum= t+r+u+e

# LOVE
l = lower_name.count("l")
o = lower_name.count("o")
v = lower_name.count("v")
e = lower_name.count("e")

lsum = l + o + v + e

compat = str(tsum) + str(lsum)

conv = int(compat)

if conv < 10 or conv > 90:
    print(f"Your score is {conv}, you go together like coke and mentos.")
elif conv >= 40 and conv <= 50:
    print(f"Your score is {conv}, you are alright together.")
else:
    print(f"Your score is {compat}.")