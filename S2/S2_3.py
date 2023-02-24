# S2_3 银行金额大写汉字转换
# 张起硕-2125060196
# 2023/02/24

num, arr = input('输入金额：'), []
ch = ['零', '壹', '贰', '叁', '肆', '伍', '陆', '柒', '捌', '玖']
unit = ['', '拾', '佰', '仟', '萬']
for i in num:
    arr.append(eval(i))
out, j = [], 0
while j < len(arr):
    if j == 0 or not (arr[j - 1] == 0 and arr[j] == 0):
        out.append(ch[arr[j]])
    if arr[j] != 0:
        out.append(unit[len(arr) - j - 1])
    j += 1
if out[-1] == ch[0]:
    out.pop(-1)
print('汉字转换:', *out, '圆整', sep='')
