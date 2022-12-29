def selectionSort(array, size):
	
	for s in range(size):
		  minimum = s
	    for i in range(s + 1, size):
		      if array[i] < array[minimum]:
				  minimum = i
		  (array[s], array[minimum]) = (array[minimum], array[s])

arr = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    arr.append(ele)

size = len(arr)
selectionSort(arr, size)

print('Sorted Array in Ascending Order is :')
print(arr)

