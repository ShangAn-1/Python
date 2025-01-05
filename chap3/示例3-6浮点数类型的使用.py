height=187.6 # 身高
print(height)
print(type(height)) # type() 查看height这个变量的数据类型

c=1
b=1.0
a=1.00
print('c的数据类型是：',type(c)) # int(整数类型)
print('b的数据类型是：',type(b)) # float(浮点数类型)
print('a的数据类型是：',type(a)) # float(浮点数类型)

x=1.99E1314
print('科学计数法：',x,'x的数据类型：',type(x))

print(0.1+0.2) # 不确定的尾数问题 0.30000000000000004
print(round(0.1+0.25,2))