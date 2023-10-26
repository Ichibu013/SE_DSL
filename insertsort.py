a = [11,23,45,1,33,83,99,12]
for i in range(1,len(a)):
    temp = a[i]
    for j in range(i,0,-1):
        if a[j]<a[j-1]:
            a[j] = a[j-1]
            a[j-1] = temp
            print(a)
        else:
            break
print(a)