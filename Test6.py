# 获取密码信息
a = input('请输入密码结束循环，你有5次机会：')
# 自定义5次回答机会
n = 5
while True:
    # 如果密码正确，则输出“密码正确”，退出循环
    if a == '198764':
        print('密码正确')
        break
    # 如果密码不正确
    else:
        # 回答机会减1
        n = n - 1
        # 重新获取密码，次数减1
        print('请输入密码结束循环，你有%d次机会：' % n, end='')
        a = input()
        # 5次之后，跳出循环
        if n == 1 and a != '198764':
            print('5次循环你都错过了，else语句生效了')
            break
    