# 生成1到10之间的随机数
import random
target = random.randint(1,10)
count = 0
while True:
    count += 1 
    geuss_age = int(input('猜年龄！（提示：年龄在1到10之间）'))
    if geuss_age > target:
        print('猜大了！')
    elif geuss_age < target:
        print('猜小了！')
    else:
        print('猜对了！你一共猜了{}次！'.format(count))
        break