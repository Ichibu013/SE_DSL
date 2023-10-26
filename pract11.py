ary = []

def getdata(n):
    for i in range(0,n):
        ele = int(input('Enter the roll number of student:'))
        ary.append(ele)
    global key
    key = int(input('Enter the element to be found:'))

def linearSearch(a,key):
    f = 0 
    for i in range(len(a)):
        if a[i]== key:
            f = f+1
    if f == 0:
        print('Element not found')
    else:
        print('Element found at',i,'index')

def sentinalSearch(ary,n,key):
    last = ary[n-1]
    ary[n-1]=key
    i = 0
    while (ary[i]!=key):
        i+=1
    ary[n-1]=last
    if ((i<n-1) or (ary[n-1]==key)):
        print('Element found')
    else:
        print('Element not found')

def insertSort(ary):
    for i in range(1,len(ary)):
        temp = ary[i]
    for j in range(i,0,-1):
        if ary[j]<ary[j-1]:
            ary[j] = ary[j-1]
            ary[j-1] = temp
        else:
            break

n = int(input('Enter the number of student that attended training program:'))
getdata(n)
print(ary)

linearSearch(ary,key)
sentinalSearch(ary,n,key)

