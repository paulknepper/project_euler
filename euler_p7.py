# euler_p7.py
"""
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6th prime is 13.

What is the 10 001st prime number?
"""
from euler_p3 import is_prime

def main():
    prime_ct = 0
    testnum = 1
    while prime_ct < 10001:
        testnum += 1
        if is_prime(testnum): prime_ct += 1
    print(testnum)

if __name__ == '__main__': main()
