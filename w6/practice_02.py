"""
reshape, broadcasting, dot

아래 작업을 순서대로 수행하시오
1. 0에서 11까지의 값을 3x4 배열로 reshape하고 출력
2. 각 열에 [100, 200, 300, 400]을 broadcasting으로 더하고 출력
3. x와 y의 내적을 계산하고 출력
"""
import numpy as np

arr = np.arange(12)

v = np.array([100, 200, 300, 400])
x = np.array([[1, 2, 3]])
y = np.array([[4, 5, 6]])

#조건 1
rst1 = arr.reshape(3,4)
print(rst1)

#조건 2
rst2 = rst1 + v
print(rst2)

#조건 3
rst3 = np.dot(x, y.T)
print(rst3)