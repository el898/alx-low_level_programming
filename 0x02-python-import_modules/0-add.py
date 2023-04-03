def add(a, b):
     """My addition function
     Args:
         a: first integer
         b: second integer
     Returns:
         The return value. a + b
    """
    return (a + b)
a = 1
b = 2

total = add(a, b)
print("{:d} + {:d} = {:d}".format(a, b, total))
