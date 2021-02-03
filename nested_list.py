if __name__ == '__main__':
    data = {}
    for _ in range(int(input())):
        name = input()
        score = float(input())
        data[name] = score
    
    data = sorted(data.items(), key = lambda x: x[1])
    data = [x for x in data if x[1] != data[0][1]]
    data = [x[0] for x in data if x[1] == data[0][1]]
    data.sort()
    print(*(x for x in data), sep="\n")
    