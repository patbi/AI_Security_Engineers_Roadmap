# python.exe -m pip install --upgrade pip
# pip install numpy
import numpy as np
# print(np.__version__)

# from timeit import default_timer as timer

# a = np.array([10,19,30,41,50,61])



a = np.array([[1,2], [3,4], [5,6]])
print(a)

# bool_idx = a > 2
# print(bool_idx)
# print(a[bool_idx])
print(a[a > 2])

b = np.where(a>2, a, -1)
print(b)

# a = np.array([[1,2,3,4], [5,6,7,8]])
# print(a)

# b = a[0,1]
# b = a[0,:]
# b = a[0,1:3]
# b = a[:,1]
# b = a[-1,-1]
# b = a[-1,-2]
# print(b)


# a = np.array([[1,2], [3,4]])
# a = np.array([[1,2,6], [3,4,8]])
# a = np.array([[1,2], [3,4]])
# print(a)
# print(a.shape)

# print(a[0])
# print(a[0][0])
# print(a[0,0])
# print(a[:,0])
# print(a[0,:])
# print(a.T)
# print(np.linalg.inv(a))
# print(np.linalg.det(a))
# print(np.diag(a))
# c = np.diag(a)
# print(np.diag(c))
# print(a[1,2])
# print(a[1][2])




# a = np.random.randn(1000)
# b = np.random.randn(1000)

# A = list(a)
# B = list(b)

# T = 1000

# def dot1():
# 	dot = 0
# 	for i in range(len(A)):
# 		dot += A[i]*B[i]
# 	return dot

# def dot2():
# 	return np.dot(a,b)

# start = timer()
# for t in range(T):
# 	dot1()
# end = timer()
# t1 = end-start

# start = timer()
# for t in range(T):
# 	dot2()
# end = timer()
# t2 = end-start

# print('list calculation', t1)
# print('np.dot', t2)
# print('ratio', t1/t2)


# l1 = [1,2,3]
# l2 = [4,5,6]
# a = np.array([1,2,3])
# a1 = np.array(l1)
# a2 = np.array(l2)

# dot product
# dot = np.dot(a1,a2)
# print(dot)

# sum1 = a1 * a2
# dot = np.sum(sum1)
# dot = (a1 * a2).sum()
# print(dot)

# dot = a1 @ a2
# print(dot)

# dot = 0
# for i in range(len(l1)):
# 	dot += l1[i] * l2[i]
# print(dot)





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