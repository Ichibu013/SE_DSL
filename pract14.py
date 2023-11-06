prct = []

def getdata():
    n = int(input('Enter the total number of students:'))
    for i in range(0,n):
        ele = input('Enter the percentage of student:')
        prct.append(ele)

def bubbleSort():
    bubsrt = prct
    n = len(bubsrt)
    for i in range(n-1):
        for j in range(0,n-i-1):
            if bubsrt[j] > bubsrt[j+1]:
                bubsrt[j],bubsrt[j+1] = bubsrt[j+1],bubsrt[j]
    o = 1
    print('Top 5 Students:-')
    for k in range(n-1,n-6,-1):
        print('\t',o,'.',bubsrt[k])
        o += 1

            

def selectionSort():
    bubsrt = prct
    n = len(bubsrt)
    for i in range(len(bubsrt)):
        for j in range(i,len(bubsrt)):
            if bubsrt[j] < bubsrt[i]:
                bubsrt[j],bubsrt[i] = bubsrt[i],bubsrt[j]
    o = 1
    print('Top 5 Students:-')
    for k in range(n-1,n-6,-1):
        print('\t',o,'.',bubsrt[k])
        o += 1
               

getdata()
print('\t1]Using Bubble Sort\t2]Using Selection Sort')
ch = int(input('ENTER YOUR CHOICE:-'))
while 1>0:
    if ch == 1:
        bubbleSort()
    elif ch == 2:
        selectionSort()
    else:
        print('ENTERED CHOICE IS INVALID')
    co = input('Do you wish to continue(y/n):')
    if co == 'y':
        continue
    else:
        break