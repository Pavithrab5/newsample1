import numpy as np
#lists working
'''
list_a=[1,2,3,4]
list_b=[5,6,7,8]
print(list_a * list_b)

numpy_a=np.array([1,2,7,4]) #1D array
numpy_b=np.array([5,6,7,8]) #size should be same, one float value is there it will convert all the list into floAT
print(numpy_a * numpy_b)

numpyBasic_array=np.array([1,'a',3,4.5,7,1])
print(numpyBasic_array.dtype)
print(numpyBasic_array.itemsize) #byte size like integer=4bytes(32),float=8bytes(64),strings=128bytes(u32)
print(numpyBasic_array.size) #no.of elements in the list


array_2D=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array_2D)

array_3D=np.array([[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]])
print(array_3D)
print("Dimensions:{}".format(array_3D.ndim))
print("shape:{}".format(array_3D.shape))
print("Array Dtype:{}".format(array_3D.dtype))

#                 0th index  1st index

array_x=np.array([[1,2,3],[4,5,6]])
print(array_x)
print(array_x.size)
print(array_x[1,2])#1st index (0,1,2) 2ndvalue =6
print(array_x[0,2])#0th index 2nd value
print(array_x[:,2])#0th & 1st index, value od 2 in both indicies
print(array_x[:,-3])#-3,-2-1
#step -start:end:stepsize
print(array_x[0,0:4:2])
print(array_x[1,1:4:1])
print(array_x[:,0:4:2])
#updating
array_x[0,2]=10
array_x[1,2]=10
array_x[:,1]=5
print(array_x)

#3d arrays
array_3d=np.array([[[1,2],[3,4]],[[4,1],[3,1]]])
print(array_3d)
#selcting a particular number in 3d array
print(array_3d[0,1,0])
print(array_3d[:,1,0])
#updating
#array_3d[:,1,:]=50
print(array_3d)
print(array_3d.shape)
#indexing
print(array_3d[:,0,:])
print(array_3d[:,1,:])

#common arrays
#zero's two's empty
#res=np.zeros(4)
#print(res)
#2d arrray

two_2d=np.zeros((2,3,3))
print(two_2d)
three_d=np.zeros(((2,3,3)))
print(three_d)

#print(np.zeros((3,3)))
four_d=np.zeros((2,3,3,2),dtype="int32")
print(four_d)
#four_d=np.zeros((2,4,3,4))#two 3d arrays(2) 4 arrays 3 rows and 2 col
#print(four_d)

full1=np.full((3,3),2)
print(full1)

#full is used to create 2x2 matrix using [1,2]
res1=(np.full((2,2),[1,2],dtype="int64"))
print(res1)
#full_like is used to replace the list with the given data
array_a=[1,2,3,4]
print(np.full_like(array_a,5))

#repeat
array_r=[[1,2,3],[4,5,6]]
array_repeat=np.repeat(array_r,2,axis=1)
print(array_repeat)
array_r=[[1,2,3],[4,5,6]]
array_repeat=np.repeat(array_r,2,axis=0)
print(array_repeat)

#updating 1,1 index =7 in a zero matrxi
array_zero=np.zeros((3,3),dtype="int32")
array_zero[1,1]=7
print(array_zero)

updated_array=np.zero((3,3),dtype="int32")
updated_array[1:-1:,1:-1] = array_zero
print(updated_array)

#copying arrays
#when we assign an array to anthoer array we are having same id's so that any changes in the array_x will refelct to array_y
array_x=np.array([1,2,3,4])
array_y=array_x
array_y[0]=7
print(array_x)
print(array_y)

#math operations
array_math=np.array([1,2,3])
print(array_math)
print("Declared array:{}".format(array_math))
print("Add 10 to array:{}".format(array_math+10))
print("sub 2 from array:{}".format(array_math-2))
print("Raise tp pow array:{}".format((array_math**2)))
print("multipy array by 5:{}".format(array_math*5))
print("divide by 2:{}".format(array_math/2))
 
array_a=np.zeros((2,3))
array_b=np.full((3,2),2)
print(array_a)
print(array_b)
print(np.matmul(array_b,array_a))
#day2
#n_a=[[1,1,1,1,1],[0,0,0,0,0]]

array_status=[[1,2,3],[4,5,-6]]
#print(array_status)
print(np.min(array_status)) #printd min value of whole array
print(np.min(array_status,axis=0))#prints col wise min elements
print(np.min(array_status,axis=1))#prints row wise min elements

#reshape
array_re=np.array([[1,2,3,7],[4,5,-6,4]])
print(array_re)
print(array_re.reshape((4,2)))
#stacking
a_v1=np.array([1,2,3])
a_v2=np.array([1,2,3])
a_v3=np.array([7,8,9])
print(np.array([a_v1,a_v2,a_v3]))
print(np.hstack([a_v1,a_v2,a_v3]))

#arange - array range
one_d=np.arange(6)
print(one_d)

two_d=np.arange(12).reshape(4,3)
print(two_d)
print(two_d.shape)
three_dim=np.arange(24).reshape(2,3,4)
print(three_dim)
print(three_dim.shape)
print(np.arange(5))

array_one=np.array([10,20,30,40])
array_two=np.arange(10,50,10)#[10,20,30,40]
print(array_two*array_two)
print(array_one@array_two)
print(array_one.dot(array_two))
print(array_two)
print(array_two-array_one)

#numpy array as alist
array_l=np.array([1,2,3,4,5,6,7,8,9,11,23,45,6,7])
#nump array can be indexed as list
print(array_l[[1,3,5,7,4]])
'''



'''
import numpy as np
data_from_text_file=np.genfromtxt('Numpy_Basics_Data.txt',delimiter=',')#firstly  it is in float type
#data_from_text_file=np.genfromtxt('Numpy_Basics_Data.txt',dtype='int32',delimiter=',') #int32 converts into float
#print(data_from_text_file)
#anthoer way to convert it into int using astype()
data_from_text_file=data_from_text_file.astype('int32')
#print(data_from_text_file)
#advance indexing
#print(data_from_text_file>10)
print(data_from_text_file[data_from_text_file>0])
#print(data_from_text_file)
print(data_from_text_file[data_from_text_file<0])

#fill values
fill_values=np.genfromtxt('Numpy_Basics_Data.txt',delimiter=',',dtype=np.int32)
print(fill_values)
fill_values=np.genfromtxt('Numpy_Basics_Data.txt',delimiter=',',dtype=np.int32,filling_values=100)
print(fill_values)


def numpy_function(x,y):
    return 10*x+y
b=np.fromfunction
'''




