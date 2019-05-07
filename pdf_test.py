# coding=utf-8

import PyPDF2

file_path = 'I:\QQ\QQDownloads\MobileFile\PythonCookbook中文版v3.pdf'

with open(file_path, 'rb') as f:
    file_reader = PyPDF2.PdfFileReader(f)
