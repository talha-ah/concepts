# Encapsultion

Encapsulation is the process of binding the data and the functions that operate on the data together. In other words, it is wrapping up of data under a single unit. It is the mechanism that binds together code and the data it manipulates.

- data and methods hidden from the outside world - private methods/attributes
- some helper methods/attributes are private and can be accessed only from inside the class itself and provide some handlers/methods to the outside world like getters/setters

# Abstraction

Abstraction is the process of hiding the implementation details and showing only functionality to the user. In other words, it is a way to achieve security. Abstraction can be achieved with either abstract classes or interfaces.

- Unnecessary information hidden in the class (a method to hide the unnecassary/unwanted information)
- how something works is hidden from the outside world

# Polymorphism

Polymorphism (Many forms) is the ability of an object to take on many forms. The most common use of polymorphism in OOP occurs when a parent class reference is used to refer to a child class object.

- same method name, different implementation
- same method name, same implementation
- same method name, different number of parameters
- same method name, different type of parameters

```python

name = "Jim"  # str
print(len(name))

some_list = ["some", "name"]  # list
print(len(some_list))

# That's polymorphism in action, a single function (len) know how to handle different kinds of objects as expected!
```

# Inheritance
