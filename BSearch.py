list=[1,2,3,4,5,6,7,8]
start=0
end=len(list)
midpoint=len(list)//2
key=int(input("What element are you looking for? "))

while key!=list[midpoint]:
    if key>list[midpoint]:
        start=midpoint
        midpoint=(start+end)//2
        print(midpoint)
        
    else:
     end=midpoint
     midpoint=(start+end)//2
     print(midpoint)
        
print(f"We found the element {key} in index: {midpoint} ")
        
        
#v.2
