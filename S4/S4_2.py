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


obj_str = 'ehllo WROLD'
print('统计字符串{0}: 大写字母{1}个, 小写字母{2}个'.format(obj_str, *char_statistic(obj_str)))
