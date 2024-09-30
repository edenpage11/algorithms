import sys
import copy
import random

def pivotStart(A, start, end):
    return start

def pivotEnd(A, start, end):
    return end

def pivotMedian(A, start, end):
    mid = start + (end - start) // 2
    pivselect = [(A[start], start), (A[mid], mid), (A[end], end)]
    pivselect.sort(key=lambda x: x[0])
    return pivselect[1][1]

def pivotRandom(A, start, end):
    rand1 = random.randint(start, end)
    rand2 = random.randint(start, end)
    rand3 = random.randint(start, end)
    pivselect = [(A[rand1], rand1), (A[rand2], rand2), (A[rand3], rand3)]
    pivselect.sort(key=lambda x: x[0])
    return pivselect[1][1]

def partition(A, start, end):
    p = A[start]
    i = start + 1
    comparisons = 0
    for j in range(start + 1, end + 1):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
        comparisons += 1
    A[start], A[i-1] = A[i-1], A[start]
    return i - 1, comparisons

def qksrt(A, pivFunc, start = 0, end = None, comparisons = 0):
    if end == None:
        end = len(A) - 1
    if start >= end:
        return comparisons # base case
    piv = pivFunc(A, start, end)
    A[start], A[piv] = A[piv], A[start]
    j, tempcomparisons = partition(A, start, end)
    comparisons += tempcomparisons
    tempcomparisons = qksrt(A,pivFunc, start, j - 1)
    comparisons += tempcomparisons
    tempcomparisons = qksrt(A,pivFunc, j + 1, end)
    comparisons += tempcomparisons
    return comparisons

def main():
    A = []
    if len(sys.argv) < 2:
        print("Console Use case: python3 quicksort.py (testfile)")
        return
    try:
        with open(sys.argv[1], 'r') as f:
            for line in f:
                A.append(int(line.strip()))  # Strips newline characters and converts to int
    except FileNotFoundError:
        print(f"File not found: {sys.argv[1]}")
        return
    except ValueError:
        print(f"One or more lines in the file {sys.argv[1]} are not valid integers.")
        return
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return
    copyA = copy.deepcopy(A)
    comparisons = qksrt(A, pivotStart)
    print(f"Start pivot comparisons: {comparisons}")
    A = copy.deepcopy(copyA)
    comparisons = qksrt(A, pivotEnd)
    print(f"End pivot comparisons: {comparisons}")
    A = copy.deepcopy(copyA)
    comparisons = qksrt(A, pivotMedian)
    print(f"Median pivot comparisons: {comparisons}")
    A = copy.deepcopy(copyA)
    fullcomparisons = 0
    n = 10
    for _ in range(n):
        fullcomparisons += qksrt(A, pivotRandom)
    comparisons = fullcomparisons//n
    print(f"Random pivot comparisons: {comparisons}")

if __name__ == "__main__":
    main()
