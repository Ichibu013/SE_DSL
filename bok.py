b = ['a','b']
c = [20,10]
d = {}
def getdata():
    n = int(input('Number of Book entries:'))
    for i in range(0,n):
        r = input('Name of the book:')
        b.append(r)
        f = input('Cost of the booK:')
        c.append(f)
def con(b,c):
    j = 0
    for i in b:
        w = c[j]
        d[i] = w
        j = j+1
def dup(b):
    return(list(dict.fromkeys(b)))
def srtcst(d):
    print(sorted(d))
con(b,c)
srtcst(d)

