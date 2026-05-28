import random
n=1000000000
x=random.randint(1,n)
print (x)
for i in range(1,n+1):
    if i==x:
        print (f"you got it right in {i} guesses")
        break


