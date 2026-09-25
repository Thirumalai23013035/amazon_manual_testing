def maximum_product(arr):

    n = len(arr)
    maxprod = arr[0]
    minprod = arr[0]
    ans =0
    prod =1

    for i in range(1,n):

        prod = prod * arr[i]

        if(arr[i]<0):
            temp = maxprod
            maxprod = minprod
            minprod = temp

        maxprod = max(maxprod*arr[i],arr[i])
        minprod = min(minprod*arr[i],arr[i])




        ans = max(ans,maxprod)

    return ans

n = int(input("Enter the array size:"))
arr=[]
print("Enter the Product sales:")
for i in range(n):
    arr.append(int(input()))


ans = maximum_product(arr)

print(f"the maximum product that can be obtained from any continuous range of sales-related values:{ans}")

        
