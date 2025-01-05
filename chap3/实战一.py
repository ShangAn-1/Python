num=eval(input('请输入一个四位整数：'))
print('个位上的数：',num%10)
print('十位上的数：',num//10%10)
print('百位上的数：',num//100%10)
print('千位上的数：',num//1000%10)

print('-'*40)

num1=input("请输入一个四位整数：")
print('个位上的数',num1[3])
print('十位上的数',num1[2])
print('百位上的数',num1[1])
print('千位上的数',num1[0])