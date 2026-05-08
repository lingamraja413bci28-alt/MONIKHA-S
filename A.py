for i in range(0,7):
    for j in range(0,5):
        if(i==0 and j in {1,2,3}):
            print('*',end=" ")
        elif(i in {1,2,3,4,5,6} and j in {0,4}):
            print('*',end=" ")
        elif(i==3 and j in {0,1,2,3,4}):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
            
print()       
for i in range(0,7):
    for j in range(0,5):
        if(i==0 and j in {1,2,3}):
            print('*',end=" ")
        elif(i in {1,2,3,4,5} and j in {0,4}):
            print('*',end=" ")
        elif(i==6 and j in {1,2,3}):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()
            
print()       
for i in range(0,7):
    for j in range(0,5):
        if(i==0 and j in {1,2,3}):
            print('*',end=" ")
        elif(i in {1,2,3,4,5} and j in {0}):
            print('*',end=" ")
        elif(i==3 and j in {1,2,3}):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()



print()       
for i in range(0,5):
    for j in range(0,5):
        if(i==0 and j in {0,4}):
            print('*',end=" ")
        elif(i in {1,2,3,4,5} and j in {0,4}):
            print('*',end=" ")
        elif(i==3 and j in {2}):
            print('*',end=" ")
        elif(i==1 and j in {1,3}):
            print('*',end=" ")
        elif(i==2 and j in {1,3}):
            print('*',end=" ")
        else:
            print(' ',end=" ")
    print()


