# S1_7-n的阶乘
# 张起硕-2125060196-版权所有

i = n = eval(input('请输入非负整数n的值：'))
ans = 1
while i > 0:
    ans *= i
    i -= 1
print(n, '!=', ans)
