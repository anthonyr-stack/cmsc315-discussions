
"""
=========================================================
UNIT 4 DISCUSSION: BINARY SEARCH TREES (BST)
=========================================================

INSTRUCTIONS:
This assignment focuses on understanding and implementing a
Binary Search Tree (BST).

You will complete and modify the provided code while explaining
key concepts in your own words using comments and output.
"""


class Node:
    def __init__(self, value):
        # TODO (Student):
        # Store the node's value and initialize references
        # to the left and right child nodes.

        self.value = value
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        # TODO (Student):
        # Initialize an empty Binary Search Tree.

        self.root = None

    def insert(self, value):
        """
        TODO (Student):
        Insert a value into the BST.

        Requirements:
        - Use the recursive helper method.
        - Add comments explaining why insertion depends on
          whether a value is smaller or larger than the
          current node.
        """

        # Start insertion at the root of the tree.
        # Smaller values go left and larger values go right.
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST insertion.

        Requirements:
        - Create a new node when a position is found.
        - Insert smaller values into the left subtree.
        - Insert larger values into the right subtree.
        - Return the updated node reference.
        """

        # If the position is empty, create a new node.
        if node is None:
            return Node(value)

        # Insert smaller values into the left subtree.
        if value < node.value:
            node.left = self._insert_recursive(
                node.left, value
            )

        # Insert larger values into the right subtree.
        elif value > node.value:
            node.right = self._insert_recursive(
                node.right, value
            )

        # Duplicate values are ignored to keep IDs unique.
        return node

    def search(self, value):
        """
        TODO (Student):
        Search for a value in the BST.

        Requirements:
        - Return True if found.
        - Return False if not found.
        - Add comments explaining why BST search is often
          more efficient than linear search.
        """

        # BST search follows only one branch at each step.
        # A balanced BST searches in O(log n) time.
        # A linear search may need to check every value.
        return self._search_recursive(self.root, value)

    def _search_recursive(self, node, value):
        """
        TODO (Student):
        Implement recursive BST search.
        """

        # Reaching an empty position means not found.
        if node is None:
            return False

        # Return True when the value matches.
        if value == node.value:
            return True

        # Search left if the value is smaller.
        if value < node.value:
            return self._search_recursive(
                node.left, value
            )

        # Otherwise, search the right subtree.
        return self._search_recursive(node.right, value)

    def inorder(self):
        """
        TODO (Student):
        Return a list containing the values from an
        in-order traversal.
        """

        values = []

        # Begin traversal from the root.
        self._inorder_recursive(self.root, values)

        return values

    def _inorder_recursive(self, node, values):
        """
        TODO (Student):
        Implement in-order traversal.

        Requirements:
        - Visit the left subtree.
        - Visit the current node.
        - Visit the right subtree.
        - Add comments explaining why this traversal
          produces sorted output in a BST.
        """

        if node is not None:

            # First visit smaller values on the left.
            self._inorder_recursive(node.left, values)

            # Next add the current node's value.
            values.append(node.value)

            # Finally visit larger values on the right.
            self._inorder_recursive(node.right, values)

            # Left, root, right produces ascending order.


def main():
    print("=== UNIT 4: BINARY SEARCH TREES ===")

    # ===============================
    # TODO (Student): BUILD A TREE
    # ===============================
    #
    # Requirements:
    # 1. Create a BST object.
    # 2. Insert at least 7 values.
    # 3. Include values that go into both left
    #    and right subtrees.
    # 4. Display the values inserted.
    # 5. Use comments to explain why a BST is efficient at reducing search space for each step.

    print("\n=== TREE CONSTRUCTION ===")

    # Create a BST to organize network device IDs.
    tree = BST()

    # These values create left and right branches.
    device_ids = [50, 30, 70, 20, 40, 60, 80]

    print("Network device IDs:", device_ids)

    # Insert each device ID into the tree.
    for device_id in device_ids:
        tree.insert(device_id)

    print("BST created successfully.")

    # The BST uses comparisons to choose one branch,
    # reducing the search space at each level.
    # Balanced trees have O(log n) search performance.

    # ===============================
    # TODO (Student): IN-ORDER TRAVERSAL
    # ===============================
    #
    # Requirements:
    # 1. Perform an in-order traversal.
    # 2. Display the traversal results.
    # 3. Use comments to explain why the traversal produces
    #    sorted output in a BST.

    print("\n=== IN-ORDER TRAVERSAL ===")

    # In-order visits left, root, then right.
    # This displays BST values in ascending order.
    print("Sorted device IDs:", tree.inorder())

    # ===============================
    # TODO (Student): SEARCH TESTS
    # ===============================
    #
    # Requirements:
    # 1. Search for at least two values that exist.
    # 2. Search for at least two values that do not exist.
    # 3. Use comments to clearly explain the results.

    print("\n=== SEARCH TESTS ===")

    # Search for two existing device IDs.
    print("Search for 30:", tree.search(30))
    print("Search for 70:", tree.search(70))

    # Search for two device IDs that do not exist.
    print("Search for 25:", tree.search(25))
    print("Search for 90:", tree.search(90))

    # True means the device exists in the BST.
    # False means the device was not found.

    # ===============================
    # TODO (Student): EDGE CASES
    # ===============================
    #
    # Demonstrate at least one edge case.
    #
    # Example ideas:
    # - Traverse an empty tree
    # - Search an empty tree
    # - Insert duplicate values
    # - Create a tree with only one node
    #
    # Use comments to explain what happens and why.

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Search an empty BST.
    empty_tree = BST()
    print("Search empty tree:", empty_tree.search(10))

    # Edge Case 2: Traverse an empty BST.
    print("Traverse empty tree:", empty_tree.inorder())

    # Edge Case 3: Insert a duplicate device ID.
    # Duplicate values are ignored.
    tree.insert(30)
    print("After inserting duplicate 30:", tree.inorder())

    # Edge Case 4: Tree containing only one node.
    single_tree = BST()
    single_tree.insert(100)
    print("Single-node tree:", single_tree.inorder())


if __name__ == "__main__":
    main()
