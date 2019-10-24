# ###  Number自动类型转换 (主要对于int float bool complex四种数据类型)
"""
自动类型转换原则 : 默认向更高精度转换
默认精度从低到高排序:
	bool < int < float < complex
"""

# bool + int
res = True + 5
print(res) # 6

# bool + float
res = False + 5.67
print(res) # 5.67 

# bool + complex
res = True + 4 + 3j
print(res) # 5 + 3j

# int + float
res = 5 + 3.14
print(res) # 8.14

# int + complex
res = 3 + 90-80j
print(res) # 93 - 80j

# float + complex
res = 5.8 + 89-4j
print(res) # 94.8 - 4j
