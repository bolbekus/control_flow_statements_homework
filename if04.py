def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    n = 0
    if a > 0:
        n += 1

    if b > 0:
        n += 1

    if c > 0:
        n += 1


    return n

print(main(-2,4,1))