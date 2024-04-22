# 创建一个空字符串
newstring = ''
# input语句获取要进行反转的字符串内容
a = input('输入字符串:')
# 字符串求长度，用于确定for循环次数
n = len(a)
for i in range(n):
    # 字符串拼接
    newstring = newstring + a[n-1-i]
print(newstring)