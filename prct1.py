A = []
B = []
C = []

def getdata():
    global A,B,C
    n = int(input('Enter the number of Cricket students:'))
    a = []
    for i in range(0,n):
        a1 = input (F"Enter the name of Cricket student '{i+1}':")
        a.append(a1)
    A = a
    n = int(input('Enter the number of Badmintion students:'))
    b = []
    for i in range(0,n):
        b1 = input (F"Enter the name of Badmintion student '{i+1}':")
        b.append(b1)
    B = b
    n = int(input('Enter the number of Football students:'))
    c = []
    for i in range(0,n):
        c1 = input (F"Enter the name of Football student '{i+1}':")
        c.append(c1)
    C = c

def crinbat(A,B):
    for i in range(len(A)):
        for j in range (len(B)):
            if A[i] == B[j]:
                print(F"\t'{i+1}']",A[i])
    
def criobat(A,B):
    cb = A+B
    for i in cb[:]:
        if i in A and i in B:
            cb.remove(i)
    for j in range(len(cb)):
        print(F"\t'{j+1}']",cb[j]) 



def no_foot(A,B,C):
    cb = A+B+C
    for i in cb[:]:
        if i in A or i in B :
            cb.remove(i)
    print('Number of sutdents that neither play cricket nor badmintion:',len(cb))

def no_cri_bat(A,B,C):
    com = A+B+C
    for i in com[:]:
        if i in B:
            com.remove(i)       
    print('Number of students that play criket and badmintion:',len(list(dict.fromkeys(com))))

getdata()
print("Choices:-\n\tA]List of students who play both cricket and badminton\n\tB]List of students who play either cricket or badminton but not both")
print("\tC]Number of students who play neither cricket nor badminton\n\tD]Number of students who play cricket and football but not badminton")
choice = str(input('Enter your choice:'))
if choice=='A':
    crinbat(A,B)
elif choice == 'B':
    criobat(A,B)
elif choice=='C':
    no_foot(A,B,C)
elif choice == 'D':
    no_cri_bat(A,B,C)
