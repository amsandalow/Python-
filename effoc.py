print ("welcome to python cafe!")
temp=input("do you want a hot drink or a cold drink? ")
if temp=="hot":
    sweetness=input ("would you like a sweet drink or bitter drink? ")
    if sweetness=="sweet":
        print ("I recomend a hot chocolate ")
    elif sweetness=="bitter":
        print ("i recomend a black coffe")
else:
    sweetness=input ("would you like a sweet drink or bitter drink? ")
    if sweetness=="sweet":
        print ("I recomend an iced frappicino")
    elif sweetness=="bitter":
        print ("i recomend an iced black")
