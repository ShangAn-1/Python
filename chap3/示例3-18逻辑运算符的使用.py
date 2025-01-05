print(True and True)
print(True and False)
print(False and False)
print(False and True)

print('-'*20)

print(8>7 and 9>5) # True
print(8>7 and 9<5) # False
print(9<5 and 10/0) # False （短路原则） 10/0并没有运算，当第一个表达式的结果为False，直接得到结果，不会计算 and 右侧的表达式了

print('-'*20)

print(True or True)
print(True or False)
print(False or True)
print(False or False)

print('-'*20)
print(8>7 or 9>5) # True
print(8>7 or 9<5) # True
print(9>5 or 10/0) # True , 左侧表达式结果为Ture时，or的右侧表达式根本不执行运算符（短路原则）

print('-'*20)

print(not True) # False
print(not False) # True
print(not 8>7) # False