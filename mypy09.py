# while语句练习

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)

# sorted([字符]) ： 排序
print("偶数：{0}\n奇数：{1}".format(sorted(even), sorted(odd)))

print("偶数：", sorted(even), "\n奇数：", sorted(odd))
