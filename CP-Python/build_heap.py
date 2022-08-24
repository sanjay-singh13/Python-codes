import math

def parent(i):
    return math.floor((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2


def max_heapify(a,i):
    l = left(i)
    r = right(i)
    if l<len(a) and a[l]>a[i]:
        largest = l
    else:
        largest = i
    if r<len(a) and a[r]>a[largest]:
        largest = r
    if largest != i:
        a[i] = a[i]+a[largest]
        a[largest] = a[i]-a[largest]
        a[i] = a[i]-a[largest]
        max_heapify(a,largest)


def build_heap(a):
    i = math.floor(len(a)/2)
    while i>=0:
        max_heapify(a,i)
        i = i-1


print("Enter the array elements")
a = list(map(int,input().split()))
build_heap(a)
print("Max Heap for the above array is given below:")
print(a)



