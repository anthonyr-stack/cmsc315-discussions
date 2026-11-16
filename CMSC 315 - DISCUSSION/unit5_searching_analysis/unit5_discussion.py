
"""
=====================================================
UNIT 5 DISCUSSION: SEARCH ALGORITHMS (LINEAR vs BINARY)
=====================================================

This program compares linear search and binary search
using small and large sorted datasets.

It also demonstrates edge cases and explains the
efficiency of both algorithms.
"""


def linear_search(lst, target):
    """
    Search the list from beginning to end.
    Return the index if found, or -1 if not found.

    Time Complexity: O(n)
    """

    # Linear search checks each element one at a time.
    # In the worst case, it checks all n elements.
    # Therefore, its time complexity is O(n).
    for i in range(len(lst)):

        # Return the index if the target matches.
        if lst[i] == target:
            return i

    # Return -1 when the target is not found.
    return -1


def binary_search(lst, target):
    """
    Search a sorted list by repeatedly dividing
    the search range in half.

    Time Complexity: O(log n)
    """

    # Set the starting and ending boundaries.
    left = 0
    right = len(lst) - 1

    while left <= right:

        # Find the middle index.
        middle = (left + right) // 2

        # Return the index if the target is found.
        if lst[middle] == target:
            return middle

        # If the target is larger, eliminate
        # the left half of the remaining list.
        elif lst[middle] < target:
            left = middle + 1

        # If the target is smaller, eliminate
        # the right half of the remaining list.
        else:
            right = middle - 1

    # Return -1 if the target is not found.
    return -1


def main():
    print("=== UNIT 5: SEARCH ALGORITHMS ===")

    # ===============================
    # SMALL DATASET
    # ===============================

    print("\n=== SMALL DATASET TEST ===")

    # Create a small sorted list of student scores.
    small_data = [55, 67, 72, 81, 90, 95]

    # Search for an existing score.
    target = 81

    print("Dataset:", small_data)
    print("Searching for:", target)

    print("Linear Search:",
          linear_search(small_data, target))

    print("Binary Search:",
          binary_search(small_data, target))

    # Both algorithms return index 3 because
    # the score 81 exists at that position.

    # Search for a score that does not exist.
    missing = 100

    print("\nSearching for missing value:", missing)

    print("Linear Search:",
          linear_search(small_data, missing))

    print("Binary Search:",
          binary_search(small_data, missing))

    # Both return -1 because 100 is not in the list.

    # ===============================
    # LARGE DATASET
    # ===============================

    print("\n=== LARGE DATASET TEST ===")

    # Create a sorted list containing 100,000 numbers.
    large_data = list(range(1, 100001))

    # Search for the last element.
    target = 100000

    print("Dataset size:", len(large_data))
    print("Searching for:", target)

    print("Linear Search:",
          linear_search(large_data, target))

    print("Binary Search:",
          binary_search(large_data, target))

    # Both searches return index 99999.
    #
    # Linear search must examine all 100,000
    # elements to find the last value.
    #
    # Binary search repeatedly cuts the search
    # range in half, requiring far fewer checks.
    #
    # This demonstrates why binary search is
    # more efficient for large sorted datasets.

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASE TESTS ===")

    # Edge Case 1: Empty list
    empty_list = []

    print("\nEmpty List:")
    print("Linear Search:",
          linear_search(empty_list, 81))
    print("Binary Search:",
          binary_search(empty_list, 81))

    # Both return -1 because the list has no elements.

    # Edge Case 2: Single-element list
    single_list = [81]

    print("\nSingle-Element List:")
    print("Linear Search:",
          linear_search(single_list, 81))
    print("Binary Search:",
          binary_search(single_list, 81))

    # Both return index 0 because the target
    # is the only element in the list.

    # Edge Case 3: Target at first position
    scores = [55, 67, 72, 81, 90]

    print("\nTarget at First Position:")
    print("Linear Search:",
          linear_search(scores, 55))
    print("Binary Search:",
          binary_search(scores, 55))

    # Both return index 0.
    # Linear search finds the target immediately.
    # Binary search requires additional comparisons.


if __name__ == "__main__":
    main()
