def average(array):
    data = set(array)
    total = 0
    for x in data: total += x
    return total/len(data)

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)