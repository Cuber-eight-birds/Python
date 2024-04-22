# 所有的书和数量都以字典的形式储存
books_dic = {'82年生的金智英': 3, '了不起的盖茨比': 6, '乌合之众': 5, '活着': 8, '小王子': 6, '设计的意义': 2}
for books in books_dic:
    if books_dic[books] > 5:
        print(books)
        books_dic[books] = '分配'
    else:
        books_dic[books] = '自留'
print(books_dic)