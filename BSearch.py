list=[1,2,3,4,5,6,7]
midpoint=len(list)//2
key=int(input("What element are you looking for? "))

while key!=list[midpoint]:
    if key>list[midpoint]:
        list=list[midpoint:]
        midpoint=len(list)//2
    else:
        list=list[:midpoint]
        midpoint=len(list)//2
print("We found the element! ")
        
        