# Basic calculator

With this project you can make basic operations like +, -, * or //
The operations must have the follow strcuture: 

```python
    number(operation(number()))
```

while this structure be respect the operations should work well with N items:

```python
    four(times(five(four(times(five(four(times(five()))))))))
    four(times(five()))
    one(plus(eight()))
```

### It is important to identify that the operations are solve from right to left, 
### the results are always integers and they don't respect the hierarchy for example:

```python
  four(times(five(plus(five())))
```

This operation will be start to solve with operation:

```python
    five(plus(five())): return 10
```

Then the operation looks like:

```python
    four(times(10)): return 40
```