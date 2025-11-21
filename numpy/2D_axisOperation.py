import numpy as np

arr = np.array([[1, 2, 3],
                [4, 5, 6]])

print("sum axis 0:", np.sum(arr, axis=0))
print("sum axis 1:", np.sum(arr, axis=1))

print("cumsum axis 0:\n", np.cumsum(arr, axis=0))
print("cumsum axis 1:\n", np.cumsum(arr, axis=1))

print("max axis 0:", np.max(arr, axis=0))
print("max axis 1:", np.max(arr, axis=1))

print("min axis 0:", np.min(arr, axis=0))
print("min axis 1:", np.min(arr, axis=1))
