import numpy as np

arr=np.array([1,2,4,5,6])
a=np.array(34)
b=np.array([[1,4,5,6],[4,5,6,9]])
c=np.array([[[1,4,5,6],[4,5,6,8],[7,8,9,8]]])
print(arr)
print(np.__version__)
print(type(arr))
print(a.ndim)
print(arr.ndim)
print(b.ndim)
print(c.ndim)
arr_=np.array([1,2,3,4],ndmin=5)
print(arr_)
print('number of dimensions:', arr_.ndim)


