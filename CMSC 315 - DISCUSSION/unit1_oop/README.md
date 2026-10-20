Unit 1 Discussion: Python OOP, Namespaces, and Copying

Overview

This assignment explored object-oriented programming concepts in Python, including inheritance, namespaces, shallow copying, and deep copying. I created a program based on cybersecurity and network management to demonstrate how classes and objects can organize information about network devices.

Implementation

Parent Class

I created a parent class called ParentClass that represented a network device. The class included a class variable called device_type and two instance variables, name and ip_address. I also implemented a display_info() method to display device information.

Child Class

I created a child class called ChildClass that inherited from ParentClass. I used super() to initialize inherited attributes and added firewall_status and ports as new instance variables.

I also created a check_firewall() method and overrode display_info() to display additional information.

Namespaces

I demonstrated the difference between class and instance namespaces by creating multiple network device objects. I accessed class variables through the class and an object, added a unique attribute to one object, and used __dict__ to examine their namespaces.

Shallow and Deep Copying

I used Python's copy() and deepcopy() functions to demonstrate object copying. The shallow copy shared the original object's nested mutable list, while the deep copy maintained an independent list.

After modifying the original list, I compared the results to observe how each copy behaved.

Student-Created Extension

I added a scan_ports() method that displayed the ports stored in a network device object's list. This extension demonstrated how additional functionality could be incorporated into an existing class.

The method simulated checking configured ports rather than performing a real network scan.

Memory Behavior

Each object stored its own instance attributes. Class variables were shared through the class rather than duplicated for every object.

The ports list grew as additional values were appended. A shallow copy created a new outer object but retained references to nested mutable data, while a deep copy created independent nested data structures.

For a list containing n ports, copying the list's contents required O(n) additional memory. Shallow copying the object itself required O(1) additional memory because it reused the existing list.

Conclusion

This assignment demonstrated how object-oriented programming could help organize network management applications. Inheritance reduced repeated code, namespaces helped separate shared and individual attributes, and object copying showed how mutable data could affect program behavior.

These concepts could be useful when developing larger cybers
