'''Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. 
Print the decimal value of each fraction on a new line with 6 places after the decimal.

Note: This challenge introduces precision problems. 
The test cases are scaled to six decimal places, though answers with absolute error of up to 10^-4 are acceptable.'''

def probability(arr):
    # Write your code here
    positive_number = []
    negative_number = []
    zeros = []
    for i in arr:
        if i > 0:
            positive_number.append(i)
        if i < 0 :
            negative_number.append(i)
        if i == 0:
            zeros.append(i)
    print("%.6f" %(len(positive_number)/len(arr)))
    print("%.6f" %(len(negative_number)/len(arr)))
    print("%.6f" %(len(zeros)/len(arr)))
    
n = int(input().strip())
arr = list(map(int, input().rstrip().split()))
probability(arr)