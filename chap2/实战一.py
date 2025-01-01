fp=open('text.txt','w') # 打开文件
print('人生苦短，我用Python',file=fp) # 将内容写入文件中
fp.close() # 关闭文件