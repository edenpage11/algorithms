import numpy as np
# Sequence Alignment Alogorithm

# TODO: Read in the two strings from the input file

# TODO: Generate numpy matrix of size (len(string1)+1) x (len(string2)+1) filled with zeros
# n x m matrix where n is the length of string1 and m is the length of string2

# TODO: Fill in the first row and first column with the gap penalty * n or m (whichever is non-zero)

# TODO: Fill in the rest of the matrix with the minimum of the three possible values:
# 1. The value down 1 row and left 1 column + match/mismatch score: A[i-1, j-1] + match/mismatch score
# 2. The value below + gap penalty: A[i-1, j] + gap penalty
# 3. The value left 1 column + gap penalty: A[i, j-1] + gap penalty

# Given two strings, find their sizes and generate a matrix of size (len(string1)+1) x (len(string2)+1) filled with zeros


# def generate_matrix(string1, string2):
#     n = len(string1)
#     m = len(string2)
#     matrix = np.zeros((n+1, m+1))
#     return matrix

def import_text(text_path):
    with open(text_path, 'r') as file:
        text_list = file.readlines()
        gap_cost, mismatch_cost = text_list[1].strip().split(" ")
        string1 = text_list[2].strip()
        string2 = text_list[3].strip()
        return gap_cost, mismatch_cost, string1, string2


def generate_matrix(string1, string2):
    n = len(string1)
    m = len(string2)
    matrix = np.zeros((n+1, m+1, 2))
    return matrix

# Given a matrix, fill in the first row and first column with the gap penalty * n or m (whichever is non-zero)


def base_case(matrix, gap_cost):
    n, m, z = matrix.shape
    for i in range(1, n):
        matrix[i, 0, 0] = gap_cost * i
        matrix[i, 0, 1] = 2
    for j in range(1, m):
        matrix[0, j, 0] = gap_cost * j
        matrix[0, j, 1] = 3
    return matrix


def min_case(case_1, case_2, case_3):
    sorted_cases = sorted([case_1, case_2, case_3], key=lambda x: x[0])
    return sorted_cases[0]


def fill_matrix(matrix, string1, string2, mismatch_cost, gap_cost):
    n, m, z = matrix.shape
    for i in range(1, n):
        for j in range(1, m):
            case_1 = np.array(
                [matrix[i-1, j-1, 0] + (0 if string1[i-1] == string2[j-1] else mismatch_cost), 1])
            case_2 = np.array([matrix[i-1, j, 0] + gap_cost, 2])
            case_3 = np.array([matrix[i, j-1, 0] + gap_cost, 3])
            best_case = min_case(case_1, case_2, case_3)
            matrix[i, j, 0], matrix[i, j, 1] = best_case

# Given two strings and a matrix, find the optimal alignment
# TODO: make the innermost value of the matrix actually be a tuple that tells you which case it came from so you can backtrack to determine the optimal alignment: (value, case)
    # it'll be the values that are originally set to zero and the case will be none:
    # TODO: create enum for each case:


def get_penalty(solved_matrix):
    return solved_matrix[-1, -1, 0]


def reconstruction(matrix, string1, string2):
    i = len(string1)
    j = len(string2)
    finalstring1 = ""
    finalstring2 = ""
    while (j > 0 or i > 0):
        match matrix[i, j, 1]:
            case 1:
                # Case 1: Diagonal move (match/mismatch)
                finalstring1 = string1[i - 1] + finalstring1
                finalstring2 = string2[j - 1] + finalstring2
                i -= 1
                j -= 1
            case 2:
                # Case 2: Upward move (gap in string2)
                finalstring1 = string1[i - 1] + finalstring1
                finalstring2 = "-" + finalstring2
                i -= 1
            case 3:
                # Case 3: Leftward move (gap in string1)
                finalstring1 = "-" + finalstring1
                finalstring2 = string2[j - 1] + finalstring2
                j -= 1
    return finalstring1, finalstring2


def main():
    gap_cost, mismatch_cost, string1, string2 = import_text(
        "problem17.8nw.txt")
    matrix = generate_matrix(string1, string2)
    matrix = base_case(matrix, int(gap_cost))
    fill_matrix(matrix, string1, string2, int(mismatch_cost), int(gap_cost))
    penalty = get_penalty(matrix)
    print(penalty)
    str1, str2 = reconstruction(matrix, string1, string2)
    print(str1)
    print(str2)


if __name__ == "__main__":
    main()
