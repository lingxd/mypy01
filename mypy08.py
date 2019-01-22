name =input('请告诉我你的名字好吗？')
print('好的我叫', name)

#开始扯淡
s = input('你的身高呢？cm')
t = input('体重呢兄弟？ kg')
S = float(s)
T = float(t)
bmi = T/(S*2)
print('你的bmi是:', bmi)
if bmi < 18.5 :
    print('有点低啊')
elif bmi >=18.5 and bmi<=25:
    print('正常')
elif bmi >=25 and bmi <=32 :
    print('废了')
#
a = input('说个数，兄弟：')
a = int(a)+1
if a>5 :
    print(a, 'da a')
else:
    print(a, 'xiao a')