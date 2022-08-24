import math

def parent(i):
    return math.floor((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2


def min_heapify(a,heap_size,i):
    l = left(i)
    r = right(i)
    if l<heap_size and a[l]<a[i]:
        smallest = l
    else:
        smallest = i
    if r<heap_size and a[r]<a[smallest]:
        smallest = r
    if smallest != i:
        a[i] = a[i]+a[smallest]
        a[smallest] = a[i]-a[smallest]
        a[i] = a[i]-a[smallest]
        min_heapify(a,heap_size,smallest)


def priority_queue(a):
    heap_size = len(a)
    i = math.floor(heap_size/2)
    while i>=0:
        min_heapify(a,heap_size,i)
        i = i-1

def heap_min(a):
    return a[0]

def extract_min(a):
    heap_size = len(a)
    if heap_size < 1:
        print("heap underflow")
    minE = a[0]
    a[0] = a[heap_size-1]
    heap_size = heap_size - 1
    min_heapify(a,heap_size,0)
    return minE

print("Enter the array elements")
a = list(map(int,input().split()))
priority_queue(a)
print("Max Heap for the above array is given below:")
print(a)

print(extract_min(a))
print(a)
