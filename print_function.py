if __name__ == '__main__':
    n = int(input())
    print(*range(1, n+1), sep="") # * allows you to send arrays through a function. U also can use end = '' inside the print function to avoid the break line