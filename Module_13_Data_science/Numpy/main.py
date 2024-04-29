# python.exe -m pip install --upgrade pip
# pip install numpy
import numpy as np
# print(np.__version__)

# from timeit import default_timer as timer

a = np.array([[1,2], [3,4]])
eigenvalues, eigenvectors = np.linalg.eig(a)

print(eigenvalues)
print(eigenvectors) # column vector

# e_vec * e_val = A * e_vec
b = eigenvectors[:,0] * eigenvalues[0]
print(b)

c = eigenvectors[:,0] @ a
print(c)

d = a @ eigenvectors[:,0]
print(d)

print(b==c)
print(b==d)
print(np.allclose(b,d))

# a = np.random.random((3,2)) # 0-1
# print(a)

# b = np.random.randn(3,2)
# print(b)

# c = np.random.randn(1000) # normal/Gaussian
# print(c.mean(), c.var())

# d = np.random.randint(3,10,size=(3,3))
# print(d)

# e = np.random.choice(5, size=10)
# print(e)

# f = np.random.choice([-8,-7,-6], size=10)
# print(f)

# a = np.zeros((2,3))
# print(a)

# a = np.ones((2,3))
# print(a)

# a = np.full((2,3), 5.0)
# print(a)

# a = np.eye(3)
# print(a)

# a = np.arange(20)
# print(a)

# a = np.linspace(0,10,5)
# print(a)

# a = np.array([1,2,3])
# b = a
# b = a.copy()
# b[0] = 42
# print(b)
# print(a)


# x = np.array([1,2])
# x = np.array([1.0,2.0], dtype=np.float16)
# print(x)
# print(x.dtype)


# a = np.array([[7,8,9,10,11,12,13], [17,18,19,20,21,22,23]])
# print(a)
# print(a.sum(axis=None))
# print(a.sum(axis=1))
# print(a.mean(axis=1))
# print(a.mean(axis=0))
# print(a.mean(axis=None))
# print(a.var(axis=None))
# print(a.std(axis=None))
# print(np.std(a, axis=None))
# print(a.min(axis=None))
# print(np.max(a, axis=None))


# print(a.sum(axis=0))
# print(a.sum(axis=1))
# print(a.mean(axis=1))
# print(a.mean(axis=0))
# print(a.mean(axis=None))


# x = np.array([[1,2,3], [4,5,6], [1,2,3], [4,5,6]])
# a = np.array([1,0,1])
# y = x + a
# print(y)



# a = np.array([1,2,3,4])
# b = np.array([5,6,7,8])
# hstack, vstack
# c = np.hstack((a,b))
# c = np.vstack((a,b))
# print(c)




# a = np.array([[1,2], [3,4]])
# print(a)
# b = np.array([[5,6]])
# c = np.concatenate((a,b), axis=None)
# c = np.concatenate((a,b.T), axis=1)
# print(c)


# a = np.arange(1,7)
# print(a)
# print(a.shape)
# b = a.reshape((3,2))
# print(b)
# print(b.shape)
# u = a[np.newaxis, :]
# u = a[:, np.newaxis]
# print(u.shape)
# print(u)

# a = np.array([10,19,30,41,50,61])
# print(a)
# b = [1,3,5]
# print(a[b])
# even = np.argwhere(a%2==0).flatten()
# print(a[even])


# a = np.array([[1,2], [3,4], [5,6]])
# print(a)

# bool_idx = a > 2
# print(bool_idx)
# print(a[bool_idx])
# print(a[a > 2])

# b = np.where(a>2, a, -1)
# print(b)

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