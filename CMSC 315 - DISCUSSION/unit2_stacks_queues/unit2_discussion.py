
"""
===========================================================
UNIT 2 DISCUSSION: STACKS AND QUEUES (PYTHON)
===========================================================

OVERVIEW:
This assignment introduces two fundamental data structures:
the Stack (LIFO) and the Queue (FIFO).

Real-world scenario: IT Help Desk Ticket Management
"""

from collections import deque


class Stack:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the stack.
        # Hint: A Python list can be used to store stack values.
        self.items = []

    def push(self, value):
        # TODO (Student): Add value to the stack.
        # Add a short comment explaining why this operation supports LIFO behavior.

        # New items go on top, so they are removed first (LIFO).
        self.items.append(value)

    def pop(self):
        # TODO (Student): Remove and return the most recently added value.
        # Improve or explain empty-stack handling.
        # What should happen if the stack is empty?

        if self.is_empty():
            return "Stack is empty. Nothing to remove."

        # Remove the most recently added item.
        return self.items.pop()

    def peek(self):
        # TODO (Student): Return the top value without removing it.
        # Add a comment explaining what peek does.

        if self.is_empty():
            return "Stack is empty. Nothing to view."

        # View the newest item without removing it.
        return self.items[-1]

    def is_empty(self):
        # TODO (Student): Return True if the stack has no values.
        return len(self.items) == 0


class Queue:
    def __init__(self):
        # TODO (Student): Create the internal data structure for the queue.
        # Hint: collections.deque is useful for efficient queue operations.
        self.items = deque()

    def enqueue(self, value):
        # TODO (Student): Add value to the back of the queue.
        # Add a short comment explaining why this operation supports FIFO behavior.

        # New tickets join the back of the line (FIFO).
        self.items.append(value)

    def dequeue(self):
        # TODO (Student): Remove and return the value from the front of the queue.
        # Explain or improve empty-queue handling.

        if self.is_empty():
            return "Queue is empty. No tickets to process."

        # Remove the oldest ticket first.
        return self.items.popleft()

    def front(self):
        # TODO (Student): Return the front value without removing it.
        # Add a comment explaining what front returns.

        if self.is_empty():
            return "Queue is empty. No tickets available."

        # View the oldest ticket without removing it.
        return self.items[0]

    def is_empty(self):
        # TODO (Student): Return True if the queue has no values.
        return len(self.items) == 0


def main():
    print("=== UNIT 2: STACKS AND QUEUES ===")
    print("Real-World Scenario: IT Help Desk\n")

    # ===============================
    # TODO (Student): STACK DEMO
    # ===============================
    # Requirements:
    # 1. Create a Stack object.
    # 2. Add at least 4 values to the stack.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate LIFO behavior.
    # 5. Show what happens when pop() is used on an empty stack.
    #
    # Edge Cases:
    # 6. Show what happens when peek() is used on an empty stack.
    # 7. Create a stack with only one item, remove it,
    #    and verify the stack is empty afterward.

    print("=== STACK DEMO (LIFO) ===")
    print("Tracking recently completed IT support actions.\n")

    stack = Stack()

    actions = [
        "Reset password",
        "Install printer",
        "Update software",
        "Restart server"
    ]

    for action in actions:
        stack.push(action)
        print("Action recorded:", action)

    print("\nMost recent action:", stack.peek())

    print("\nRemoving actions in LIFO order:")

    while not stack.is_empty():
        print("Removed:", stack.pop())

    print("\nTesting pop on an empty stack:")
    print(stack.pop())

    print("\nTesting peek on an empty stack:")
    print(stack.peek())

    print("\nTesting a stack with one item:")

    single_stack = Stack()
    single_stack.push("Check network connection")

    print("Removed:", single_stack.pop())
    print("Is the stack empty?", single_stack.is_empty())

    # ===============================
    # TODO (Student): QUEUE DEMO
    # ===============================
    # Requirements:
    # 1. Create a Queue object.
    # 2. Add at least 4 values to the queue.
    # 3. Improve the print statements so they clearly explain what is happening.
    # 4. Demonstrate FIFO behavior.
    # 5. Show what happens when dequeue() is used on an empty queue.
    #
    # Edge Cases:
    # 6. Show what happens when front() is used on an empty queue.
    # 7. Create a queue with only one item, remove it,
    #    and verify the queue is empty afterward.

    print("\n=== QUEUE DEMO (FIFO) ===")
    print("Processing incoming IT support tickets.\n")

    queue = Queue()

    tickets = [
        "Ticket 1: Reset password",
        "Ticket 2: Install printer",
        "Ticket 3: Update software",
        "Ticket 4: Fix network connection"
    ]

    for ticket in tickets:
        queue.enqueue(ticket)
        print("Ticket added:", ticket)

    print("\nNext ticket:", queue.front())

    print("\nProcessing tickets in FIFO order:")

    while not queue.is_empty():
        print("Processed:", queue.dequeue())

    print("\nTesting dequeue on an empty queue:")
    print(queue.dequeue())

    print("\nTesting front on an empty queue:")
    print(queue.front())

    print("\nTesting a queue with one item:")

    single_queue = Queue()
    single_queue.enqueue("Ticket 5: Update antivirus")

    print("Processed:", single_queue.dequeue())
    print("Is the queue empty?", single_queue.is_empty())


if __name__ == "__main__":
    main()
