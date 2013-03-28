# euler_p6.py
"""
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first
ten natural numbers and the square of the sum is 3025  385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.
"""
def main():
    squares = list(map(square, range(1, 101)))
    sum_sq = sum(squares)
    sums = sum(range(1,101))
    sq_sum = sums**2
    return sq_sum - sum_sq


def square(x):
    return x**2

if __name__ == '__main__': main()
