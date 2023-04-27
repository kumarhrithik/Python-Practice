# Given an array of integers, find the sum of its elements.

def simpleArraySum(ar):
    return sum(ar)

ar_count = int(input().strip())
ar = list(map(int, input().rstrip().split()))
result = simpleArraySum(ar)
print(result)