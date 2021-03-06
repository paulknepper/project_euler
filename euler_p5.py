# euler_p5.py
"""
2520 is the smallest number that can be divided by each of the numbers from
1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the
numbers from 1 to 20?
"""
def main(): # takes too long
    testnum = 20
    numset = [11, 13, 14, 16, 17, 18, 19, 20]
    while True:
        for num in numset:
            if testnum % num != 0:
                break
            elif num == 20:
                print(testnum)
                return
        testnum += 1

if __name__ == '__main__': main()

