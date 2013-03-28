# euler_p4.py
"""
A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""
def main():
    highest = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            product = i * j
            if is_palindrome(product):
                highest = max([highest, i * j])
    return highest

def is_palindrome(num):
    if str(num) == str(num)[::-1]: return True
    
    
# this actually works, but there is easier way->string[::-1]
def str_rev(string): 
    if len(string) == 1: return string
    s = string[1:] 
    return str_rev(s) + string[0]

if __name__ == '__main__': main()
