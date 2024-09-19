#4.write a program to sort the array elements using bubble sort technique.

def bubblesort(arr):
    n=len(arr)
    for i in range(n-1):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [24,67,12,46,95]
bubblesort(arr)
print("Sorted array is :: ")
for i in arr:
    print(i)

