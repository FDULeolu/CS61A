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
        


#################
# Discussion 05 #
#################  
# Python Lists, Trees, Mutability

from notes import *

# 1.1
"""
Write a function that returns the height of a tree. Recall that the height of a tree
is the length of the longest path from the root to a leaf.
"""
def height(t):
    """
    Return the height of a tree.

    >>> t = tree(3, [tree(5, [tree(1)]), tree(2)])
    >>> height(t)
    2
    """

    if is_leaf(t):
        return 0
    else:
        return max(height(b) for b in branches(t)) + 1
    

# 1.2
"""
Write a function that takes in a tree and squares every value. It should return a
new tree. You can assume that every item is a number.
"""
def square_tree(t):
    """
    Return a tree with the square of every element in t
    >>> numbers = tree(1,
    ...                [tree(2,
    ...                      [tree(3),
    ...                       tree(4)]),
    ...                 tree(5,
    ...                      [tree(6,
    ...                            [tree(7)]),
    ...                       tree(8)])])
    >>> print_tree(square_tree(numbers))
    1
     4
      9
      16
     25
      36
       49
      64
    """

    if is_leaf(t):
        return tree(label(t) ** 2)
    else:
        return tree(label(t) ** 2, [square_tree(b) for b in branches(t)])
    

# 1.3
"""
Write a function that takes in a tree and a value x and returns a list containing the
nodes along the path required to get from the root of the tree to a node containing
x.
If x is not present in the tree, return None. Assume that the entries of the tree are
unique.
"""
def find_path(tree, x):
    if label(tree) == x:
        return [label(tree)]
    elif not is_leaf(tree):
        path = [label(tree)]
        for b in branches(tree):
            subpath = find_path(b, x)
            if subpath:
                return path + subpath
        return None
    else:
        return None


# 2.2
"""
Write a function that takes in a value x, a value el, and a list and adds as many
el’s to the end of the list as there are x’s. Make sure to modify the original
list using list mutation techniques.
"""
def add_this_many(x, el, lst):
    """ 
    Adds el to the end of lst the number of times x occurs in lst.

    >>> lst = [1, 2, 4, 2, 1]
    >>> add_this_many(1, 5, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5]
    >>> add_this_many(2, 2, lst)
    >>> lst
    [1, 2, 4, 2, 1, 5, 2, 2]
    """

    while x > 0:
        lst.append(el)
        x -= 1


# 2.3
"""
Write a function that takes in a sequence s and a function fn and returns a dictionary.
The values of the dictionary are lists of elements from s. Each element e in a list
should be constructed such that fn(e) is the same for all elements in that list.
Finally, the key for each value should be fn(e).
"""
def group_by(s, fn):
    """
    >>> group_by([12, 23, 14, 45], lambda p: p // 10)
    {1: [12, 14], 2: [23], 4: [45]}
    >>> group_by(range(-3, 4), lambda x: x * x)
    {0: [0], 1: [-1, 1], 4: [-2, 2], 9: [-3, 3]}
    """

    result = {}
    for num in s:
        if fn(num) not in result:
            result[fn(num)] = [num]
        else:
            result[fn(num)].append(num)

    sorted_keys = sorted(result.keys())
    sorted_dict = {key: result[key] for key in sorted_keys}

    return sorted_dict


# Quiz 1 So Many Options
# (a)
"""
Implement the following function partition_options which outputs all the ways to partition a number total using numbers no larger than biggest.
"""
def partition_options(total, biggest):
    """
    >>> partition_options(2, 2)
    [[2], [1, 1]]
    >>> partition_options(3, 3)
    [[3], [2, 1], [1, 1, 1]]
    >>> partition_options(4, 3)
    [[3, 1], [2, 2], [2, 1, 1], [1, 1, 1, 1]]
    """

    if total == 0:
        return [[]]
    elif total < 0 or 1 > biggest:
        return []
    else:
        with_biggest = partition_options(total - biggest, biggest)
        without_biggest = partition_options(total, biggest - 1)

        with_biggest = [[biggest] + sub_options for sub_options in with_biggest]
        
        return with_biggest + without_biggest
    

# (b)
"""
Return the minimum number of elements from the list that need to be summed in order to add up to T.
The same element can be used multiple times in the sum. For example, for T = 11 and lst = [5, 4, 1] we should return 3 because at minimum we need to add 3 numbers together (5, 5, and 1). You can assume that there always exists a linear combination of the elements in lst that equals T.
"""
def min_elements(T, lst):
    """
    >>> min_elements(10, [4, 2, 1]) # 4 + 4 + 2
    3
    >>> min_elements(12, [9, 4, 1]) # 4 + 4 + 4
    3
    >>> min_elements(0, [1, 2, 3])
    0
    """
    # 如果目标值 T 等于 0，则不需要添加任何元素
    if T == 0:
        return 0
    # 如果目标值 T 小于 0 或列表为空，返回无穷大表示不可行
    if T < 0 or not lst:
        return float('inf')
    
    # 递归计算包含当前元素和不包含当前元素两种情况下的最小元素数量
    with_current = 1 + min_elements(T - lst[0], lst)
    without_current = min_elements(T, lst[1:])
    
    # 返回两种情况下的最小值
    return min(with_current, without_current)


##########################################
# Discussion 06 Nonlocal, Midterm Review #
##########################################

# 1.2
"""
Write a function that takes in a number n and returns a one-argument function.
The returned function takes in a function that is used to update n. It should return
the updated n.
"""
def memory(n):
    """
    >>> f = memory(10)
    >>> f(lambda x: x * 2)
    20
    >>> f(lambda x: x - 7)
    13
    >>> f(lambda x: x > 5)
    True
    """

    def memoried(func):
        nonlocal n
        n = func(n)
        return n
    return memoried


