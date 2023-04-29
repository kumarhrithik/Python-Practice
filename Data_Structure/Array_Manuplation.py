'''Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. 
Once all operations have been performed, return the maximum value in the array.
Example
n=10
queries = [[1,5,6],[4,8,7],[6,9,1]]
Queries are interpreted as follows:
    a b k
    1 5 3
    4 8 7
    6 9 1
Add the values of k between the indices a and b inclusive:
index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]
The largest value is 10 after all operations are performed.'''

def arrayManipulation(n, queries):
    arr = [0]*n
    for i in queries:
        for j in range(i[0], i[1] + 1):
            arr[j - 1] += i[2]
    return max(arr)

nm = input().split()
n = int(nm[0])
m = int(nm[1])
queries = []
for _ in range(m):
    queries.append(list(map(int, input().rstrip().split())))
result = arrayManipulation(n, queries)
print(result)