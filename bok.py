b = []
c = []
d = {}
w = {}
sorted_value_l = []

def getdata():
    n = int(input('Number of Book entries:'))
    for i in range(0,n):
        r = input('Name of the book:')
        b.append(r)
        f = input('Cost of the booK:')
        c.append(f)

def con(b,c):
    j = 0
    for i in c:
        w = b[j]
        d[i] = w
        j = j+1

def dup(b):
    return list(dict.fromkeys(b))
    
def srtcst(d):
    con(b,c)
    w = list(d.keys())
    w.sort()
    return {i: d[i] for i in w}

def cnt(c):
    l = 0
    for i in c:
        if 500<=i:
            l = l+1
    return l

def l500(w):
    keys_l = list(d.keys())
    value_l = list(d.values())
    for i in keys_l:
        if (500 >= i):
            l = value_l[keys_l.index(i)]
            sorted_value_l.append(l)

getdata()
print("Choices:-\n\tA]Delete duplicate entries\n\tB]Display books in ascending order based on cost of books")
print("\tC]Count of books with cost more than 500\n\tD]Copy of books in a new list which has cost less than 500")
i = 0
w = srtcst(d)
print(w)
while i <1:
    choice = str(input('Enter your choice:'))
    if choice=='A':
        print('Lsit without duplicate entries:-',dup(b))
    elif choice == 'B':
        print('Asending order:-\n\t',srtcst(d))
    elif choice=='C':
        print('Count-',cnt(w))
    elif choice == 'D':
        print('Copy of list:',sorted_value_l)
    co = input('Do you wish to continue(y/n):')
    if co == 'y':
        continue
    else:
        break

