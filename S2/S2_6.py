# S2_6 回文素数求解
# 张起硕-2125060196
# 2023/02/24

for n in range(2, 1001):
    arr = []
    for x in str(n):
        arr.append(eval(x))
    rev_arr = arr[::-1]
    if arr == rev_arr:
        for i in range(2, n):
            if n % i == 0:
                break
        else:
            print(n, end=' ')
