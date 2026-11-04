
"""
==================================================
Unit 3 DISCUSSION: List Operations (Insert, Delete, Search)
==================================================

This program demonstrates insertion, deletion, and searching
in Python lists, including edge cases and performance.
"""


def insert_at(lst, index, value):
    """
    Insert a value at the specified index.
    """
    # Inserting shifts existing elements to the right.
    # Inserting at the beginning or middle takes O(n) time.
    # Inserting at the end is usually O(1) amortized time.
    lst.insert(index, value)


def delete_at(lst, index):
    """
    Remove and return a value at the specified index.
    Return None if the index is invalid.
    """
    # Check that the index is within the list boundaries.
    # This prevents an IndexError from occurring.
    if index < 0 or index >= len(lst):
        return None

    # Removing an element shifts later elements to the left.
    # Deleting from the beginning or middle takes O(n) time.
    # Deleting from the end takes O(1) time.
    return lst.pop(index)


def search_value(lst, value):
    """
    Search for a value and return its index.
    Return -1 if the value is not found.
    """
    # Linear search checks each element sequentially.
    # It takes O(n) time in the worst case.
    for index in range(len(lst)):
        if lst[index] == value:
            return index

    return -1


def main():
    print("=== UNIT 3: LIST OPERATIONS ===")

    # ===============================
    # INSERTION TESTS
    # ===============================

    print("\n=== INSERTION TESTS ===")

    # Create a list containing several values.
    numbers = [10, 20, 30, 40, 50]
    print("Original list:", numbers)

    # Insert at the beginning.
    # Existing elements shift one position to the right.
    insert_at(numbers, 0, 5)
    print("After inserting 5 at beginning:", numbers)

    # Insert into the middle of the list.
    insert_at(numbers, 3, 25)
    print("After inserting 25 in middle:", numbers)

    # Insert at the end of the list.
    insert_at(numbers, len(numbers), 60)
    print("After inserting 60 at end:", numbers)

    # ===============================
    # DELETION TESTS
    # ===============================

    print("\n=== DELETION TESTS ===")

    # Delete the first element.
    removed = delete_at(numbers, 0)
    print("Removed from beginning:", removed)
    print("Updated list:", numbers)

    # Delete an element from the middle.
    removed = delete_at(numbers, 2)
    print("Removed from middle:", removed)
    print("Updated list:", numbers)

    # Delete the last element.
    removed = delete_at(numbers, len(numbers) - 1)
    print("Removed from end:", removed)
    print("Updated list:", numbers)

    # ===============================
    # SEARCH TESTS
    # ===============================

    print("\n=== SEARCH TESTS ===")

    # Search for a value that exists.
    result = search_value(numbers, 30)
    print("Searching for 30: Found at index", result)

    # Search for a value that does not exist.
    result = search_value(numbers, 100)

    if result == -1:
        print("Searching for 100: Value not found")
    else:
        print("Searching for 100: Found at index", result)

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Delete using an invalid index.
    # The function returns None instead of crashing.
    result = delete_at(numbers, 100)
    print("Deleting invalid index 100:", result)

    # Edge Case 2: Insert into an empty list.
    empty_list = []
    insert_at(empty_list, 0, 99)
    print("Inserting into empty list:", empty_list)

    # Edge Case 3: Delete from an empty list.
    another_empty_list = []
    result = delete_at(another_empty_list, 0)
    print("Deleting from empty list:", result)

    # ===============================
    # REAL-WORLD SCENARIO
    # ===============================

    print("\n=== REAL-WORLD SCENARIO ===")

    # A network administrator maintains a list
    # of connected devices on a network.
    devices = ["Router", "Switch", "Firewall"]
    print("Connected devices:", devices)

    # Add a new device to the network.
    insert_at(devices, 1, "Access Point")
    print("After adding Access Point:", devices)

    # Search for a specific network device.
    result = search_value(devices, "Firewall")
    print("Firewall found at index:", result)

    # Remove a disconnected device.
    removed = delete_at(devices, 0)
    print("Disconnected device:", removed)
    print("Updated connected devices:", devices)


if __name__ == "__main__":
    main()
