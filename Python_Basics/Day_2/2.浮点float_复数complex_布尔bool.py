# ### 数据类型 Number( 包含 float,bool,complex )

# float 浮点型 : 小数

# 表达方式一
floatvar = 6.59
print(floatvar)
print( type(floatvar) )
print( id(floatvar) )

# 表达方式二 科学计数法
floatvar = 5.72e4
print(floatvar)
print( type(floatvar) ) 
print( id(floatvar) )

# bool 布尔型 : True_真 False_假
boolvar = False
print( type(boolvar) )
print( id(boolvar) )


# complex 复数类型
"""
实数 + 虚数 组成的
3 + 4j
3  => 实数
4j => 虚数
j : 如果有一个数,他的平方等于-1,那么这个数就是j.用来表达高精度的数据类型 
j 是内置的关键字 不能随意改变
"""
# 表达方式一
complexvar = 3 + 4j
print(complexvar)
print(type(complexvar))
print(id(complexvar))

# 表达方式二
"""complex(实数,虚数)"""
complexvar = complex(3,4)
complexvar = complex(3,-4)
complexvar = 56j
print(complexvar)
print(type(complexvar))
