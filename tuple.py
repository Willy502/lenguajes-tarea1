if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    my_array = []
    for x in integer_list:
        my_array.append(x)
    print(hash(tuple(my_array)))