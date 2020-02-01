def insertionSort(A):
    length = len(A)

    for j in range(1, length):
        key = A[j]
        i = j - 1
        while i > -1 and A[i] > key:
            A[i + 1] = A[i]
            i = i - 1
        A[i + 1] = key

    print(A)


def selectionSort(A):
    for i in range(len(A)):

        min_idx = i
        for j in range(i + 1, len(A)):
            if A[min_idx] > A[j]:
                min_idx = j

        A[i], A[min_idx] = A[min_idx], A[i]

    print(A)


def bubbleSort(A):
    for passnum in range(len(A) - 1, 0, -1):
        for i in range(passnum):
            if A[i] > A[i + 1]:
                temp = A[i]
                A[i] = A[i + 1]
                A[i + 1] = temp

    print(A)



def mergeSort(A):
    if len(A) > 1:
        mid = len(A) // 2
        left = A[:mid]
        right = A[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0

        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1


        while i < len(left):
            A[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            A[k] = right[j]
            j += 1
            k += 1


def countingsort(A, k):
    m = k + 1
    count = [0] * m

    for a in A:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            A[i] = a
            i += 1
    return A


A = [12, 1, 23, 4, 34, 11, 49]
print('Actual Array', end=' ')
print(A)


A = [12, 1, 23, 4, 34, 11, 49]
print('Insertion Sort:', end=' ')
insertionSort(A)

A = [12, 1, 23, 4, 34, 11, 49]
print('Bubble Sort:', end=' ')
bubbleSort(A)

A = [12, 1, 23, 4, 34, 11, 49]
print('Selection Sort:', end=' ')
selectionSort(A)

A = [12, 1, 23, 4, 34, 11, 49]
mergeSort(A)
print('Merge Sort:', end=' ')
print(A)

A = [12, 1, 23, 4, 34, 11, 49]
k = 0
for i in range(0, len(A)):
    if k < A[i]:
        k = A[i]
print('Counting Sort:', end=' ')
print(countingsort(A, k))
