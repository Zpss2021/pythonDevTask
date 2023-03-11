# S3_3 函数-平均值
# 张起硕-2125060196
# 2023/03/10

def calculate(*nums):
    aver, ret = 0, [0]
    for n in nums:
        ret[0] += n
    ret[0] /= len(nums)
    for n in nums:
        if n > ret[0]:
            ret.append(n)
    return tuple(ret)


arr = []
while True:
    tmp = input('请输入数字，输入q结束:')
    if tmp.isdigit():
        arr.append(eval(tmp))
    elif tmp == 'q':
        result = calculate(*arr)
        print('平均值为{0}, 大于平均值的所有数为：{1}'.format(result[0], result[1:]))
        break
    else:
        print('输入错误，请重新输入！')
        continue
