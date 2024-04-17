'''
하나하나 작은거 앞으로 보내자.
def insertionSort(arr):


# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)
'''
def insertionSort(arr):
	n = len(arr)  # 총 배열의 길이가 5이다.

	if n <= 1:
		return  # If the array has 0 or 1 element, it is already sorted, so return

	# Iterate over the array starting from the second element
	for i in range(1, n):  # 1 (11, 5)                            #2 (13,5)                #3 (5,5)
		# Store the current element as the key to be inserted in the right position
		key = arr[i]       # key= 11                              #key 12                 # key=5
		front = i - 1      # front = 1-1=0 =>12                   #front=2-1=1 =>12       # front=2=>13

		# Move elements greater than key one position ahead
		while front >= 0 and key < arr[front] : # 0==0 & 11 < 12    #1>0 and 12<12 False     #2>0 and 5<13          # 1>0 and 5<12
			arr[front + 1] = arr[front]        # 11에 12값을 대입.                             #5에 13을 대입해          # 5에 12 대입
			front -= 1  # front 1감소 (똑같이 index0)                                          #front=1               # front=0
			# [12, 12, 13, 5, 6]                                                            # [11, 12, 13, 13, 6]  #[11, 5, 5, 13, 6]

		# Insert the key in the correct position
		arr[front + 1] = key  # key = 12                                                    #key =5                # key = 12
		# [11, 12, 13, 5, 6]  # [11, 12, 13, 5, 6]                                          # [11, 12, 5, 13, 6]  # [11, 5, 12, 13, 6]


# Sorting the array [12, 11, 13, 5, 6] using insertionSort
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)