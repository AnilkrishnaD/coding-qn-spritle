N = int(input())

puzzle = []
nums_in_order_input = [] 
for i in range(N):
    each_row = list(map(int, input().split()))
    puzzle.append(each_row)
    for j in each_row:
        nums_in_order_input.append(j)
    

def getInvCount(arr):
	arr1=[]
	for y in arr:
		for x in y:
			arr1.append(x)
	arr=arr1
	inv_count = 0
	for i in range(N * N - 1):
		for j in range(i + 1,N * N):
			# count pairs(arr[i], arr[j]) such that
			# i < j and arr[i] > arr[j]
			if (arr[j] and arr[i] and arr[i] > arr[j]):
				inv_count+=1
		
	
	return inv_count


# find Position of blank from bottom
def findXPosition(puzzle):
	# start from bottom-right corner of matrix
	for i in range(N - 1,-1,-1):
		for j in range(N - 1,-1,-1):
			if (puzzle[i][j] == 0):
				return N - i


# This function returns true if given
# instance of N*N - 1 puzzle is solvable
def isSolvable(puzzle):
	# Count inversions in given puzzle
	invCount = getInvCount(puzzle)

	# If grid is odd, return true if inversion
	# count is even.
	if (N & 1):
		return ~(invCount & 1)

	else: # grid is even
		pos = findXPosition(puzzle)
		if (pos & 1):
			return ~(invCount & 1)
		else:
			return invCount & 1
	

# print(puzzle)
result = isSolvable(puzzle)
#print(type(result))
original_nums = []

for i in range(N*N):
    original_nums.append(i)


#print(len(original_nums))
#print(len(nums_in_order_input))

if result == -1:
    arranged_nums = []
    for i in range(N*N):
        if nums_in_order_input[i] != original_nums[i]:
            arranged_nums.append(nums_in_order_input[i])
    print(arranged_nums)
else:
    print("null")


