n=5
for i in range(n):
    print(" "*i,end=" ")
    for j in range(n-i):
        print("*",end=" ")
    print()      
n=5
for i in range(n):
    print(" "*(n-i-1
               ),end=" ")
    for j in range(i+1):
        print("*",end=" ")
    print() 
