### Python Coding

1)Write a Python program that accepts a sentence and calculate the number of
letters and digits.Suppose the following input is supplied to the program:

Input :hello world! 123
the output should be:
LETTERS 10
DIGITS 3

### Code

```
s=input()

n = len(s)
alpha=0
digit =0

for i in range(n):

  if(s[i].isalpha()):
    alpha+=1

  elif(s[i].isdigit()):
    digit+=1

print(f"LETTERS {alpha}")
print(f"DIGITS {digit}")
```

### Image
 <img width="1897" height="980" alt="image" src="https://github.com/user-attachments/assets/30557c1a-b7c3-49c3-a3e8-8feeb8bb1290" />


2)Write a program which can compute the factorial of a given numbers.Theresults should be printed in a comma-separated sequence on a single
line.
following input is supplied to the program:8
Then, the output should be:40320

### Code

```

n = int(input())
fact=1

for i in range(1,n+1):
  fact = fact *i

print(fact)

```

### Image
 <img width="1902" height="973" alt="image" src="https://github.com/user-attachments/assets/cef1501c-edb8-4d3a-a0e8-81dae709996d" />

3)Write a Python program which accepts a sequence of comma separated 4 digit binary numbers as its input and then check whether they are divisible by 5 or not.
The numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010

### Code
```

arr =input().split(",")
res=[]

for i in arr:
  d = int(i,2)

  if(d%5==0):
      res.append(i)

print(",".join(res))
```
    

### Image
<img width="1907" height="965" alt="image" src="https://github.com/user-attachments/assets/30c2ef77-72e9-4eb0-bd5f-e93e60e49c56" />








