

# Vectors
x = [-1.1, 0.0, 3.6, -7.2]
print(len(x))


# Concatenate Vectors
import numpy as np
x = np.array([1, -2])
y = np.array([1, 1, 0])
z = np.concatenate((x, y))
print(z)

# Vector of first differences
x = np.array([1,8,3,2,1,9,7])
d = x[1:] - x[:-1]
print(d)

# Create Zero vector
np.zeros(3)

# Unit Vectors
i, n = 2, 4
x = np.zeros(n)
x[i] = 1
print(x)

# Ones Vector
np.ones(3)

# Random Vectors
np.random.random(2)

# Plotting
import matplotlib.pyplot as plt
#plt.ion()

temps = [71, 71, 68, 69, 69, 68, 74, 77, 82, 85, 86, 88, 86,
         85, 86, 84, 79, 77, 75, 73, 71, 70, 70, 69, 69, 69, 69, 67,
         68, 68, 73, 76, 77, 82, 84, 84, 81, 80, 78, 79, 78, 73, 72,
         70, 70, 68, 67]

#plt.plot(temps, '-bo')
#plt.savefig('temperature.pdf', format='pdf')



# Vector Addition
x = np.array([1,2,3])
y = np.array([100, 200, 300])
print('Sum of arrays: x= ',x,'and y= ',y,'is: ', x+y)

# Scalar Vector Multiplication
print(2.2*x)

# Scalar-Vector addition
print(x + 2)

# Elementwise Operation
p_initial = np.array([22.15, 89.32, 56.77])
p_final = np.array([23.05, 87.32, 53.13])
r = (p_final - p_initial) / p_initial
print(r)

#Linear Combination
def lincomb(coef, vectors):
    n = len(vectors[0])
    comb = np.zeros(n)
    for i in range(len(vectors)):
        comb = comb + coef[i] * vectors[i]
    return comb

a = np.array([1,2])
b = np.array([3,4])
alpha = -0.5
beta = 1.5
c = alpha*a + beta*b
print(c)
print(lincomb([alpha, beta], [a,b]))

def lincomb(coef, vectors):
    return sum(coef[i]*vectors[i] for i in range(len(vectors)))



# Inner Product
x = np.array([-1, 2, 2])
y = np.array([1, 0, -3])
print(np.inner(x,y))

# Alternatively
print(x@y)

# Sparse Vectors
from scipy import sparse
I = np.array([4,7,8,9])
J = np.array([0,0,0,0])
V = np.array([100, 200, 300, 400])
A = sparse.coo_matrix((V, (I,J)), shape=(10000,1))
A









