import sys

list = [1, 2, 3, 4]
it = iter(list)  # 创建迭代器对象
for x in it:
    print(x, end=",")

list = [1, 2, 3, 4]
it = iter(list)

print("\n============================================")
while True:
    try:
        print(next(it))
    except StopIteration:
        sys.exit()
