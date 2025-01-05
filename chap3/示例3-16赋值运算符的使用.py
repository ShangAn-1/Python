x=10 # 直接赋值，直接将10赋值给左侧的变量x
y=20

x=x+y # 将x+y的值赋值给x，x的值为30
print(x) # x的值是30

x+=y # 相当于 x=x+y
print(x) # x=50

x-=y # 相当于 x=x-y
print(x) # x=-10

x*=y # 相当于 x=x*y
print(x) # x=300

x/=y # 相当于 x=x/y 发生了类型转换 x的数据类型为float类型
print(x,type(x)) # <class 'float'>

x%=y # 相当于 x=x%y
print(x) # 10.0

z=3

x//=z # 相当于 x=x//z
print(x) # 3.0

x**=2 # 相当于 x=x**2
print(x) # 9.0

# Python 支持链式赋值
a=b=c=100 # 相当于执行 a=100 b=100 c=100
print(a,b,c)

# Python 支持系列解包赋值
a,b=10,20 # 相当于执行了 a=10 b=20
print(a,b)

print('----------如何交换两个变量的值呢？-----------')
a,b=b,a # 将b的值赋给a, 将a的值赋给b
print(a,b)

a&=b
print(a)