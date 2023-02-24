# S2_5 百钱百鸡问题求解
# 张起硕-2125060196
# 2023/02/24

dad, mom, son, count = 0, 0, 0, 0
for dad in range(101):
    for mom in range(101):
        for son in range(101):
            if dad + mom + son == 100:
                if dad * 15 + mom * 9 + son == 300:
                    print('公鸡%d只，母鸡%d只，小鸡%d只' % (dad, mom, son))
                    count += 1
print('共有%d组解！' % count)
