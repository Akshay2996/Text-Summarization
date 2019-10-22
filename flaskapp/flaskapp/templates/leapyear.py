x=int(input("enter any year")) 
d=0    
while(x>0):
    d=d+x%10
    x=x/10
print(d)    
