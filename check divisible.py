

listNumbers= [];
x= int (input("Number of element: "))
n= int (input("Number the elements should be divided by: "))
for i in range(0, x):
    element = int(input())
    listNumbers.append(element)

print("the number in list", listNumbers, "that divisible by ", n , " : ")
listNumbers = list(dict.fromkeys(listNumbers))
def check_division (list,m):
     for i in list:
        if i%n == 0:
           print(i)

check_division(listNumbers,n)