# 2.2
"""
Write a function that takes in no arguments and returns two functions, prepend and
get, which represent the “add to front of list” and “get the ith item” operations,
respectively. Do not use any python built-in data structures like lists or dictionaries.
You do not necessarily need to use all the lines.
"""
def nonlocalist():
    """
    >>> prepend, get = nonlocalist()
    >>> prepend(2)
    >>> prepend(3)
    >>> prepend(4)
    >>> get(0)
    4
    >>> get(1)
    3
    >>> get(2)
    2
    >>> prepend(8)
    >>> get(2)
    3
    """
    pass
    # get = lambda x: "Index out of range!"
    # def prepend(value):
    #     nonlocal 
    #     f = get(0)
    #     def get(i):
    #         if i == 0:
    #             return value
    #         return f(i - 1)
        
    # return prepend, get


# 2.4
"""
Implement the memory function, which takes a number x and a singleargument function f. It returns a function with a peculiar behavior that you must discover from the doctests. You may only use names and call expressions in your solution. You may not write numbers or use features of Python not yet covered in the course.
"""
square = lambda x: x * x
double = lambda x: 2 * x
def memory(x, f):
    """
    Return a higher-order function that prints its
    memories.

    >>> f = memory(3, lambda x: x)
    >>> f = f(square)
    3
    >>> f = f(double)
    9
    >>> f = f(print)
    6
    >>> f = f(square)
    3
    None
    """
    # def g(h):
    #     print(x)
    #     return memory(h(x), f)
    # return g

    def memoize(g, prev_result=None):
        print(prev_result if prev_result is not None else x)
        return memory(x, g)

    return lambda g: memoize(g, prev_result=f(x)) if f else lambda g: memoize(g)


# 2.5
"""
It’s Hog again! Write a commentary function announce losses that takes in a player who and returns a commentary function that announces whenever that player loses points.
"""
def announce_losses(who, last_score=0):
    """
    >>> f = announce_losses(0)
    >>> f1 = f(10, 0)
    >>> f2 = f1(1, 10) # Player 0 loses points due to swine swap
    Oh no! Player 0 just lost 9 point(s).
    >>> f3 = f2(7, 10)
    >>> f4 = f3(7, 11) # Should not announce when player 0's score does not change
    >>> f5 = f4(11, 12)
    """
    assert who == 0 or who == 1, 'The who argument should indicate a player.'
    def say(score0, score1):
        if who == 0:
            score = score0
        elif who == 1:
            score = score1
        if score < last_score:
            print('Oh no! Player', who, 'just lost', last_score - score, 'point(s).')
        return announce_losses(who, score)
    return say


# 2.6 
"""
The CS 61A staff has developed a formula for determining what a fox
might say. Given three strings—a start, a middle, and an end—a fox will say the start string, followed by the middle string repeated a number of times, followed by the end string. These parts are all separated by single hyphens.

Complete the definition of fox says, which takes the three string parts of the fox’s statement (start, middle, and end) and a positive integer num indicating how many times to repeat middle. It returns a string. You cannot use any for or while statements. Use recursion in repeat. Moreover, you cannot use string operations other than the + operator to concatenate strings together.
"""
def fox_says(start, middle, end, num):
    """
    >>> fox_says('wa', 'pa', 'pow', 3)
    'wa-pa-pa-pa-pow'
    >>> fox_says('fraka', 'kaka', 'kow', 4)
    'fraka-kaka-kaka-kaka-kaka-kow'
    """
    def repeat(k):
        if k == 1:
            return middle
        else:
            return middle + '-' + repeat(k-1)
        
    return start + '-' + repeat(num) + '-' + end


# 2.7
"""
The study of stress is still an open field of inquiry in linguistics—why do we say “alaBAma,” but “aLAbama” and “alabaMA” make us cringe? Or how did it come to be that “AMERICAN history professor” and “american HISTORY professor” mean two different things? One model that we use to understand stress actually employs the tree data structure!

############
# Diagrams #
############

In the above diagrams, every node has a “strong” child and a “weak” child, and primary stress is placed on the leaf that has the greatest number of strong parents. In the spirit of computational linguistics, let’s write a function that, given one of these tree structures, identifies the stressed part of a word or phrase.
"""
def primary_stress(t):
    """
    >>> word = tree("", [tree("w", [tree("s", [tree("min")]), tree("w", [tree("ne")])]),tree("s", [tree("s", [tree("so")]), tree("w", [tree("ta")])])])
    >>> primary_stress(word)
    'so'
    >>> phrase = tree("", [tree("s", [tree("s", [tree("law")]), tree("w", [tree("degree")])]),tree("w", [tree("requirement")])])
    >>> primary_stress(phrase)
    'law'
    """
    def helper(t, num_s):
        if is_leaf(t):
            return [label(t), num_s]
        if label(t) == "s":
            num_s = num_s + 1
        return max([helper(b, num_s) for b in branches(t)],
            key = lambda x: x[1])
    return helper(t, 0)[0]


# 2.8
"""
Consider the subset sum problem: you are given a list of integers and a number k.
Is there a subset of the list that adds up to k?
"""
def subset_sum(seq, k):
    """
    >>> subset_sum([2, 4, 7, 3], 5) # 2 + 3 = 5
    True
    >>> subset_sum([1, 9, 5, 7, 3], 2)
    False
    >>> subset_sum([1, 1, 5, -1], 3)
    False
    """
    seq = sorted(seq)
    if k == 0:
        return True
    elif seq[0] > k:
        return False
    else:
        return subset_sum(seq[1:], k - seq[0])