# 分数以字典嵌套列表存储，列表中依次为语文、数学、英语的成绩
scores = {'小李': [95, 98, 90], '小花': [96, 90, 94],
          '小华': [85, 80, 90], '小胖': [87, 94, 89],
          '小红': [79, 85, 90]}
# 遍历字典取出每个人的名字
for name in scores:
    # 初始化个人总分变量scores_sum=0
    scores_sum = 0
    # 遍历每个人自己的三科成绩并累加
    for score in scores[name]:
        scores_sum += score
    # 打印每个人的总分
    print('{}的总分为:{}'.format(name, scores_sum))

# 初始化班级人数计数器
count = 0
# 初始化各科成绩
chinese_sum = 0
math_sum = 0
english_sum = 0
# 遍历每个人的成绩并分别累加
for name in scores:
    chinese_sum += scores[name][0]
    math_sum += scores[name][1]
    english_sum += scores[name][2]
    # 每遍历一个人，人数计数器+1
    count += 1
# 打印班级平均分，平均分为总分/人数
print('语文的平均分为{}分\n数学的平均分为{}分\n英语的平均分为{}分'.format(
    chinese_sum/count, math_sum/count, english_sum/count))