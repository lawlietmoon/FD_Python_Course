# ### filter 
"""
filter(func,iterable)
功能: 过滤
	   在自定义的函数中,
	   如果返回True   代表保留该数据
	   如果返回Falase 代表舍弃该数据
			
参数: 
	 func 自定义函数
	 iterable 可迭代数据(容器类型数据, range对象, 迭代器)
返回值:
	迭代器
"""
lst = [1,2,3,4,5,6,7,8,9,10]
lst_new = []
# 要所有的奇数
for  i in lst:
	if i % 2 == 1 :
		lst_new.append(i)
print(lst_new)


# filter
def func(n):
	if n % 2 == 0:
		return False
	else:
		return True

it = filter(func,lst)
from collections import Iterator,Iterable
res = isinstance(it,Iterator)
print(res)

# (1)next 
res = next(it)
print(res)

# (2)for
for i in it:
	print(i)

# (3) for + next
it = filter(func,lst)
# 单纯的循环2次而已
for i in range(2):
	# 调用迭代器两次
	res = next(it)
	print(res)

# (4) list
it = filter(func,lst)
print(list(it))


# 改写成lambda 表达式
it = filter(lambda n : True if n % 2 == 1 else False ,lst)
print(list(it))




























