'''
创建一个文件并写入
打开一个文件并读取
'''

# 创建一个文件并写入
fw = open("sample.txt", "w")
fw.write("Wrting some stuff in my text file\n")
fw.write("I like bacon\n")
fw.close()

# 打开一个文件并读取
fr = open("sample.txt", "r")
text = fr.read()
print(text)
fr.close()
