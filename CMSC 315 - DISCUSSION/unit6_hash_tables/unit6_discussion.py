
"""
====================================================
UNIT 6 DISCUSSION: Python Dictionaries as Hash Tables
====================================================
Author: Anthony Romero
Scenario: Network Device Management System
====================================================
"""


def main():
    print("=== UNIT 6: DICTIONARIES AS HASH TABLES ===")

    # ===============================
    # CREATE A HASH TABLE
    # ===============================

    print("\n=== INSERT OPERATIONS ===")

    # Create an empty dictionary.
    network_devices = {}

    # Python dictionaries behave like hash tables.
    # A hash function determines where each key-value
    # pair is stored, allowing efficient access.

    network_devices["Router1"] = "192.168.1.1"
    network_devices["Switch1"] = "192.168.1.2"
    network_devices["Firewall1"] = "192.168.1.3"
    network_devices["AccessPoint1"] = "192.168.1.4"
    network_devices["Server1"] = "192.168.1.5"

    print("Network devices:", network_devices)

    # ===============================
    # LOOKUP OPERATIONS
    # ===============================

    print("\n=== LOOKUP OPERATIONS ===")

    # Dictionaries use the hash of a key to locate
    # its associated value without searching every entry.

    print("Router1 IP:", network_devices["Router1"])
    print("Server1 IP:", network_devices["Server1"])

    # ===============================
    # UPDATE OPERATIONS
    # ===============================

    print("\n=== UPDATE OPERATIONS ===")

    print("Before update:", network_devices)

    # Assigning a new value to an existing key replaces
    # the previous value without creating a duplicate key.

    network_devices["Switch1"] = "192.168.1.10"

    print("After update:", network_devices)

    # ===============================
    # DELETE OPERATIONS
    # ===============================

    print("\n=== DELETE OPERATIONS ===")

    print("Before deletion:", network_devices)

    # Removing a key also removes its associated value
    # and decreases the dictionary size by one.

    del network_devices["Firewall1"]

    print("After deletion:", network_devices)

    # ===============================
    # EDGE CASES
    # ===============================

    print("\n=== EDGE CASES ===")

    # Edge Case 1: Lookup a missing key.
    # Using get() with a default value prevents a KeyError.

    print("\nEdge Case 1: Missing key lookup")
    print(network_devices.get("Router2", "Device not found"))

    # Edge Case 2: Delete a missing key.
    # Using pop() with a default value prevents a KeyError.

    print("\nEdge Case 2: Delete missing key")
    print(network_devices.pop("Switch2", "Device not found"))

    # Edge Case 3: Insert a duplicate key.
    # The existing value is replaced instead of
    # creating another entry.

    print("\nEdge Case 3: Duplicate key")
    print("Before:", network_devices["Router1"])

    network_devices["Router1"] = "192.168.1.20"

    print("After:", network_devices["Router1"])

    # Edge Case 4: Lookup in an empty dictionary.
    # The dictionary returns the specified default value.

    print("\nEdge Case 4: Empty dictionary")

    empty_dictionary = {}

    print(empty_dictionary.get("Router1", "Dictionary is empty"))

    # ===============================
    # FINAL RESULTS
    # ===============================

    print("\n=== FINAL NETWORK DEVICES ===")

    for device, ip_address in network_devices.items():
        print(device, ":", ip_address)

    print("\nTotal devices:", len(network_devices))


if __name__ == "__main__":
    main()
