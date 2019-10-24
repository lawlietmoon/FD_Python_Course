# ### 高阶函数 : 能够把函数当成参数传递的就是高阶函数 map reduce sorted filter
# map
"""
map(func,iterable)
功能:把iterable 里面的数据一个一个的拿到func进行处理,把处理之后的结果,返回到迭代器之后,最后返回迭代器
参数:
	func 自定义函数 或 内置函数
	iterable 可迭代对象 ( 容器类型数据 range对象 迭代器)
返回值:
	迭代器
"""

# ### (1) ["1","2","3","4"] => [1,2,3,4]
# 常规
lst = ["1","2","3","4"]
lst_new = []
for i in lst:
	res = int(i)
	# print(res,type(res))
	lst_new.append(res)
print(lst_new)

# map 改写
from collections import Iterator,Iterable
it = map(int,lst)
res = isinstance(it,Iterator)
print(res) # True

# (1).next获取迭代器中的数据
res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)
res = next(it)
print(res)

# (2) for获取迭代器中的数据
it = map(int,lst)
print("<==>")
for i in it:
	print(i)

# (3) list 强转成列表,瞬间得到迭代器里所有数据
it = map(int,lst)
lst = list(it)
print(lst)

"""
代码解析:
首先拿出列表当中的第一个数 "1" ,扔到int函数当中进行处理, 强转成整型后扔到迭代器中
然后拿出列表当中的第二个数 "2" ,扔到int函数当中进行处理, 强转成整型后扔到迭代器中
然后拿出列表当中的第三个数 "3" ,扔到int函数当中进行处理, 强转成整型后扔到迭代器中
然后拿出列表当中的第四个数 "4" ,扔到int函数当中进行处理, 强转成整型后扔到迭代器中
最后返回迭代器,程序结束;
"""

# ### (2) [1,2,3,4] => [1,4,9,16]
#  常规
lst = [1,2,3,4]
lst_new = []
for i in lst:
	res = i**2
	# print(res)
	lst_new.append(res)
print(lst_new)

# 改写 
"""
自定义函数的时候,务必要加一个参数,
因为可迭代数据会源源不断的往函数中传值
还需要加上return , 需要把处理好的数据扔到迭代器中.
"""
def func(n):
	return n**2
it = map(func,lst)
# 强转列表,瞬间拿到所有数据
print(list(it))


# ### (3) dic = {97:"a",98:"b",99:"c"}   给["a","b","c"] => 返回[97,98,99]
dic = {97:"a",98:"b",99:"c"}
dic_new = {}
# 翻转字典键值对
for k,v in dic.items():
	dic_new[v] = k
print(dic_new) # {'a': 97, 'b': 98, 'c': 99}

lst = ["a","b","c"]
lst_new = []
for i in lst:
	# i => "a" "b" "c"   {'a': 97, 'b': 98, 'c': 99}
	res = dic_new[i]
	lst_new.append(res)
print(lst_new) #[97, 98, 99]

# map 改写
dic = {97:"a",98:"b",99:"c"}
lst = ["a","b","c"]
def func(n):
	dic_new = {}
	for k,v in dic.items():
		dic_new[v] = k
	# print(dic_new) # {'a': 97, 'b': 98, 'c': 99}
	return dic_new[n]
it = map(func,lst)
print(list(it))











