# euler_p2.py

"""
Each new term in the Fibonacci sequence is generated by adding the previous
two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed
four million, find the sum of the even-valued terms.
"""
def main():
    sums, num, ct = 0, 0, 0
    while num <= 4000000:
        num = fib2(ct)
        sums += num if num % 2 == 0 else 0
        ct += 1
    print(sums)
        

def fib(num): # takes too long to compute...
    a, b = 1, 2
    for i in range(num):
        a, b = b, a + b
    return a

def fib2(num): 
    if num < 1: return 1 # Make this num < 2 to get real fibo sequence
    else: # for loop pointless here because of use of return in loop;
          # probably true for a lot of recursive functions
        return fib2(num - 1) + fib2(num - 2)

if __name__ == '__main__': main()
        