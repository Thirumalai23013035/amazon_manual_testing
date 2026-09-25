def maximum_subarray(arr):

    n = len(arr)
    curr_max=arr[0]
    max_sum = arr[0]

    for i in range(1,n):

        curr_max=max(curr_max+arr[i],arr[i])
        max_sum = max(curr_max,max_sum)

    return max_sum


n = int(input("Enter the array size:"))
arr=[]
print("Enter the product prices :")
for i in range(n):
    arr.append(int(input()))


ans = maximum_subarray(arr)

print(f"Maximum value that can be obtained from any comtinuous range is {ans}")