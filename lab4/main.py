from math import sqrt
from itertools import permutations
from typing import List


def find_longest_wire(w: int, heights: List[int]):
    counter: float = 0
    possible_lengths = []

    pillars_permutations_list = list(permutations(heights))

    for arr in pillars_permutations_list:
        for i in range(len(arr) - 1):
            if (i + 1) != len(arr):
                if arr[i] == arr[i + 1]:
                    wire_length_between_two_neighbor_pillars = w
                else:
                    wire_length_between_two_neighbor_pillars = sqrt((arr[i] - arr[i + 1]) ** 2 + w ** 2)
                counter += wire_length_between_two_neighbor_pillars

        result = round(counter, 2)
        possible_lengths.append(result)
        counter = 0

    return max(possible_lengths)


print(find_longest_wire(2, [3, 1, 3]))


print(find_longest_wire(100, [1, 1, 1, 1]))



