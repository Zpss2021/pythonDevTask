# S2_2 斐波那契数列生成
# 张起硕-2125060196
# 2023/02/24

arr, i, limit = [1, 1], 0, eval(input('请输入生成到第几个数：'))
if limit <= 2:
    print('1 ' * limit)
else:
    while i < limit - 2:
        arr.append(arr[i] + arr[i + 1])
        i += 1
    print(*arr)
