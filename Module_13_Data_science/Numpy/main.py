# python.exe -m pip install --upgrade pip
# pip install numpy
import numpy as np
# print(np.__version__)

from timeit import default_timer as timer


l1 = [1,2,3]
l2 = [4,5,6]
# a = np.array([1,2,3])
a1 = np.array(l1)
a2 = np.array(l2)

# dot product
dot = np.dot(a1,a2)
print(dot)

sum1 = a1 * a2
# dot = np.sum(sum1)
dot = (a1 * a2).sum()
print(dot)

dot = a1 @ a2
print(dot)

dot = 0
for i in range(len(l1)):
	dot += l1[i] * l2[i]
print(dot)





# l = [1,2,3]
# a = np.array([1,2,3])

# a = np.sqrt(a)
# a = np.log(a)
# print(a)


# l = l * 2
# print(l)
# a = a * np.array([4])
# a = a * 2
# print(a)

# l = l + [4]
# l.append(4)
# print(l)
# a = a + np.array([4])
# a = a + np.array([4,4,4])
# a.append(4)
# print(a)





# a = np.array([1,2,3])
# print(a)
# print(a.shape)
# print(a.dtype)
# print(a.ndim)
# print(a.size)
# print(a.itemsize)

# print(a[0])
# a[0] = 10
# print(a)

# b = a * np.array([2,0,2])
# print(b)