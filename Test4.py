# 用来管理每一行内容的输出，这里的y表示乘法x*y=z中的y
for y in range(1, 10):
    # 用来管理每一列内容的输出，表这里的x表示乘法x*y=z中x
    for x in range(1, y+1):
        # 打印出x*y=z，并且使用end='\t'表示制表符
        print("{}*{}={}".format(y, x, x*y), end="\t")
    # 每一行的内容打印完之后换行
    print()