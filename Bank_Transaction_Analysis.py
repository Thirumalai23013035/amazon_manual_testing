def Bank_Transaction_Analysis(arr,k):

    n = len(arr)
    mp = dict()
    sum1=0
    count=0

    for i in range(n):

        sum1 = sum1 + arr[i]

        if sum1-k in mp:

            count = count + mp[sum1-k]

        mp[sum1]=mp.get(sum1,0)+1

    return count

n = int(input("Enter the array size:"))
arr=[]
print("Enter the transactions :")
for i in range(n):
    arr.append(int(input()))

k = int(input("Target: "))

ans = Bank_Transaction_Analysis(arr,k)

print(f" number of continuous transaction groups whose sum is exactly equal to the target amount:{ans}")

        

