def LinearSearch(arr, n1, k):

    for j in range(0, n1):

        if (arr[j] == k):

            return j

    return -1

 
arr = []
n = int(input("Enter number of elements : "))

for i in range(0, n):
    ele = int(input())
    arr.append(ele)
k = int(input("Enter a Key "))

n1 = len(arr)

result = LinearSearch(arr, n1, k)

if(result == -1):

    print("Element not found")

else:

    print("Element found at index: ", result)
