s = input("请输入一个数字s=")

if int(s) < 10:
    print("s小于10")
else:
    print("s大于等于10")

# 条件三元运算符
# 条件为真的值  if 【条件】 else 条件为假的值

a = input("请输入一个数字a=")
print(a if int(a) <= 10 else "a值大于10")
