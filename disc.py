#################
# Discussion 02 #
#################  
# Higher Order Functions

# 1.5 
"""
Write a function that takes in a function cond and a number n and prints unmbers from 1 to n where calling cond on that number returns True.
"""

def keep_ints(cond, n):
    """
    Print out all integers 1..i..n where cond(i) is True.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> keep_ints(is_even, 5)
    2
    4
    """
    for i in range(n):
        if cond(i+1):
            print(i+1)

# 1.6 
"""
Write a function similar to keep_ints like before, but now it takes in a number n and returns a function that has one parameter cond. 
The returned function prints out numbers from 1 to n where calling cond on that number returns True.
"""

def make_keeper(n):
    """
    Returns a function which takes one parameter cond and prints out all integers 1..i..n where calling cond(i) returns True.

    >>> def is_even(x):
    ...     return x % 2 == 0
    >>> make_keeper(5)(is_even)
    2
    4
    """
    def cond_func(cond):
        for i in range(n):
            if cond(i+1):
                print(i+1)
    return cond_func

# 1.7 
"""
Write a function print delayed delays printing its argument until the next function call. print delayed takes in an argument x and returns a new function delay print. When delay print is called, it prints out x and returns another delay print.
"""

def print_delayed(x):
    """
    Return a new function. This new function, when called, will print out x and return another function with the same behavior.

    >>> f = print_delayed(1)
    >>> f = f(2)
    1
    >>> f = f(3)
    2
    >>> f = f(4)(5)
    3
    4
    """
    def delay_print(y):
        print(x)
        return print_delayed(y)
    return delay_print

# 1.8 
"""
Write a function print n that can take in an integer n and returns a repeatable print function that can print the next n parameters. After the nth parameter, it just prints ”done”.
"""

def print_n(n):
    """
    >>> f = print_n(2)
    >>> f = f("hi")
    hi
    >>> f = f("hello")
    hello
    >>> f = f("bye")
    done
    >>> g = print_n(1)
    """
    def inner_print(x):
        if n > 0:
            print(x)
            return print_n(n - 1)
        else:
            print("done")
            return print_n(n) 
    return inner_print

#################
# Discussion 04 #
#################  
# Recursion, Tree Recursion, Python Lists

# 1.1 
"""
Write a function that takes two numbers m and n and returns thier product. Assume m and n are positive integers. 
Use recursion, not nul or *!
"""

def multiply(m, n):
    """
    >>> multiply(5, 3)
    15
    """
    if n == 0:
        return 0
    else:
        return m + multiply(m, n - 1)

# 1.2 
"""
Implement the recursive is_prime function.
"""

def is_prime(n):
    """
    >>> is_prime(7)
    True
    >>> is_prime(10)
    False
    >>> is_prime(1)
    False
    """
    return prime_helper(n, n - 1)

def prime_helper(n, m):
    if n == 1:
        return False
    elif n % m == 0 and m != 1:
        return False
    elif m == 1:
        return True
    else: 
        return prime_helper(n, m - 1)
    
# 2.1 
"""
You want to go up a flight of stairs that has n steps. You can either take 1 or 2 steps each time. How many different ways can you go up this flight of stairs? Write a function count_stair_ways that solves this problem. Assume n is positive.
"""

def count_stair_ways(n):
    assert n > 1 and type(n) == int, "n must be a positive integer!"
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return count_stair_ways(n - 1) + count_stair_ways(n - 2)
    
# 2.2 
"""
Consider a special version of the count_stairways problem, where instead of taking 1 or 2 steps, we are able to take up to and including k steps at a time. 
Write a function count_k that figures out the number of paths for this scenario. Assume n and k are positive.
"""
def count_k(n, k):
    """
    >>> count_k(3, 3)
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    274
    >>> count_k(300, 1)
    1
    """
    sum_of_count = 0
    if n == 0 or n == 1 or k == 1:
        return 1
    elif n > k:
        for i in range(k):
            sum_of_count += count_k(n - i - 1, k)
    else:
        for i in range(n):
            sum_of_count += count_k(n - i - 1, n - i - 1)
    return sum_of_count

# 3.2
"""
Write a function that takes a list s and returns a new list that keeps only
the even-indexed elements of s and multiplies them by their corresponding
index.
"""
def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]

# 3.3
"""
Write a function that takes in a list and returns the maximum product that can be formed using nonconsecutive elements of the list. 
The input list will contain only numbers greater than or equal to 1.
"""
def max_product(s):
    """
    Return the maxium product that can be formed using non-consecutive elements of s.

    >>> max_product([10, 3, 1, 9, 2])
    90
    >>> max_product([5, 10, 5, 10, 5])
    125
    >>> max_product([])
    1
    """
    if len(s) == 0:
        return 1
    elif len(s) == 1:
        return s[0]
    else:
        return max(max_product(s[:-1]), max_product(s[:-2]) * s[-1])
    
# Whole Numbers
# (a)
"""
A hole number is a number in which every other digit dips below the digits immediately adjacent to it.
For example, the number 968 would be considered a hole number because the number 6 is smaller than
both of its surrounding digits. Assume that we only pass in numbers that have an odd number of digits.
Define the following function so that it properly identifies hole numbers.
"""
def check_hole_number(n):
    """
    >>> check_hole_number(123)
    False
    >>> check_hole_number(3241968)
    True
    >>> check_hole_number(3245968)
    False
    """
    digit_list = [int(x) for x in str(n)]
    even_digit = digit_list[1::2]
    for i in range(len(even_digit)):
        if even_digit[i] >= digit_list[2 * i] or even_digit[i] >= digit_list[2 * i + 2]:
            return False
    return True

# (b)
"""
Define the following function so that it properly identifies mountain numbers. A mountain number is a
number that either
i. has digits that strictly decrease from right to left OR strictly increase from right to left.

ii. has digits that increase from right to left up to some point in the middle of the number (not necessarily
the exact middle digit). After reaching the maximum digit, the digits to the left of the maximum
digit should strictly decrease.
"""
def check_mountain_number(n):
    """
    >>> check_mountain_number(103)
    False
    >>> check_mountain_number(153)
    True
    >>> check_mountain_number(123456)
    True
    >>> check_mountain_number(2345986)
    True
    """
    digit_list = [int(x) for x in str(n)]
    if len(digit_list) <= 2:
        return True
    is_up = True
    index = 0
    while is_up:
        if index == len(digit_list) - 1:
            return True
        elif digit_list[index] < digit_list[index + 1]:
            index += 1
            continue
        else:
            is_up = False
    while not is_up:
        if index == len(digit_list) - 1:
            return True
        elif digit_list[index] > digit_list[index + 1]:
            index += 1
            continue
        else: 
            return False