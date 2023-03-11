# S3_3 函数-数字加密
# 张起硕-2125060196
# 2023/03/11

def encrypt(origin_text, refer_list):
    cipher = ''
    for c in origin_text:
        if str(c).isnumeric():
            cipher += refer_list[int(c)]
        else:
            cipher += c
    return cipher


refer = ('O', 'I', 'Z', 'E', 'Y', 'S', 'G', 'L', 'B', 'P')
origin = input('请输入原文：')

print('密文：', encrypt(origin, refer))
