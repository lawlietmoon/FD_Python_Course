# ### 容器类型数据_list 列表
"""特点: 可获取,可修改,有序"""
# 定义一个空列表 
listvar = []
print(listvar)
print( type(listvar) )

# 正向索引   0   1    2     3    4
listvar =  [89,7.56,False,8-9j,"十八"]
# 逆向索引  -5  -4   -3    -2   -1

# (1)获取列表中的值
res = listvar[4] # 十八
# 逆向索引可以迅速得到列表当中最后一个元素(python特有)
res = listvar[-1] # 十八
print(res)

# 其他语言如何得到列表中最后一个元素? (通用写法)
"""
len()函数 可以获取容器类型数据的长度(元素个数)
"""
res = len(listvar)
print(res) #5
res2 = listvar[res-1]
print(res2)

# (2)修改列表中的值
listvar[1] = "北雨栖风" # 7.56 => 北雨栖风
print(listvar)

# ### 容器类型数据_tuple 元组
"""特点: 可获取,不可修改,有序"""
"""
用逗号,来区分是否是元组,逗号是元组这个数据类型的标识
如果定义一个空元组,可以直接使用().只能是空元组;
"""

# 定义一个空元组
tuplevar = ()
print(tuplevar)
print(type(tuplevar))

# 它不是元组(没有,)
tuplevar = (5-9j)
# 它是元组
tuplevar = (5-9j,)
tuplevar = 1,2,3,4,5
tuplevar = (1,2,3,4,5) # 推荐写法
print(tuplevar , type(tuplevar) )

# (1) 获取元组中的值

# 正向         0         1        2      3
tuplevar = ("顾十九","北雨栖风","铭启","沉机")
# 逆向        -4        -3       -2      -1

res = tuplevar[2] # 铭启
res = tuplevar[-1] # 沉机
print(res)

# (2) 元组不能够修改其中的值

# tuplevar[0] = "清十八"----报错error
# print(tuplevar)


# ### 字符串 str
"""特点: 可获取,不可修改,有序"""
# 正向    0  1 2 3 4 5 6
strvar = "骑马吃遍长安瓜"
# 逆向   -7 -6-5-4-3-2-1

# (1) 获取字符串当中的元素
res = strvar[5] # 安
res = strvar[-2] # 安
print(res)

# (2) 是否可以修改字符串当中的元素值?
# strvar[0] = "你"----报错error
# print(strvar)
