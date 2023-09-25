# CS61A Summer 2020 Lecture 6: Recursion
# Inverse Cascade

def inverse_cascade(n):
    """
    Write a function that prints an inverse cascade.

    >>> inverse_cascade(1234)
    1
    12
    123
    1234
    123
    12
    1
    """
    grow(n)
    print(n)
    shrink(n)

def f_then_g(f, g, n):
    if n:
        f(n)
        g(n)

grow = lambda n: f_then_g(grow, print, n // 10)
shrink = lambda n: f_then_g(print, shrink, n // 10)


# Lecture 10: Trees
# How to construct a tree
def tree(label, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be trees!'
    return [label] + list(branches)

def label(tree):
    return tree[0]

def branches(tree):
    return tree[1:]

def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    return not branches(tree)

def count_leaves(t):
    """Count the leaves of a tree"""
    if is_leaf(t):
        return 1
    else:
        return sum([count_leaves(b) for b in branches(t)])
    
def leaves(tree):
    """
    Return a list containing the leaf labels of tree.
    
    >>> leaves(fib_tree(5))
    [1, 0, 1, 0, 1, 1, 0, 1]
    """
    if is_leaf(tree):
        return list(label(tree))
    else:
        return sum([leaves(b) for b in branches(tree)], [])

# A Fibonacci tree
def fib_tree(n):
    if n <= 1:
        return tree(n)
    else:
        left, right = fib_tree(n - 2), fib_tree(n - 1)
    return tree(label(left) + label(right), [left, right])

def increment_leaves(t):
    """Return a tree like t but with leaf labels incremented."""
    if is_leaf(t):
        return tree(label(t) + 1)
    else:
        return tree(label(t), [increment_leaves(b) for b in branches(t)])
    
def increment(t):
    """Return a tree like t but with all labels incremented."""
    return tree(label(t) + 1, [increment_leaves(b) for b in branches(t)])

# Print the tree
def print_tree(t, indent=0):
    print(' ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)