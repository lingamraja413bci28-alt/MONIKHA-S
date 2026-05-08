L = [2, 2, 3, 4, 5, 6, 6, 7, 8, 8, 8, 10, 3]
counts = {}
for num in L:
    counts[num] = counts.get(num, 0) + 1
seen = set()
for num in L:
    if counts[num] == 2 and num not in seen:
        print(num)
        seen.add(num)






data = input("Enter 10 integers separated by space: ")
numbers = list(map(int, data.split()))
MyList1 = []
MyList2 = []
for num in numbers:
    
    if num % 2 == 0 and num % 3 != 0:
        MyList1.append(num)
        
   
    if num % 9 == 0:
        MyList2.append(num)

print(*(MyList1))
print(*(MyList2))
