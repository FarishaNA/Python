import numpy as np

# 2D ARRAY (2x2)
arr2d = np.array([[1, 2],
                  [3, 4]])

print("2D Array:\n", arr2d, "\n")

print("arr2d[0:2, 0:1] =")
print(arr2d[0:2, 0:1], "\n")

print("arr2d[:, 1] =")
print(arr2d[:, 1], "\n")


# 3D ARRAY (2x2x2)
arr3d = np.array([
    [[1, 2],
     [3, 4]],

    [[5, 6],
     [7, 8]]
])

print("3D Array:\n", arr3d, "\n")

print("arr3d[0] =")
print(arr3d[0], "\n")

print("arr3d[:, 1, :] =")
print(arr3d[:, 1, :], "\n")

print("arr3d[:, :, 1] =")
print(arr3d[:, :, 1], "\n")
