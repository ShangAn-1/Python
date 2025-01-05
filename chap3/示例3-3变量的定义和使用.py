luck_number=29 # 创建一个整型变量luck_number,并为其赋值为8
my_name='徐莹'

print('luck_number的数据类型是：',type(luck_number)) # <class 'int'>
print('my_name的数据类型是：',type(my_name)) # <class 'str'>

# Python动态修改变量的数据类型，通过不同类型的值就可以直接修改
luck_number='逢考必过'
print('luck_number的数据类型是：',type(luck_number)) # <class 'str'>

# 在Python中允许多个变量指向同一个值
no=number=8 # no与number都指向了8这个整数值
print(no,number)
print(id(no)) # id()查看对象的内存地址的  140724053607560
print(id(number)) # 140724053607560

