# Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.
# Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
# It must be greater than the original word
# It must be the smallest word that meets the first condition
# Example
#w=abcd
# The next largest word is abcd .
# Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.
# Function Description
# Complete the biggerIsGreater function in the editor below.
# biggerIsGreater has the following parameter(s):
# string w: a word
def biggerIsGreater(w):
    # Write your code here
    result = ''
    length = len(w)
    w = list(w)
    i = length-2
    while i>= 0 and w[i]>=w[i+1]:
        i-=1
    if i == -1:
        result = "no answer"
    else:
        j = length-1
        while j >= i and w[j] <= w[i]:
            j -= 1
        w[i], w[j] = w[j], w[i]
        w = "".join(w)
        result = w[:i+1]+w[i+1:][::-1]
    return result

T = int(input().strip())
for T_itr in range(T):
    w = input()
    result = biggerIsGreater(w)
    print(result)