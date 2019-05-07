# coding=utf-8

import os
import PyPDF2


file_path = 'I:\QQ\QQDownloads\MobileFile'
os.chdir(file_path)

file_writer = PyPDF2.PdfFileWriter()

with open('PythonCookbook中文版v3.pdf', 'rb') as f:
    file_reader = PyPDF2.PdfFileReader(f)   # 创建Reader对象
    for pageNumber in range(file_reader.numPages):
        pageObj = file_reader.getPage(pageNumber)
        if 'OpenStack' in pageObj.extractText():
            continue
        else:
            file_writer.addPage(pageObj)

    with open('PythonCookbook中文版v3_updated.pdf', 'wb') as f:
        file_writer.write(f)
