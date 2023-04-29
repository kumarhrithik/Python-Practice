# The factorial of the integer , written , is defined as:

# Calculate and print the factorial of a given integer.

# For example, if n = 5 , we calculate 5x4x3x2x1  and get 120 .

def extraLongFactorials(n):
    # Write your code here
    num = 1
    for i in range(1, n+1):
        num *= i
    return num
n = int(input().strip())
print(extraLongFactorials(n))