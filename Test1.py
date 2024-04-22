# scores列表里嵌套了三个科目的列表
chinese = [55, 60, 95, 90, 88, 87, 61, 59, 78, 90]
math = [66, 77, 90, 99, 58, 69, 77, 88, 82, 95]
english = [100, 98, 66, 43, 66, 47, 91, 67, 89, 59]
scores = [chinese, math, english]

# 依次从scores列表里取出chineses、math、english列表
for score in scores:
    # 从取出的小列表里取出分数跟60进行比较
    for s in score:
        # 分数大于等于60分的就打印出来
        if s >= 60:
            print(s)