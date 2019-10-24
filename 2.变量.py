# ### 变量：可以改变的量就是 变量，实际上变量是在内存内开辟空间

# 1.变量的概念

admin_1 = "清十八" 
admin_1 = "北雨栖风"
print(admin_1)


# 2.变量的声明
# 形式一
a = 1
b = 2
print(a,b)


# 形式二
a,b = 3,4
print(a)
print(b)

# 形式三
a = b = 5
print(a,b)

# (3)变量的命名

"""
          变量的命名
字母数字下划线，首字符不能为数字
严格区分大小写，且不能使用关键字
变量命名有意义，且不能使用中文哦
"""

_411894Yy = 1
abc = 3
ABC = 4
print(abc)
print(ABC)

# python系统关键字
import keyword# import 引入 keyword模块
print(keyword.kwlist)# 打印该模块中所有的关键字 kwlist是其中的一个属性。

'''
Python中的关键字

['False', 'None', 'True', 'and', 'as', 
'assert', 'break', 'class', 'continue', 'def', 
'del', 'elif', 'else', 'except', 'finally', 'for', 
'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 
'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


'''


恶人谷 = "自在逍遥"
print(恶人谷) # Python不会报错,但是不推荐

#python 支持中文语法命名变量，但是严禁使用。
"""
    utf-8 国际标准编码(可变长的unicode编码)： 中文字符占用3个字节，英文符号占用1个字节
    gbk   国标编码 ，中文字符占用2个字节， 英文符号占用1个字节
"""

# (4)变量的交换

# 通用写法
a = 314
b = 217
tmp = a
a = b
b = tmp
print(a,b)

# python特有,非常简便!
a = 314
b = 217
a,b = b,a # 将a与b的值互换
print(a,b)


# 定义常量 ： 约定俗成全都变成大写；永远不能改变的量
CURRENTTIME = "201910241639"
