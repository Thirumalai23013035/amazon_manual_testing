n = int(input("Enter the size of list:"))
print("Enter the student ID's")
arr =[]

for i in range(0,n):
    arr.append(int(input()))
seen = set()
left =0
maxlen = float('-inf')

for i in range(n):


    while arr[i] in seen:

        seen.remove(arr[left])
        left+=1

    seen.add(arr[i])

    maxlen = max(maxlen,i-left+1)


print(f"the maximum length of such a sequence : {maxlen}")



