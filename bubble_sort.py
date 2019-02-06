def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]




#get the array size
n = int(input("Enter the limit for array"))
arr=[]
print("Enter the array")
for i in range(n):
    temp = int(input(""))
    arr.insert(i,temp)

print("Initial array")
print(arr)
bubble_sort(arr)
print ("Sorted array")
print(arr)