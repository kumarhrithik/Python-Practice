'''Given an array of integers and a target value, determine the number of pairs of array elements that have a difference equal to the target value.
Example
k=1
arr= [1,2,3,4]
There are three values that differ by k=1: 2-1=1 ,3-2=1 , and 4-3=1. Return 3.'''
from collections import Counter

def pair_diff(k, arr):
    # Write your code here
    elem = Counter(arr)
    pairs = 0
    
    for i in arr:
        if i+k in elem:
            pairs += 1
        if i-k in elem:
            pairs += 1
        del elem[i]
    return pairs


first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
k = int(first_multiple_input[1])
arr = list(map(int, input().rstrip().split()))
result = pair_diff(k, arr)