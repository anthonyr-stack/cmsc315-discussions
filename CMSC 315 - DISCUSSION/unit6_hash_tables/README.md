# Unit 6 Discussion: Dictionaries as Hash Tables

## Overview

This assignment uses Python dictionaries to demonstrate hash table behavior.

## Learning Objectives

- Insert key-value pairs
- Retrieve values efficiently
- Update existing values
- Remove entries
- Understand hashing concepts

## Requirements

1. Create and populate a dictionary.
2. Demonstrate lookup operations.
3. Demonstrate update operations.
4. Demonstrate delete operations.
5. Test edge cases.
6. Create a real-world scenario.

## Discussion Board Reflection

After completing the programming assignment, add this reflection to your initial discussion post in LEO.

Your reflection should be approximately 150–200 words and address the following questions:

1. What concepts or skills did you learn while completing this assignment?
2. What challenges did you encounter, and how did you overcome them?
3. Explain how hash tables behave, what collisions are, and how hash tables can improve efficiency.
While completing this assignment, I learned how Python dictionaries use hash tables to efficiently store and manage key-value pairs. Since I am interested in pursuing a career in network engineering, I decided to create a network device management system that stores device names and their corresponding IP addresses. This helped me understand how dictionaries can be applied to real-world networking tasks.

One challenge I encountered was understanding how to handle nonexistent keys without causing errors. I overcame this by using the get() and pop() methods with default values. I also learned that inserting an existing key updates its associated value instead of creating a duplicate entry.

Hash tables work by using a hash function to determine where data should be stored. A collision occurs when two different keys map to the same storage location. Python dictionaries handle collisions internally, allowing different keys to remain accessible. Hash tables improve efficiency because insertion, lookup, updating, and deletion typically have an average time complexity of O(1), compared to O(n) for linear searches. Overall, this assignment helped me understand why hash tables are valuable for managing large amounts of network information.
