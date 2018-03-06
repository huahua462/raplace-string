# # 文件替换程序
import sys, os

if len(sys.argv) <= 4:
    print "usage:./practice.py  old_text  new_text  filename"

    old_text, new_text = sys.argv[1], sys.argv[2]
    filename = sys.argv[3]

f = file(filename, 'rb')
new_f = file('.%s.bak' % filename, 'wb')  # 文件前面加一个点表示隐藏文件

for line in f.xreadlines():  # 把每一行都取出来
    new_f.write(line.replace(old_text, new_text))  # 替换文本并写入新文件中

f.close()
new_f.close()  # 一定要记得关文件

os.rename(filename, '%s.bak' % filename)  # 没改的
os.rename('.%s.bak' % filename, filename)  # 改过的