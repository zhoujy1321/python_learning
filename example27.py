#python标准库概览

#操作系统接口
#os模块提供不少于操作系统相关联的函数


#文件通配符
#glob模块提供了一个函数用于从目录通配符搜索中生产文件列表


#命令行参数
#以链表形式存储于sys模块的argv变量:sys.argv
#错误输出重定向和程序终止
#sys还有stdin,stdout,stderr属性:sys.stderr.write


#字符串正则匹配
#re模块为高级字符串提供了正则表达式工具


#数学
#math模块为运算提供了对底层c函数库的访问
#random提供了生成随机数的工具


#访问互联网
#处理从urls接受数据的urllib.request,用于发送电子邮件的smtplib
'''
import smtplib
server = smtplib.SMTP('localhost')
server.sendmail('zjy1061832496@mail.ustc.edu.cn', '1061832496@qq.com',
\'''To: 1061832496@qq.com
From: zjy1061832496@mail.ustc.edu.cn
oh no
\'''#)
server.quit()
'''


#日期和时间
#datetime模块
from datetime import date
now = date.today()
print(now)


#数据压缩
#以下模块支持通用的数据打包和压缩格式:zlib, gzip, bz2, zipfile, tarfile


#性能度量
#Timer模块


#测试模块
#doctest模块