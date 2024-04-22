# 提问有没有人卖包子和西瓜
buying_steamed_stuffed_bun = input('市场上有没有人卖包子？\n')
buying_watermelon = input('市场上有没有人卖西瓜？\n')

# 使用条件判断来判断有没有人卖包子
if buying_steamed_stuffed_bun == '有':
    
    # 进一步判断有没有人卖西瓜
    if buying_watermelon == '有':
        print('卖一个包子')
        
    # 否则
    else:
        print('卖十个包子')