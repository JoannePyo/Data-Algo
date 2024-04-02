'''
def partition(arr, low, high):  


def quickSort(arr, low, high):       


data = [1, 7, 4, 1, 10, 9, -2]
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
'''

def partition(arr, low, high):                   #(arr,0,6)                                                                         #(arr, 1,6)
	pivot = arr[high]                              #pivot = -2                                                                        #pivot = 1
	i = low-1                                      # i =-1                                                                            # i=0
	for j in range(low,high):                      #(0,6)   #(1,6)  #(3,6)  #(4,6)  #(5,6)                                            #(1,6)   #(2,6) #(3,6)                     #(4,6) #(5,6) #6
		if arr[j] <= pivot:                          #1 <=-2  #7<=-2  #4<=-2  #10<=-2 #9<=-2                                            #7<=1    #4<=1  # 1<=1                     #10<=1 #9<=1
			i = i+1                                                                                                                                 # i=1
			arr[i], arr[j] = arr[j], arr[i]                                                                                                         #7,1 = 1,7 [-2,1,4,7,10,9,1]
	(arr[i + 1], arr[high]) = (arr[high], arr[i + 1])                                    #1,-2=-2,1 (swapping) [-2,7,4,1,10,9,1]                                                             #arr[1+1],arr[6]=> 4,1 = 1,4 [-2,1,1,7,10,9,4]
	return i+1                                                                           #return 0                                                                                           #return 2

def quickSort(arr, low, high):         #(arr,0,6)                                                                    #(0, -1)
	if low < high:                       #0 < 6 True                                                                   # False
		pi = partition(arr, low, high)     #위로
		quickSort(arr, low, pi-1)                                                         #(arr,0, pi=0=>0-1=> -1)                                                                            #(arr, 1, pi=2-1 => 1)
		quickSort(arr, pi+1, high)                                                                                       #(arr, 0+1 => 1, 6)


data = [1, 7, 4, 1, 10, 9, -2]
size = len(data)
quickSort(data, 0, size - 1)
print('Sorted Array in Ascending Order:')
print(data)
