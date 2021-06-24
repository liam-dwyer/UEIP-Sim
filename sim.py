import numpy as np
import math


A = 4093
B = 7
C = 56
D = 131071

Sum = np.zeros(10)



def Y_i_0(i):
    return (A*i + B)%D
def Y_j_0(j):
    return (A*j + B)%D
def Z_i_0(i):
    return Y_i(i)%C
def Z_j_0(j):
    return Y_j(j)%C


def Y_i(i,k):
    return (A * Y_i(i,k-1) + B) % D
def Y_j(j,k):
    return (A * Y_j(j,k-1) + B) % D
def Z_i(i,k):
    return Y_i(i,k)%C
def Z_j(j,k):
    return Y_j(j,k)%C

for i in range(2**16):
    for j in range(2**16):
        for k in range(10):
            if i == 0:
                Yi = Y_i_0(i)
                Yi_prev = Yi
            if j == 0:
                Yj = Y_j_0(j)
                Yj_prev = Yj
            else:
                Yi = (A * Yi_prev +B)%D
                Yk = (A * Yj_prev +B)%D
                if ((Yi%C) == (Yj%C)):
                    Sum[k] += 1
                    Yi_prev = Yi
                    Yj_prev = Yj
                else:
                    Yi_prev = Yi
                    Yj_prev = Yj
                    
    

#Now create the loops that call on these functions

print(Sum / (2**32))

