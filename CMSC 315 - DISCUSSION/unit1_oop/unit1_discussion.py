
"""
===========================================================
Unit 1 DISCUSSION: Python OOP, Namespaces, and Copying
===========================================================

INSTRUCTIONS:
In this assignment, you will build and explore object-oriented programming (OOP) concepts in Python.
You are provided with starter code containing TODO sections. Your task is to complete, modify, and
analyze the code to demonstrate understanding of inheritance, namespaces, and object copying.
"""

from copy import copy, deepcopy


# TODO 1:
# Create a parent class.
#
# Requirements:
# - Include at least one class variable.
# - Include at least two instance variables.
# - Include a constructor (__init__).
# - Include a method that returns or displays information about the object.
#
# Replace the pass statement with your implementation.

class ParentClass:
    device_type = "Network Device"

    def __init__(self, name, ip_address):
        self.name = name
        self.ip_address = ip_address

    def display_info(self):
        print(f"Device: {self.name}, IP: {self.ip_address}")


# TODO 2:
# Create a child class that inherits from the parent class.
#
# Requirements:
# - Use inheritance.
# - Add at least one new class variable.
# - Add at least two new instance variables.
# - Add at least one new method.
# - Override a method from the parent class.
#
# Replace the pass statement with your implementation.

class ChildClass(ParentClass):
    security_level = "High"

    def __init__(self, name, ip_address, firewall_status, ports):
        super().__init__(name, ip_address)
        self.firewall_status = firewall_status
        self.ports = ports

    def check_firewall(self):
        print(f"Firewall Status: {self.firewall_status}")

    def display_info(self):
        print(
            f"Device: {self.name}, IP: {self.ip_address}, "
            f"Firewall: {self.firewall_status}, "
            f"Ports: {self.ports}"
        )


# TODO 3:
# Create a function that demonstrates class namespaces and instance namespaces.
#
# Your function should:
# - Create at least two objects of the child class.
# - Access a class variable through the class itself.
# - Access the same class variable through an object.
# - Add a new attribute to only one object after it is created.
# - Display each object's namespace using __dict__.
# - Display information about the class namespace.

def demonstrate_namespaces():
    print("\n=== Namespace Demonstration ===")

    device1 = ChildClass("Router", "192.168.1.1", "Enabled", [80, 443])
    device2 = ChildClass("Switch", "192.168.1.2", "Disabled", [22, 80])

    print("Class variable:", ChildClass.security_level)
    print("Object variable:", device1.security_level)

    device1.location = "Server Room"

    print("Device 1 namespace:", device1.__dict__)
    print("Device 2 namespace:", device2.__dict__)

    print("Class namespace:", list(ChildClass.__dict__.keys()))


# TODO 4:
# Create a function that demonstrates shallow copying and deep copying.
#
# Requirements:
# - Create an object that contains nested mutable data.
# - Create a shallow copy.
# - Create a deep copy.
# - Modify the original object's nested data.
# - Display the original object, shallow copy, and deep copy.
# - Use comments to explain the difference between shallow and deep copying.

def demonstrate_copying():
    print("\n=== Copy Demonstration ===")

    original = ChildClass(
        "Firewall",
        "192.168.1.10",
        "Enabled",
        [80, 443]
    )

    shallow = copy(original)
    deep = deepcopy(original)

    # A shallow copy shares the nested list with the original.
    # A deep copy creates an independent copy of the nested list.

    original.ports.append(8080)

    print("Original ports:", original.ports)
    print("Shallow copy ports:", shallow.ports)
    print("Deep copy ports:", deep.ports)


# TODO 5:
# Complete the main function.
#
# Requirements:
# - Create at least one object from the parent class.
# - Create at least one object from the child class.
# - Demonstrate inheritance by calling methods.
# - Call your namespace demonstration function.
# - Call your copy demonstration function.

def main():
    print("=== Unit 1 OOP Assignment ===")

    print("\n=== Parent Object ===")
    parent = ParentClass("Main Server", "192.168.1.100")
    parent.display_info()

    print("\n=== Child Object ===")
    child = ChildClass(
        "Security Router",
        "192.168.1.1",
        "Enabled",
        [22, 80, 443]
    )

    child.display_info()
    child.check_firewall()

    # Demonstrate the inherited parent method.
    super_method = super(ChildClass, child)
    super_method.display_info()

    demonstrate_namespaces()
    demonstrate_copying()


if __name__ == "__main__":
    main()
