import numpy as np
# 1
myList = [1,2,3,4,5,6,7,8]
print(myList)
arr = np.array(myList)
print(arr)
print(type(myList))
print(type(arr))

# 2
arr = np.arange(31,37)
print(arr)
arr = np.arange(80,90,2)
print(arr)

# 3
arr = np.zeros((5,5))
print(arr)
arr = np.zeros((1,5))
print(arr)
arr = np.ones((2,10))
print(arr)

# 4
num = np.random.randint(30,70)
print(num)
num = np.random.randint(30,70)
print(num)
num = np.random.randint(30,70)
print(num)
arr = np.random.randint(20,30,(5,5))
print(arr)

# 4
arr = np.linspace(0,10,4)
print(arr)
arr = np.linspace(0,10,100)
print(arr)

# 5
np.random.seed(101)
arr = np.random.randint(0,100,10)
print(arr)
arr = np.random.randint(0,100,10)
print(arr)

# 6
arr = np.random.randint(0,100,10)
print(arr)
print(arr.max())
print(arr.argmax())
print(arr.min())
print(arr.argmin())
print(arr.mean())

# 7
arr = arr.reshape(2,5)
print(arr)
arr = arr.reshape(5,2)
print(arr)

# 8
arr = np.arange(0,100).reshape(10,10)
print(arr)
print(arr[5][2])
print(arr[:,2])             # Bring back the entire 2nd column
print(arr[3,:])             # Bring back the entire 3rd row

#9  Masking
print(arr>30)
arr = arr[arr>30]
print(arr)