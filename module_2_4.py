numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
Primes = [] #список простых чисел, что делятся только на себя (True)
Not_Primes = [] #список непростых чисел, что деляться не только на себя (False)
i = 0 # индекс
h = 0 # делитель
isprime = True

for i in range (0, len(numbers)):
    for h in range (2, numbers[i]-1):
        if numbers[i] % h == 0:
            isprime = False
            break
        else:
            isprime = True
    if numbers[i]==1:
        continue
    if isprime==True:
        Primes.append(numbers[i])
    if isprime==False:
        Not_Primes.append(numbers[i])

print('Primes', Primes)
print('Not_Primes', Not_Primes)







    #if numbers[i] == 1:
       # continue
    #if numbers[i] % h == 0:
        #continue
    #while 1>0:
        #h+=1
        #if h==numbers[i]:
          #  break
        #if numbers[i] % h == 0:
            #if h==numbers[i]:
             #   isprime = True
            #else:
            #    isprime=False
    #if isprime == False:
     #   Not_Primes.append(numbers[i])
    #if isprime == True:
    #    Primes.append(numbers[i])
#print(Not_Primes)
#print(Primes)

#Not_Primes.append(numbers[i])
#Primes.append(numbers[i])