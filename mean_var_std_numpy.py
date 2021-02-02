import numpy
array_input = []

N, M = map(int, input().split())
for x in range(1, N+1):
    array_input.append(input().split())
print(numpy.mean(numpy.array(array_input, int), axis = 1))
print(numpy.var(numpy.array(array_input, int), axis = 0))
print(numpy.around((numpy.std(numpy.array(array_input, int))),decimals=11))