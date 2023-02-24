# S2_4 输出九九乘法表
# 张起硕-2125060196
# 2023/02/24

i, j = 1, 1
while i <= 9:
    j = 1
    while j <= i:
        print('%d * %d = %2d ' % (i, j, i * j), end='')
        j += 1
    print()
    i += 1
