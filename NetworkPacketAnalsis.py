def Network_analysis(arr):

    n = len(arr)
    seen = set()
    maxlen =0

    for i in range(n):
        seen.add(arr[i])

    for s in seen:

        if s-1 not in seen:
            ele = s
            streak =1

            while ele+1 in seen:

                streak+=1
                ele+=1

            maxlen = max(maxlen,streak)

    return maxlen


n = int(input("Enter the array size:"))
arr=[]
print("Enter the Network Packets :")
for i in range(n):
    arr.append(int(input()))


ans = Network_analysis(arr)

print(f" the length of the longest sequence of consecutive numbers:{ans}")

        
