from enum import Enum
import random
import os


def parse_input(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file.readlines()]


class PivotStrategy(Enum):
    FIRST = 1
    RANDOM = 2
    MEDIAN_OF_THREE = 3
    LAST = 4


def choose_pivot(array, strategy=PivotStrategy.FIRST, start_index=0, end_index=0):
    if strategy == PivotStrategy.FIRST:
        return array[start_index], start_index
    elif strategy == PivotStrategy.RANDOM:
        pivot_index = random.randint(start_index, end_index)
        return array[pivot_index], pivot_index
    elif strategy == PivotStrategy.MEDIAN_OF_THREE:
        mid = (start_index + end_index) // 2
        candidates = [
            (array[start_index], start_index),
            (array[mid], mid),
            (array[end_index], end_index)
        ]
        candidates.sort(key=lambda x: x[0])
        # Return the median value and its index
        return candidates[1][0], candidates[1][1]
    elif strategy == PivotStrategy.LAST:
        return array[end_index], end_index


def start_quicksort(array, pivot_strategy=PivotStrategy.FIRST):
    num_comparisons = 0
    num_comparisons = quicksort(
        array, pivot_strategy, 0, len(array) - 1, num_comparisons)
    return array, num_comparisons


def quicksort(array, pivot_strategy=PivotStrategy.FIRST, start_index=0, end_index=0, num_comparisons=0):
    # Base case
    if (end_index - start_index) <= 0:
        # Returns the total number of comparisons made
        # print(num_comparisons)
        return num_comparisons
    else:
        # Count the number of comparisons
        num_comparisons += (end_index - start_index)

        pivot, pivot_index = choose_pivot(
            array, pivot_strategy, start_index, end_index)

        # Swap pivot to the first element
        array[start_index], array[pivot_index] = array[pivot_index], array[start_index]

        # The inequality index is the first element greater than the pivot
        # TODO: possibly off by 1
        inequality_index = start_index + 1

        for partition_index in range(inequality_index, end_index + 1):
            if array[partition_index] < pivot:
                array[partition_index], array[inequality_index] = array[inequality_index], array[partition_index]
                inequality_index += 1

        # Swap pivot to the correct position
        array[start_index], array[inequality_index -
                                  1] = array[inequality_index - 1], array[start_index]

        # Recursively sort the partitions and accumulate comparisons
        num_comparisons = quicksort(
            array, pivot_strategy, start_index, inequality_index - 2, num_comparisons)
        num_comparisons = quicksort(
            array, pivot_strategy, inequality_index, end_index, num_comparisons)

        # print(num_comparisons)
        return num_comparisons


def main():
    file_paths = [
        r"C:\Users\jarre\Documents\School\Algorithms\quicksort\problem5.6test1.txt",
        r"C:\Users\jarre\Documents\School\Algorithms\quicksort\problem5.6test2.txt",
        r"C:\Users\jarre\Documents\School\Algorithms\quicksort\problem5.6.txt"
    ]

    for file_path in file_paths:
        array = parse_input(file_path)
        array_copy = array.copy()

        file_name = os.path.basename(file_path)
        for pivot_strategy in PivotStrategy:
            array_copy = array.copy()  # Make a copy of the array
            sorted_array, comparisons = start_quicksort(
                array_copy, pivot_strategy)
            print(
                f"\nFile: {file_name}, Pivot Strategy: {pivot_strategy.name}, Total comparisons: {comparisons}")


if __name__ == "__main__":
    main()
