import numpy
array_input = []

N, M = map(int, input().split())
for x in range(1, N+1):
    array_input.append(input().split())
print(numpy.prod(numpy.sum(numpy.array(array_input, int), axis = 0)))
