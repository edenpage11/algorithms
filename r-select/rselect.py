import sys
import copy
import random
from mpmath import mp

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
    for j in range(start + 1, end + 1):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    A[start], A[i-1] = A[i-1], A[start]
    return i - 1

def quicksrt(A, pivFunc, start = 0, end = None):
    if end == None:
        end = len(A) - 1
    if start >= end:
        return # base case
    piv = pivFunc(A, start, end)
    A[start], A[piv] = A[piv], A[start]
    j = partition(A, start, end)
    quicksrt(A,pivFunc, start, j - 1)
    quicksrt(A,pivFunc, j + 1, end)

def qksrt(A, pivFunc, i, start = 0, end = None):
    if end == None:
        end = len(A) - 1
    if start >= end:
        return  A[start]# base case
    piv = pivFunc(A, start, end)
    A[start], A[piv] = A[piv], A[start]
    j = partition(A, start, end)
    if j == i - 1:
        return A[j]
    elif j > i - 1:
        return qksrt(A,pivFunc, i, start, j - 1)
    else:
        return qksrt(A,pivFunc, i, j + 1, end)

def main():
    A = []

    # READ FILE YOU WANT TO TEST
    if len(sys.argv) < 2:
        print("Console Use case: python3 quicksort.py (testfile/pi)")
        return
    if sys.argv[1].lower() != "pi":
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
        i = 10 # Element to search for (not zero index)
        copyA = copy.deepcopy(A)
        quicksrt(A, pivotRandom) # sort the list and then find the index we are looking for as a check
        print(f"Element in the sorted list: {A[i - 1]}")
        A = copy.deepcopy(copyA)
        elem = qksrt(A, pivotStart, i)
        print(elem)
        A = copy.deepcopy(copyA)
        elem = qksrt(A, pivotEnd, i)
        print(elem)
        A = copy.deepcopy(copyA)
        elem = qksrt(A, pivotMedian, i)
        print(elem)
        A = copy.deepcopy(copyA)
        elem = qksrt(A, pivotRandom, i)
        print(elem)
    # BACK TO PI ARRAY
    else:
        mp.dps = 1000000 + 1 
        pi_digits = str(mp.pi)[2:]
        pi_chunks = [pi_digits[i:i+10] for i in range(0, len(pi_digits), 10)]
        print("Searching pi")
        copyPi = copy.deepcopy(pi_chunks)
        quicksrt(copyPi, pivotRandom)
        print(f"Should be: {copyPi[len(copyPi)//2 - 1]}")
        print(qksrt(pi_chunks, pivotRandom, len(pi_chunks)//2))


if __name__ == "__main__":
    main()
