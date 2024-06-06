# README

## Type Annotations in Python 3

Type annotations in Python 3 allow developers to specify the expected data types of variables, function parameters, and return values. This feature enhances code readability and helps with static type checking, making it easier to catch type-related errors during development. Type annotations do not enforce type checking at runtime but provide hints that can be used by tools like IDEs and linters.

## Using Type Annotations to Specify Function Signatures and Variable Types

Type annotations can be added to function signatures to specify the expected types of arguments and return values. Similarly, you can annotate variables to indicate their types. Here are some examples:

### Function Signatures

```python
def add(x: int, y: int) -> int:
    return x + y

def greet(name: str) -> str:
    return f"Hello, {name}!"
```

### Variable Types

```python
age: int = 30
name: str = "Alice"
pi: float = 3.14159
is_active: bool = True
```

In the examples above, the types of function parameters and return values are specified, as well as the types of variables. These annotations serve as documentation and help tools understand the expected types, improving code quality and maintainability.

## Duck Typing

Duck typing is a concept in Python where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit type. The saying "If it looks like a duck and quacks like a duck, it's a duck" captures this idea. In duck typing, if an object implements the necessary methods, it can be used regardless of its actual type.

### Example of Duck Typing

```python
class Duck:
    def quack(self):
        print("Quack!")

class Person:
    def quack(self):
        print("I'm quacking like a duck!")

def make_it_quack(duck_like):
    duck_like.quack()

d = Duck()
p = Person()

make_it_quack(d)  # Output: Quack!
make_it_quack(p)  # Output: I'm quacking like a duck!
```

In this example, both `Duck` and `Person` classes have a `quack` method, so they can both be passed to the `make_it_quack` function, demonstrating duck typing.

## Validating Your Code with mypy

[mypy](http://mypy-lang.org/) is a static type checker for Python. It reads type annotations and checks the code for type consistency, helping to catch type errors before runtime. To validate your code with mypy, you need to install it and then run it on your codebase.

### Installation

You can install mypy using pip:

```sh
pip install mypy
```

### Running mypy

To check a Python file with mypy, use the following command:

```sh
mypy your_file.py
```

mypy will analyze the type annotations and report any type inconsistencies or errors. This helps ensure that your code adheres to the specified types, improving reliability and reducing the chances of runtime type errors.

### Example mypy Output

Consider the following Python code:

```python
def add(x: int, y: int) -> int:
    return x + y

result = add(10, "20")
```

Running mypy on this code will produce an error because the second argument to `add` is a string instead of an integer:

```sh
error: Argument 2 to "add" has incompatible type "str"; expected "int"
```

By fixing these type errors, you can improve the robustness of your code.