def runner_up(arr):
    # print(list(set(arr))[-2])
    raw = list(set(arr))
    raw.pop(raw.index(max(raw)))
    return max(raw)
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    runner_up(arr)