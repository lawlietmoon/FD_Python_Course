# ### set 集合类型 作用:做交叉并补操作
"""特点:不可查询不可修改,无序,自动去重"""

setvar = {"北雨栖风","顾十九","亢小龙"}
print(setvar)
print(type(setvar))

# 定义一个空集合
print("<=============>")
# setvar = {} 是空字典,不是空集合!
setvar = set() # 空集合唯一定义方法
print(setvar)
print(type(setvar))
print("<=============>")

# 集合既不可以获取,有不能够修改
# 是否可以获取集合当中的值? 不可以!
# setvar[0]

# 是否可以修改集合当中的值? 不可以
# setvar[0] = 90

# 集合可以自动去重
setvar = {"清十八","吴彦祖","清十八","周杰伦","罗志祥"}
print(setvar)

# ### dict 字典类型 
"""特点: 由键值对存储的数据,本质上无序,看起来有序"""

# 定义一个空字典
dictvar = {}
print(dictvar)
print(type(dictvar))

# 定义一个普通字典
"""
键和值用冒号隔开, 键值对之间用逗号隔开
{ 键1:值1  ,  键2:值2 , 键3:值3 ....  }


    3.6版本之前都是 字典和集合都是无序的
    3.6版本之后,把字典的字面顺序记录下来，当从内存拿数据的时候，
    根据字面顺序重新排序，所以看起来像有序,但本质上无序
"""
dictvar = { "top":"Theshy" , "middle":"肉鸡" ,"adc":"澡子哥","jungle":"clearlove20" ,"support":"北雨栖风" }
print(dictvar)
print(type(dictvar))

# (1)获取字典当中的值
res = dictvar["support"]
print(res)

# (2)修改字典当中的值
dictvar["support"] = "王思聪"
print(dictvar)


# ### 集合的值 字典的键 需要是可哈希数据(不可修改)

# 哈希算法: 可以均匀的把数据分散在内存当中进行存储的算法;
# 哈希算法要求数据必须可哈希:
"""
可哈希数据:(不可变)
	Number(int float bool complex) str tuple
不可哈希数据:(可变)
	list set dict
"""

# 字典
dictvar = {1:1 , 5.88:"abc" , False: 111 , 7-9j:90,"123456":"aaa" , (1,2,3):"bbb"}
# dictvar = {{"a":1}:43}----报错error,字典的键必须为可哈希数据(不可修改数据)
# print(dictvar)
print(dictvar[(1,2,3)])

# 集合 
setvar = { 1,6.7,False,4-90j,"abc",(1,2,3) }
print(setvar)

