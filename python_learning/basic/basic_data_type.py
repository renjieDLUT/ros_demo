#!/usr/bin/python3
# -*- coding: windows-1252 -*-
# 数字类型
a, b, c, d = 20, 5.5, True, 4+3J
print(type(a), type(b), type(c), type(d))

# 字符串
# 可索引，可截取
# 不可改变元素
str = "renjie"
print(str)
print(str[0:-1])
print(str[-1::-1])

# 列表,存储的元素类型可不同
# 可索引，可截取，元素可改变，
list = ['abcd', 786, 2.23, 'runoob', 70.2]
print(list)
print(list[-1])
print(list[0:3:2])
list[0] = 8
print(list)

# 元组，存储的元素类型可不同，可包含list列表
# 可索引，可截取
# 不可修改元素
# 特殊元组，（包含1个，0个元素的元组）
tuple = ('abcd', 10, [1, 2, 3], 'name')
print(tuple[0])
print(tuple[0:3:1])
tup1 = ()
tup2 = (65,)

# 集合，存储的元素类型可不同，删除重复元素
# 成员关系测试
# 不可索引，不可截取
sets = {'google', 8, 'baidu', 'name'}
print(sets)
if "google" in sets:
    print("google in set")
else:
    print("google not in set")

b = set(["renjie", "hxj"])
print(b)


# 字典，无序的对象集合
# 可通过键来索引，键key必须使用不可变类型
tinydict = {'name': 'runoob', 'code': 1, 'site': 'www.runoob.com'}
print(tinydict['name'])


# 数据类型转换
a = 8
print(type(oct(a)))
print(int(oct(a), 8))
