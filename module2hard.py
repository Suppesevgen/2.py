import random
n=random.randrange(3,21)

result=''
# i первое число
# j второе число
print('Number:',n)

for i in range (1,n):
    for j in range (i+1,n):
        if n % (i + j) ==0:
            if (i == j):
                continue
            result += str(i) + str(j)

print('Result:',result)