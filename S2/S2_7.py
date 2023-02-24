# S2_7 BMI计算
# 张起硕-2125060196
# 2023/02/24

height = float(eval(input('请输入身高（米）:')))
bmi = float(eval(input('请输入体重（千克）:'))) / (height * height)
print('BMI:%.1f ' % bmi, end='')
if bmi < 18.5:
    print('过轻')
elif bmi < 23.9:
    print('正常')
elif bmi < 27:
    print('过重')
elif bmi < 32:
    print('肥胖')
else:
    print('非常肥胖')
