def modify_array(arr1):

    average = sum(arr1) / len(arr1)

    arr2 = [x - average for x in arr1]

    arr2.sort()

    return arr2, average


arr1 = [12, 45, 23, 67, 34, 98, 54, 21, 33, 77, 89, 10, 5, 42, 30]

modified_arr2, average = modify_array(arr1)

print("Заданий масив:", arr1)
print("Середнє значення:", average)
print("Новий масив:", modified_arr2)
