if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    numbers = [x for x in arr]
    numbers.sort(reverse = True)
    for x in numbers:
        if x < numbers[0]:
            print(x)
            break
