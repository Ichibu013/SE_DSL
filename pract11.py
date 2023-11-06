ary = []

def getdata(n):
    for i in range(0,n):
        ele = int(input('Enter the roll number of student:'))
        ary.append(ele)
    global key
    key = int(input('Enter the roll no to be searched:'))

def linearSearch(a,key):
    f = 0 
    for i in range(len(a)):
        if a[i]== key:
            f = f+1
    if f == 0:
        print('Student is absent')
    else:
        print('Student is present ')

def sentinalSearch(ary,n,key):
    last = ary[n-1]
    ary[n-1]=key
    i = 0
    while (ary[i]!=key):
        i+=1
    ary[n-1]=last
    if ((i<n-1) or (ary[n-1]==key)):
        print('Student is present ')
    else:
        print('Student is absent')


def binarySearch(ary,key,n):
    a = sorted(ary)
    l = 0
    r = n-1
    while l<r:
        mid = int((l+r)/2)
        if key>ary[mid]:
            l = mid+1
        elif key < ary[mid]:
            r = mid - 1
        elif key == ary[mid]:
            return mid
        else:
            return -1

def fibonacciSearch(ary,key,n):
    fib2 = 1
    fib1 = 0
    fib3 = fib1 + fib2
    while fib3<=n:
        fib2 = fib1
        fib1 = fib3
        fib3 = fib2 + fib1
        
    offset = 0
    
    while fib3>1:
        i = min(offset+fib1,n-1)
        if ary[i] > key:  
            fib3 = fib2
            fib2 = fib2 - fib1
            fib1 = fib3- fib2
        
        elif ary[i]< key:
            fib3 = fib1
            fib1 = fib2
            fib2 = fib3 - fib1
            offset = i

        else:
            return i
    if fib1 == 0 and ary[offset+1] == key:
        return offset+1
    return -1


n = int(input('Enter the number of student that attended training program:'))
getdata(n)
print('LIST OF CHOICES\n\t1]Search using Linear seacrh\n\t2]Search using Sentinal search')
print('\t3]Search using Binary search\n\t4]Search using Fibnoacci search')
while 1>0: 
    c = int(input('\t\tEnter you choice:'))
    if c == 1:
        linearSearch(ary,key)
    elif c == 2:
        sentinalSearch(ary,n,key)
    elif c == 3:
        r = binarySearch(ary,key,n)
        if r != -1:
            print('Student is absent')
        elif r == -1:
            print('Student is present ')
    elif c == 4:
        r = fibonacciSearch(ary,key,n)
        if r != -1:
            print('Student is absent')
        elif r == -1:
            print('Student is present')
    else:
        print('Entered choice is invalid')
    co = input('Do you wish to continue(y/n):')
    if co == 'y':
        continue
    else:
        break