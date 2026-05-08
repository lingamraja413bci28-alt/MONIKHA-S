n=5
for i in range(n):
    for j in range(n):
        print('*',end=" ")



print()
n=int(input("Enter the no:"))
for i in range(n):
    for j in range(n):
        print('*',end=" ")
    print()



print()
n=5
for i in range(n):
    for j in range(i+1):
        print('*',end=" ")
    print()




print()
n=5
for i in range(n):
    for j in range(i,n-1):
         print('*',end=" ")
    print()



print()
for i in range(n):
    for j in range(i+1):
        print('*',end=" ")
    print()
for i in range(n):
    for j in range(i,n-1):
        print('*',end=" ")
    print()





print()
n=int(input("Enter the no:"))
for i in range(n):
    for j in range(n):
        print('a',end=" ")
    print()



print()
n=int(input("Enter the no:"))
for i in range(n):
    for j in range(n):
        print(j,end=" ")
    print()

print()
for i in range(0,7):
    for j in range(0,5):
        if(i==0 and j in {1,2,3}):
            print('*',end=" ")
        elif(i in {1,2,3,4,5,6} and j in {0,4}):
            print('*',end=" ")
        elif(i==3 and j in {0,1,2,3,4}):
            print('*',end=" ")
        else:
            print('*',end=" ")
    print()
            
            

        
    
    

