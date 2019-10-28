# ### 二级容器: 外面是一个容器类型的数据,里面的元素还是一个容器类型的元素

# 二级列表
listvar = [1,2,3,4,5,[6,7,8]]
# 二级元组
tuplevar = (1,2,3,4,5,(11,12,34),90)
# 二级集合 Number str tuple
setvar = {1,2,3,"a","b","c",(5,6,7)}
# 二级字典
dictvar = {"a":1 , "b":2 ,"c":{"d":1,"e":2}}

# 四级容器
container = [1,2,3,4,5,(6,7,8,["a","b","c",{"aa":1,"bb":"王遗风"}])]
# (6, 7, 8, ['a', 'b', 'c', {'aa': 1, 'bb': '王遗风'}])
res = container[-1]
print(res)
# ['a', 'b', 'c', {'aa': 1, 'bb': '王遗风'}]
res2 = res[-1]
print(res2)
# {'aa': 1, 'bb': '王遗风'}
res3 = res2[-1]
print(res3)
# 王遗风
res4 = res3["bb"]
print(res4)

# 简写
res = container[-1][-1][-1]["bb"]
print(res)

# 等长的二级容器
container = [(1,2,3,4) , {"a","b","c","d"}]
container = [ (1,2) , [3,4]]


# ### dict 强制转换成字典
"""必须是等长的二级容器,并且里面的元素个数是2个"""

# (1)外面是列表,里面可以是元组或者列表(推荐)
listvar = [ ("a",1) , ["b",2]]
dictvar = dict(listvar)
print(dictvar , type(dictvar))


# 语法上可以,但是不推荐,因为集合无序,达不到想要的效果 (不推荐)
listvar = [ ("a",1) , ["b",2] , {"c",3}]
dictvar = dict(listvar)
print(dictvar)

# 字符串作为元素,有一定的局限性,仅限于2个元素才可以(不推荐)
listvar = [ ("a",1) , ["b",2] , "c3"]
dictvar = dict(listvar)
print(dictvar)

# (2)外面是元组,里面可以是元组或者列表(推荐)
tuplevar = ( ("a",1) , ["b",2] )
dictvar = dict(tuplevar)
print(dictvar)

# (3)外面是集合,里面只能放元组
setvar = { ("a",1),("b",2) }
dictvar = dict(setvar)
print(dictvar)


# 去掉列表中的所有重复数据
listvar = [1,2,3,3,4,4,5,6,7,"a","a","b","b","c","c"]
res = set(listvar)
print(res,type(res))
lst = list(res)
print(lst,type(lst))

# 可以修改元组嵌套的列表中的数据;
tuplevar = (1,2,3,4,5,6,["a","b","c"])
lst = tuplevar[-1]
print(lst)
lst[2] = "d"
print(tuplevar)
