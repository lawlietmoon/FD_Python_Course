# ###  Number强制类型转换 ( int float bool complex)

var1 = 89
var2 = 5.87
var3 = True
var4 = 4+5j
var5 = "135"

# 1.int 强制转换成整型
res = int(var2)
res = int(var3)
# res = int(var4) error
res = int(var5)
print(res , type(res))

# 2.float 强制转换成浮点型
res = float(var1)
res = float(var3)
res = float(var5)
print(res , type(res))

# 3.complex 强制转换成复数
res = complex(var1) # 89 +0j
res = complex(var2) # 5.87 +0j
res = complex(var3) # 1 + 0j
res = complex(var5) # 135 + 0j
print(res , type(res))


# 4.bool 强制转换成布尔型 True 真的 False 假的
res = bool(None)
print(res)

# 布尔类型为假的十种情况(重要)
# 0 0.0 0j False '' () [] set() {} None

# None 是python中的关键字,代表空的,什么也没有,一般用于变量的初始化操作
var = None

"""
# 括号里面不加任何值,可以转换出一个当前数据类型的值
int() float() bool() complex()
"""
var =complex()
print(var)
