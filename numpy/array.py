#pip install NumPy
import numpy as np

x1 = np.random.randint(0,10, size = 5)
print(x1[-1]) #뒤에서부터 index(0)
print(x1[:3]) #처음 3개 요소 선택

#2차원 배열 만들기
x2 = np.array([range(i,i+5) for i in [1,11,21]])
print(x2[::-1]) #배열 뒤집기
print(x2[::-1,:-1]) #배열 뒤집기
x2[:2,:2] #2개의 행, 2개의 열 선택
x2c = x2[:2,:3].copy() #명시적으로  copy하기

x2r = np.random.random((3,3)) #난수 배열
x2n = np.random.normal(0,10,(3,3)) # 정규분포를 따르는 3x3 난수배열

x3 = np.random.randint(0,10, size = (3,4,5)) #정수 난수 배열
print(x3.ndim) #차원 갯수
print(x3.shape) #모양
print(x3.size) #전체 값의 갯수
print(x3.dtype) #타입

x = np.array([1,2,3])
y = x[::-1].copy()
conc = np.concatenate([x,y])
#out = array([1, 2, 3, 3, 2, 1])

x = [1,2,36,99,99,4,5,6]
x1,x2,x3  =  np.split(x, [3,5])

grid = np.arange(16).reshape((4,4))
print(grid)
