import random
n = 0
counter = 0
while n!=6:    
    n = random.randint(1,6)
    print (n)
    counter+=1
print(f'It took {counter} rolls to get a 6.')