# -*- coding: utf-8 -*-
__author__ = 'yuzhou'
__date__ = '2017/2/12 20:29'


def zjpx(array):
    n = len(array)
    for i in xrange(1, n):
        key = array[i]
        j = i - 1
        while j >=0 and array[j] > key:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key


def xepx(array):
    # 设定步长
    step = len(array)/2
    while step > 0:
        for i in xrange(step, len(array)):
            while i >= step and array[i-step] > array[i]:
                array[i], array[i-step] = array[i-step], array[i]
                i -= step
        step /= 2
    return array


def select_sort(array):
    n = len(array)
    for i in xrange(0, n-1):
        index = i
        for j in xrange(i+1, n):
            if a[index] > a[j]:
                index = j
        a[i], a[index] = a[index], a[i]


def Bubble_Sort(array):
    n = len(array)
    for i in xrange(0, n-1):
        for j in xrange(0, n-1-i):
            if a[j+1] < a[j]:
                a[j+1], a[j] = a[j], a[j+1]


def kxpx(arrary, low, high):
    if low < high:
        i, j, key = low, high, arrary[low]
        while i<j:
            while i<j and key <= arrary[j]:
                j -= 1
            arrary[i] = arrary[j]
            arrary[j] = key
            while i<j and key >= arrary[i]:
                i += 1
            arrary[j] = arrary[i]
            arrary[i] = key
        kxpx(arrary, low, i-1)
        kxpx(arrary, j+1, high)

def HeadAjust(array, i, n):
    lchild = 2*i
    rchild = 2*i + 1
    max = i
    if i <= n/2:
        if lchild <= n and array[lchild] > array[max-1]:
            max = lchild
        if rchild <= n and array[rchild] > array[max-1]:
            max = rchild
        if max != i:
            array[max-1], array[i-1] = array[i-1], array[max-1]
            HeadAjust(array, max, n)

def BuildHead(array, n):
    for i in xrange(n, 0, -1):
        array[0], array[i-1] = array[i-1], array[0]
        HeadAjust(array, 1, i-1)


def merge(array, low, mid, high):
    b = []
    left_low, left_high = low, mid
    right_low, right_high = mid + 1, high

    while left_low <= left_high and right_low <= right_high:
        if array[left_low] <= array[right_low]:
            b.append(array[left_low])
            left_low += 1
        else:
            b.append(array[right_low])
            right_low += 1
    while left_low <= left_high:
        b.append(array[left_low])
        left_low += 1
    while right_low <= right_high:
        b.append(array[right_low])
        right_low += 1
    for i in xrange(len(b)):
        array[low] = b[i]
        low += 1
    del b

def merge_sort(array, low, high):
    mid = 0
    if low < high:
        mid = (low + high)/2
        merge_sort(array, low, mid)
        merge_sort(array, mid+1, high)
        merge(array, low, mid, high)


if __name__ == '__main__':
    a = [60, 71, 49,11, 82, 49, 3, 66]
    merge_sort(a, 0, len(a)-1)
    print a