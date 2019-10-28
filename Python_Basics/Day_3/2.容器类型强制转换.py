# ### 强制类型转换 容器类型数据 (str list tuple set )

var1 = "你好世界"
var2 = ["丐王坡","烟雨山","平安客栈","内城"]
var3 = ("丐王坡","烟雨山","平安客栈","内城")
var4 = {"丐王坡","烟雨山","平安客栈","内城"}
var5 = 411894
var6 = {"a":1,"b":2}

# 1.str 强制转换成字符串
"""就是单纯的在原有数据的两边套上引号"""
res = str(var2)
res = str(var4)
res = str(var5)
print(res , type(res))

# repr 不转义字符,原型化输出 , 可以显示引号
print(repr(res))

# 2.list 强制转换成列表
"""
如果是字符串:把每一个字符都当成一个新元素组合在一起,形成新列表
如果是字典:只保留字典的键
如果是其他容器:仅仅单纯的在原有数据的两边,套上中括号[]即可
"""
res = list(var1)
res = list(var3)
res = list(var4)
res = list(var6)
print(res , type(res))


# 3.tuple 强制转换成元组
"""
如果是字符串:把每一个字符都当成一个新元素组合在一起,形成新元组
如果是字典:只保留字典的键
如果是其他容器:仅仅单纯的在原有数据的两边,套上小括号()即可
"""
res = tuple(var1)
res = tuple(var2)
# res = tuple(var5) error
res = tuple(var6)
print(res)

# 4.set 强制转换成集合
"""
集合具有无序的属性:
如果是字符串:把每一个字符都当成一个新元素组合在一起,形成新集合
如果是字典:只保留字典的键 
如果是其他容器:仅仅单纯的在原有数据的两边,套上花括号{}即可
"""
res = set(var1)
res = set(var2)
res = set(var6)
print(res)

"""
# 括号里面不加任何值,可以转换出一个当前数据类型的值
str() list() tuple() set() dict()
"""
var = dict()
print(var)
