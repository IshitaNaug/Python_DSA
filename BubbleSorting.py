#Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

#Modified Bubble Sort
def modified_bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, 0, -1):     # decreasing range
        for j in range(i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


sort_1 = [64, 34, 25, 12, 22, 11, 90]

print("Original array1:", sort_1)
print("Bubble Sort result:", bubble_sort(sort_1))


sort_2 = [64, 38, 20, 80, 25, 4, 90]
print("\nOriginal array2:", sort_2)
print("Modified Bubble Sort result:", modified_bubble_sort(sort_2)) 