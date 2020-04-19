import numpy as np

a = [[1.1, 0.1, 0.1, 5]]
a = np.array(a )
print(a.shape)
print(a)
print(np.dot(a, np.log(a).T))
print(np.sum(a*np.log(a)))
# print(np.sum(a*np.log(a) + (1-a)*np.log(1-a)))
print(1+a)
x = np.dot(a, np.log(a).T) + np.dot(1+a, np.log(1+a).T)
print(x)
x = np.squeeze(x)
print(x)
