# CS61A Summer 2020 Lecture 6: Recursion
# Inverse Cascade
from projects.ants.ucb import trace, main, interact
from operator import add, sub, mul, truediv


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






"""An interpreter for the Scheme-Syntax Calculator Language

An interpreter for a calculator language that uses prefix-order Operator expressions must be operator symbols. Operand express separated by spaces."""

class Pair:
    """A Pair has two instance attributes: first and sceond
    
    For a pair to be a well-formed list, second is either a well-formed list or nil. Some methods only apply to well-formed lists."""

    def __init__(self, first, second):
        self.first = first
        self.second = second
    
    
def reduce(fn, scheme_list, start):
    if scheme_list is nil:
        return start
    return reduce(fn, scheme_list.second, fn(start, scheme_list.first))

def as_scheme_list(*args):
    if len(args) == 0:
        return nil 
    return Pair(args[0, as_scheme_list(*args[1:])])


def calc_eval(exp):
    if type(exp) in (int, float):
        return exp
    elif isinstance(exp, Pair):
        arguments = exp.second.map(calc_eval)
        return calc_apply(exp.first, arguments)
    else:
        raise TypeError(str(exp) + ' is not a number or call expression')
    

def calc_apply(operator, args):
    if not isinstance(operator, str):
        raise TypeError(str(operator) + ' is not a symbol')
    if operator == '+':
        return reduce(add, args, 0)
    elif operator == '-':
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 argument')
        elif len(args) == 1:
            return -args.first
        else:
            return reduce(sub, args, 0)
    elif operator == '*':
        return reduce(mul, args, 1)
    elif operator == '/':
        if len(args) == 0:
            raise TypeError(operator + 'requires at least 1 ')
        elif len(args) == 1:
            return 1 / args.first
        else:
            return reduce(truediv)
    else:
        return TypeError(operator + ' is a unknown operator')
    
