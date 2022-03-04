'''
Concatenate
Two or more arrays can be concatenated together
using the concatenate function with a tuple of
the arrays to be joinedIf an array has more
than one dimension, it is possible to specify
the axis along which multiple arrays are
concatenated. By default, it is along the first
dimension.

Task
You are given two integer arrays of size
N X P and M X P (N & M are rows,and P is the
column). Your task is to concatenate the arrays
along axis 0.

Input Format

The first line contains space separated integers
N, M and P.
The next N lines contains the space separated
elements of the P columns.
After that, the next M lines contains the space
separated elements of the P columns.

Output FormatPrint the concatenated array of size
(N + M) X P.
'''

import numpy as np

n, m, p = map(int,input().split())

arrN = np.array([input().split() for _ in range(n)],int)
arrM = np.array([input().split() for _ in range(m)],int)

nmp = np.concatenate((arrN, arrM))
print(nmp)