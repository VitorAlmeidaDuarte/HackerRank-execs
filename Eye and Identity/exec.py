import numpy
numpy.set_printoptions(legacy='1.13')

array_size = list(input().split())

print(numpy.eye(int(array_size[0]), int(array_size[1]), k=0))
