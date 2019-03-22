# QUICK SORT WHIT HOARE PARTITION SCHEME
# Angelo Gonzalez 
#Wikipedia: https://en.wikipedia.org/wiki/Quicksort
def partition(A,lo,hi):
    pivot = A[(lo+hi)//2]
    print("Pivot--> %d"  % pivot)
    i = lo
    j = hi
    while (i < j):
        while A[i] < pivot:
            i +=1           
        while A[j] > pivot:
            j -=1
        if (i < j):
            A[i] , A[j] = A[j], A[i]
            print("Array-->" , A)
            print("i:%d j:%d" % (i,j))
            i +=1
            j -=1            
    return j
def quicksort(A,lo,hi):
    if (lo < hi):
        p = partition(v1,lo,hi)
        quicksort(A,lo,p)
        quicksort(A,p +1 , hi)
#v1 = [61 , 32 , 75 , 26 , 76 , 68 , 30 , 25 , 76 , 15 , 64 , 31 , 27 , 94 , 46 , 22 , 99 , 75 , 61 , 23 , 71 , 99 , 74 , 52 , 2  , 76 , 4  , 13 , 87 , 8  , 98 , 54 , 62 , 36 , 70 , 62 , 45 , 48 , 87 , 33 , 54 , 100, 87 , 26 , 94 , 31 , 21 , 93 , 19 , 54 , 62 , 88 , 20 , 2  , 93 , 32 , 36 , 66 , 48 , 28 , 88 , 34 , 16 , 84 , 87 , 87 , 97 , 13 , 29 , 69 , 17 , 87 , 34 , 71 , 88 , 61 , 59 , 44 , 23 , 69 , 99 , 69 , 58 , 89 , 68 , 90 , 72 , 90 , 85 , 63 , 44 , 52 , 88 , 12 , 36 , 45 , 65 , 10 , 75 , 81]
v1 = [10,3,2,4,7,3,2,11,1]
quicksort(v1,0,len(v1)-1)
print("Sorted Array: ", v1)
