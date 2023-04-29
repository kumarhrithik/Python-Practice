'''Given a square matrix, calculate the absolute difference between the sums of its diagonals.
For example, the square matrix  is shown below
1 2 3
4 5 6
9 8 9  
The left-to-right diagonal = 1+5+9 = 15. The right to left diagonal = 3+5+9 = 17. Their absolute difference is|15-17|=2. '''

def diagonalDifference(arr):
    left_to_right_diagonal = []
    right_to_left_diagonal = []
    for i in range(len(arr)):
        left_to_right_diagonal.append(arr[i][i])
        right_to_left_diagonal.append(arr[i][-i-1])
    diagonal_difference = abs(sum(left_to_right_diagonal)-sum(right_to_left_diagonal))
    return diagonal_difference


n = int(input().strip())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

result = diagonalDifference(arr)
print(result)