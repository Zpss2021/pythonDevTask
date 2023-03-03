# S3_3 字符串操作-格式化输出
# 张起硕-2125060196
# 2023/03/03

stu_name = "张三"
stu_num = 1101
stu_aver = 90.6497
stu_list = [stu_name, stu_num, stu_aver]
stu_dict = {
    "name": stu_name,
    "num": stu_num,
    "aver": stu_aver
}

print("姓名：{0}，学号：{1}, {0}的平均分为{2:.2f}分".format(stu_name, stu_num, stu_aver))
print("姓名：{name}，学号：{num}, {name}的平均分为{aver:.2f}分".format(name=stu_name, num=stu_num, aver=stu_aver))
print("姓名：{0}，学号：{1}, {0}的平均分为{2:.2f}分".format(*stu_list))
print("姓名：{name}，学号：{num}, {name}的平均分为{aver:.2f}分".format(**stu_dict))
