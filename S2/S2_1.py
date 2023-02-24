# S2_1 用户登录
# 张起硕-2125060196
# 2023/02/24

username = 'admin'
password = '123'

for i in range(3):
    input_name = input('请输入用户名：')
    input_pwd = input('请输入密码：')
    if input_name == username and input_pwd == password:
        print("欢迎%s" % username)
        break
    else:
        print("录入错误，你还有%d次机会！" % (2 - i))
else:
    print('登录超限，请明天再来！')
    exit(-1)
