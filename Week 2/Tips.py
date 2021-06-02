import numpy as np

a = np.random.rand(5)  # don't use this . why ? this called "Rank 1 array " a.shape = (5,)


print(a)

print(a.shape)


print("rank 1 array a * a.T : ", np.dot(a, a.T))  # cause a was rank 1 array this will be just 1 number

a = np.random.rand(5, 1)  # use this , now this matrix 5 * 1

print(a)

print(np.dot(a, a.T))  # output Matrix 5 * 5


#  np.random.rand(5, 1) column vector
#  np.random.rand(1, 5)   row  vector
