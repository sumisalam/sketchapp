a=[]
print("Enter the total number elements:")
t=int(input())
print("enter the elements:")
for i in range(t):
    elem=int(input())
    a.append(elem)

list1=sorted(a)
print(list1)

p=int(input("Enter a number : "))
if p in list1:
    index_of_p = list1.index(p)
    print("Index of ",p," is ",index_of_p)
else:
    for i in list1:
        if i>p:
            j=list1.index(i)
            list1.insert(j,p)
            print(p," is added")
            print(list1)
            break
    else:
        print(p,"is added")
        list1.append(p)
        print(list1)
        index_of_p = list1.index(p)
        print("Index of ",p," is ",index_of_p)
