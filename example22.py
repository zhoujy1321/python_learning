#python File方法
#open()方法,close()方法
'''
open(file, mode='r'),file:文件路径,mode:文件打开模式
mode参数有:
x:写模式
b:二进制模式
+:打开一个文件进行更新
r  rb:只读,指针在开头
r+  rb+:读写,指针在开头
w  wb:只写,会删除原来内容
w+  wb+:读写,会删除原来内容
a  ab:追加,指针在结尾
a+  ab+:追加,指针在结尾
'''


#file对象
'''
file.close()
file.flush():刷新文件内部缓冲
file.read([size]):从文件读取指定的字节数
file.readline([size]):读取整行包括'\n'
file.readlines([size]):读取所有行并返回列表
file.seek(offset,[whence]):移动文件读取指针到指定位置
file.tell()
file.write(str):将字符串写入文件,返回写入字符长度
file.writelines(sequence):向文件写入一个字符串列表,要换行需要自己加入换行符
'''