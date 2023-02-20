# S1_8-冒泡排序
# 张起硕-2125060196-版权所有

arr = [23, 4, 6, 9, 2, 11, 20]
swapped = True
j = len(arr)
while swapped:
    swapped = False
    for i in range(1, j):
        if arr[i - 1] < arr[i]:
            arr[i - 1], arr[i] = arr[i], arr[i - 1]
            j = i
            swapped = True
print(arr)
