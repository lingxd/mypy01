score = int(input("请输入你的分数："))
if score < 60:
    grade = "不及格"
elif score < 80:
    grade = "及格"
elif score < 90:
    grade = "良好"
elif score < 100:
    grade = "优秀"
else:
    grade = "不合理"

print("分数是{0}，成绩是{1}".format(score, grade))

x = int(input("X="))
y = int(input("Y="))
if x == 0 and y == 0:
    position = "原点"
elif x == 0:
    position = "X轴"
elif y == 0:
    position = "Y轴"
elif x > 0 and y > 0:
    position = "第一象限"
elif x > 0 and y < 0:
    position = "第二象限"
elif x < 0 and y < 0:
    position = "第三象限"
elif x < 0 and y > 0:
    position = "第四象限"

print("坐标（{0}，{1}），位置在坐标轴{2}".format(x, y, position))
