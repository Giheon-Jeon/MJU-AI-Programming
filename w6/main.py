import numpy as np

a = np.ones((2, 2, 3, 4))
b = np.arange(12).reshape(3, 4)

result = a + b

print(result)
print("Shape A:", a.shape)            # (2, 2, 3, 4)
print("Shape B:", b.shape)            # (3, 4)
print("Result Shape:", result.shape)  # (2, 2, 3, 4)