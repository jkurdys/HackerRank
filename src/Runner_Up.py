def runner_up(arr):
    print(list(set(arr))[-2])

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up(arr)