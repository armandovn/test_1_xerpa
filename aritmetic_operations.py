"""
Contains function that represents the numbres from 0 to 9.
Contains four basic arithmetic functions like +, -, * and //
"""

def zero(x: dict = None) -> int:
    return op(0, x) if x else 0

def one(x: dict = None) -> int:
    return op(1, x) if x else 1

def two(x: dict = None) -> int:
    return op(2, x) if x else 2

def three(x: dict = None) -> int:
    return op(3, x) if x else 3

def four(x: dict = None) -> int:
    return op(4, x) if x else 4

def five(x: dict = None) -> int:
    return op(5, x) if x else 5

def six(x: dict = None) -> int:
    return op(6, x) if x else 6

def seven(x: dict = None) -> int:
    return op(7, x) if x else 7

def eight(x: dict = None) -> int:
    return op(8, x) if x else 8

def nine(x: dict = None) -> int:
    return op(9, x) if x else 9

def op(a: int, x: dict) -> int:
    """
    a: represents the first number of operation
    x: must be a dict with two values: 
        op: The operation to apply 
        val: The second number in the operation
    raise: TypeException if x is not a dict or it 
        doesn´t have the keys
    """
    if x["op"] == "+":
        return a + x["val"]
    if x["op"] == "-":
        return a - x["val"]
    if x["op"] == "*":
        return a * x["val"]
    if x["op"] == "//":
        return a // x["val"]

def times(x: int) -> dict:
    return {"op": "*", "val": x}

def plus(x: int) -> dict:
    return {"op": "+", "val": x}

def minus(x: int) -> dict:
    return {"op": "-", "val": x}

def divided_by(x: int) -> dict:
    return {"op": "//", "val": x}


if __name__ == '__main__':
    print(four(times(five()))) # print 20
    print(one(plus(eight()))) # print 9
    print(seven(minus(three()))) # print 4
    print(nine(divided_by(three()))) # print 3
    print(three(minus(nine()))) # print -6
    print(four(times(five(plus(five()))))) # print 60
    # The big one
    print(four(times(five(times(four(plus(eight(minus(nine()))))))))) # print 60