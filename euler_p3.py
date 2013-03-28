# euler_p3.py
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math

def main():
    bignum = 600851475143
    maxout = int(math.sqrt(bignum) + 1)
    # this was way, waaay simpler than I initially made it:
    for i in range(maxout, 2, -2):
        if bignum % i == 0 and is_prime(i):
            print("Max prime is %s" % i)
            break

def is_prime(num):
    maxtest = int(num**0.5+ 1)
    for denominator in range(2, maxtest):
        if num / denominator == int(num / denominator):
            return False
    return True

if __name__ == '__main__': main()


