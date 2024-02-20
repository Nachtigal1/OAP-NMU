import numpy as np


def modify_array(arr1):
    average = np.mean(arr1)
    arr2 = arr1 - average
    arr2_sorted = np.sort(arr2)
    return arr2_sorted, average


arr1 = np.array([12, 45, 23, 67, 34, 98, 54, 21, 33, 77, 89, 10, 5, 42, 30])

modified_arr2, average = modify_array(arr1)

print("Заданий масив:", arr1)
print("Середнє значення:", average)
print("Новий масив:", modified_arr2)
