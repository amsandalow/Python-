import random
numlist=[]
for i in range (100):
    n=100
    x=random.randint(1,n)
    low=1
    high=n
    mid=(low+high)//2
    found=False
    attempts=0
    while found==False:
        mid=(low+high)//2
        if x>mid:
            low=mid
            attempts=attempts+1
        elif x<mid:
            high=mid
            attempts=attempts+1
        else:
            found=True
            numlist.append(attempts)
avg= (sum (numlist))
avg= avg/len(numlist)
print (avg)
