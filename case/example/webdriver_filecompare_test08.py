import sys
import difflib
import time
import os

def main():
    """主函数"""
    try:
        f1 = 'C:\\Users\\seamus\\Downloads\\configure_data\\1.txt'
        f2 = 'C:\\Users\\seamus\\Downloads\\configure_data\\2.txt'
    except  Exception as e:
        print("Error: "+ str(e))
        print("Usage : python compareFile.py filename1 filename2")
        sys.exit()

    if f1 == "" or f2 == "":#参数不够
        print("Usage : python compareFile.py filename1 filename2")
        sys.exit()

    tf1 = readFile(f1)
    tf2 = readFile(f2)

    d = difflib.HtmlDiff()#创建一个实例difflib.HtmlDiff
    writeFile(d.make_file(tf1,tf2))#生成一个比较后的报告文件，格式为html

def readFile(filename):
    """读取文件，并处理"""
    try:
        fileHandle = open(filename, "r")
        text = fileHandle.read().splitlines()
        fileHandle.close()
        return text
    except IOError as e:
        print("Read file error: "+ str(e))
        sys.exit()

def writeFile(file):
    """写入文件"""
    diffFile = open('diff_{}_.html'.format(time.strftime("%Y_%m_%d_%H_%M_%S",time.localtime())), "w")
    diffFile.write("<meta charset='UTF-8'>")
    diffFile.write(file)
    print("The file on {}".format(os.path.abspath(str(diffFile.name))))#提示文件生成在什么地方
    diffFile.close()


if __name__ == "__main__":
    main()

