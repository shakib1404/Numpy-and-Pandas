import numpy as np

arr=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
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
print(arr[0])
print(b[1,0])
print(arr[:3])
print(arr[1:3])
print(arr[5:])
print(arr[-3:])
print(arr[-7:-5])
print(arr[::2])
print(arr[1:8:2])
print(b[1,2:4])
print(b[1:3,2:4])
print(arr.dtype)
arra=np.array([1.1,3.1,5,6])
new_arr=arra.astype('i')
print(new_arr)

x=arr.copy()
print(x)
y=arr.view()
arr[0]=31
print(y)
print(b.shape)
newarr=arr.reshape(3,4)
print(newarr)
new=arr.reshape(2,3,2)
print(new)
newa=arr.reshape(2,2,-1)



for x in arr:
    print(x)

arr1 = np.array([[1, 2,3],[4,5,6]])

arr2 = np.array([[4, 5,6],[7,8,9]])

arr3 = np.concatenate((arr1, arr2),axis=0)

print(arr3)    
nw=np.array_split(arr,6)
print(nw)
print(nw[0])
print(nw[1])
print(nw[2])
arr4 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])

newarr4 = np.array_split(arr4, 3, axis=1)
print(newarr4)