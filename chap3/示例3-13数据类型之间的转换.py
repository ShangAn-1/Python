x=10
y=4
z=x/y # 在执行除法运算的时候，将运算的结果赋值给z
print(z,type(z)) # 隐式转换，通过运算隐式的转换了结果的类型

# float类型转成int类型，只保留整数部分
print('float类型转成int类型：',int(3.14))
print('float类型转成int类型：',int(3.9))
print('float类型转成int类型：',int(-3.14))
print('float类型转成int类型：',int(-3.9))

# 将int转成float类型
print('将int转成float类型：',float(10))

# 将str转成int类型
print(int('100')+int('200'))

# 将字符串转成int或float时报错的情况
# print(int('18a')) ValueError: invalid literal for int() with base 10: '18a'
# print(int('3.14')) ValueError: invalid literal for int() with base 10: '3.14'
# print(float('45a.987')) ValueError: could not convert string to float: '45a.987'

# chr(),ord()是一对
print(ord('徐'))
print(chr(24464))

# 进制之间的转换操作，十进制与其他进制之间的转换
print('十进制转换成十六进制：',hex(24464))
print('十进制转换成八进制：',oct(24464))
print('十进制转换成二进制：',bin(24464))