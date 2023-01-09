def average(array):
    # your code goes here
    sarr = set(array)
    s=0
    for i in sarr:
        s = s + i
    avg = s / len(sarr)
    return avg

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
