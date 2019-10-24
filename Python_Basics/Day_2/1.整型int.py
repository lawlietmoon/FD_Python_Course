# ### Number数据类型 (包含 int,float,bool,complex)

# int 整型 (正整型,0,负整型)

intvar = 411894
print(intvar)

# type 可以获取一个变量的类型
res =  type(intvar) # <class 'int'>
print(res)

# id   可以获取一个变量对应值的地址
res = id(intvar) # 1525062112
print(res)


# 十六进制整型
intvar = 0xff
print(intvar)
# 获取类型
print( type(intvar) )
# 获取地址
print( id(intvar) )

# 八进制整型
intvar = 0o235
print(intvar)
print( type(intvar) ) 
print( id(intvar) )

# 二进制整型
intvar = 0b101
print(intvar)
print( type(intvar) )
print( id(intvar) )
