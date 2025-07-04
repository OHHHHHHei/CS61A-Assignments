def unique_digits(n):
    """Return the number of unique digits in positive integer n.

    >>> unique_digits(8675309) # All are unique
    7
    >>> unique_digits(13173131) # 1, 3, and 7
    3
    >>> unique_digits(101) # 0 and 1
    2
    """
    "*** YOUR CODE HERE ***"
    num = 0
    while n != 0:
        curr_digit = n % 10
        n = n // 10
        if has_digit(n, curr_digit):
            continue
        else:
            num += 1
    return num

def has_digit(n, k):
    """Returns whether k is a digit in n.

    >>> has_digit(10, 1)
    True
    >>> has_digit(12, 7)
    False
    """
    assert k >= 0 and k < 10
    "*** YOUR CODE HERE ***"
    while n != 0:
        digit = n % 10
        if k == digit:
            return True
        n = n // 10
    return False
    




