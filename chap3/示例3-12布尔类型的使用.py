x=True
print(x)
print(type(x)) # <class 'bool'>
print(x+10) # 11 -->1+10
print(False+10) # 10 -->0+10

print('--------------------')
print(bool(18)) # 测试整数18的布尔值 True
print(bool(0)) # 测试整数0的布尔值 False
print(bool(0.0)) # 测试浮点数0.0的布尔值 False
print(bool(-18)) # 测试整数-18的布尔值 True
# 总结，非0数的布尔值都是True

print(bool('北京欢迎你')) # True
print(bool('')) # False
# 总结, 所有非空字符串的布尔值都是True

print(bool(False)) # False
print(bool(None)) # False