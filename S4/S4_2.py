# S3_3 函数-字符统计
# 张起硕-2125060196
# 2023/03/10

def char_statistic(dest_str):
    ret = [0, 0]
    for c in dest_str:
        if str(c).isupper():
            ret[0] += 1
        if str(c).islower():
            ret[1] += 1
    return tuple(ret)


print(char_statistic('ehllo WROLD'))
