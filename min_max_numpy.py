import numpy
array_input = []

N, M = map(int, input().split())
for x in range(1, N+1):
    array_input.append(input().split())
print(numpy.max(numpy.min(numpy.array(array_input, int), axis = 1)))
