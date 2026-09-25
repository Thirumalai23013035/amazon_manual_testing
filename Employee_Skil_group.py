def GroupAnagrams(arr):

    n = len(arr)
    mp = dict()

    for i in range(n):

        str1 = arr[i]

        key = ''.join(sorted(str1))

        if key not in mp:

            mp[key] = []

        mp[key].append(str1)


    return list(mp.values())

    

n = int(input("Enter the array size:"))
arr=[]
print("Enter the transactions :")
for i in range(n):
    arr.append(input())


ans = GroupAnagrams(arr)


print(ans)

        

