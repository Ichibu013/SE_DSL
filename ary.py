def partition(a,start,end):
    pivot = a[start]
    low = start + 1
    high = end
    while True:
        while low <= high and a[high]>=pivot:
            high = high - 1
        while low <= high and a[low]<=pivot:
            low = low + 1
        if low <= high:
            a[low],a[high]=a[high],a[low]
        else:
            break
    a[start],a[high]=a[high],a[start]
    return high
    
def quickSorrt(a,start,end):
    if start>=end:
        return
    p = partition(a,start,end)
    quickSorrt(a,start,p-1)
    quickSorrt(a,p+1,end)

a = [15,6,13,17,61,29,21,5,94,7]
quickSorrt(a,0,len(a)-1)
print(a)