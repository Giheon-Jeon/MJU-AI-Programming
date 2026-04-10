import numpy as np

arr = np.array([
 [ 5, 10, 15, 20],
 [25, 30, 35, 40],
 [45, 50, 55, 60]
])

# 두 번째 열 출력
print(arr[:, 1])

# 20보다 큰 값들만 출력
mask = arr >= 20
print(arr[mask])

# 첫 두 행의 마지막 두 열만 잘라서 출력
print(arr[:2, -2:])