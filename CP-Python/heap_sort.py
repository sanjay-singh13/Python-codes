import math

def parent(i):
    return math.floor((i-1)/2)

def left(i):
    return 2*i+1

def right(i):
    return 2*i+2


def max_heapify(a,heap_size,i):
    l = left(i)
    r = right(i)
    if l<heap_size and a[l]>a[i]:
        largest = l
    else:
        largest = i
    if r<heap_size and a[r]>a[largest]:
        largest = r
    if largest != i:
        a[i] = a[i]+a[largest]
        a[largest] = a[i]-a[largest]
        a[i] = a[i]-a[largest]
        max_heapify(a,heap_size,largest)


def build_heap(a):
    heap_size = len(a)
    i = math.floor(heap_size/2)
    while i>=0:
        max_heapify(a,heap_size,i)
        i = i-1


def heap_sort(a):
    build_heap(a)
    heap_size = len(a)
    i = heap_size-1
    while i>0:
        a[0] = a[0]+a[i]
        a[i] = a[0]-a[i]
        a[0] = a[0]-a[i]
        heap_size = heap_size - 1
        max_heapify(a,heap_size,0)
        i = i-1

print("Enter the array elements")
a = list(map(int,input().split()))
heap_sort(a)
print("Sorted Array using Heap Sort:")
print(a)

