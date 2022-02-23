'''
Task
The provided code stub reads an integer, n, from STDIN.
For all non-negative integers i < n, print i**2.

Example
The list of non-negative integers that are less than n = 3 is [0, 1, 2].
Print the square of each number on a separate line.

'''

def print_lesser_squares(n):
    squares = [x for x in range(n)]
    for s in squares:
        print(s**2)
        

if __name__ == '__main__':
    n = int(input('Enter an integer from 1 to 20:'))
    print_lesser_squares(n)
