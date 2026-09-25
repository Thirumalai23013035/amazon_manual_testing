
def trap(arr):

    n = len(arr)
    print(arr)

    left =0
    right = n-1
    maxleft = arr[left]
    maxright = arr[right]
    water=0

    while left<right:

        if maxleft<=maxright:

            maxleft = max(maxleft,arr[left])
            water = water + maxleft - arr[left]
            left+=1

        else:

            maxright = max(maxright,arr[right])
            water= water+ maxright - arr[right]
            right-=1


    return water



n = int(input("Enter the size of list:"))
print("Enter the values of buildings:")
arr=[]

for i in range(n):
    arr.append(int(input()))

ans = trap(arr)

print(f"the water stored between buildings {ans} units")

    