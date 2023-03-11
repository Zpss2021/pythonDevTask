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


print(calculate(1, 2, 3, 4, 5, 6, 7))
