# Count the number of occurrences of a character in a string

def check_freq(x):
    freq = {}
    for c in set(x):
       freq[c] = x.count(c)
    return freq

print(check_freq("abbabcbdbabdbdbabababcbcbab"))
