'''
You are given an array of integers of size n, where each element in the array represents
the number of test cases that passed in a regression test,
(There is no value before the first regression entry)

1.- Count the number of times that the quantity of passed test cases increases from the previous measurement
    - The minimumIncreases() function must return said count.

2.- Print the quantity of test cases PASSED between the first regression try and the latest

Example:

passedTests = [10,12,18,18,30]

count = 3

Expected return: 3

Expected print: 20
'''

def minimumIncreases(arr):
    count = 0
    for i in range(len(arr)-1):
        if arr[i] != arr[i+1]:
            count+=1
    return count


def passedQty(arr):
    firstIter = arr.pop(0)
    lastIter = arr.pop()
    passedTestQty = lastIter - firstIter
    return passedTestQty


passedTests = [10,12,18,18,18,24,29,30,40]

print("Number of times of passed test cases between iterations: " + str(minimumIncreases(passedTests)))
print("Passed test cases between first and last iteration: " + str(passedQty(passedTests)))