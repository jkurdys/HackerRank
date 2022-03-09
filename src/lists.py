import sys

if __name__ == '__main__':
    N = int(input())
    for i in map(str.rstrip, sys.stdin):
        txt = i.split()
        print(txt)
        