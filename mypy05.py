score = int(input("请输入0-100的分数："))
grade = ""

if score < 0 or score > 100:
    score = int(input("输入错误！请重新输入0-100的分数："))
else:
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "E"

print("分数为{0}，成绩为{1}".format(score, grade))

score = int(input("请输入0-100的分数："))
degree = "ABCDE"
num = 0
if score < 0 or score > 100:
    score = int(input("输入错误！请重新输入0-100的分数："))
else:
    num = score // 10
    if num < 6:
        num = 5

print("分数为{0}，成绩为{1}".format(score, degree[9 - num]))
