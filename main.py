# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import shutil
from pathlib import Path

path = '\\\\NAS4F66FF\\tvshows'  # 待读取文件的文件夹绝对地址
files = os.listdir(path)  # 获得文件夹中所有文件的名称列表
resultPathName = 'Nothing.But.Thirty'

for file in files:
    if not file.startswith(resultPathName):
        continue
    print(file)
    resultPath = os.path.join(path, resultPathName)
    # 如果不存在目录，则创建
    if not Path(resultPath).exists():
        os.mkdir(resultPath)
    # 移动目录中文件到resultPath
    dirFileList = os.listdir(os.path.join(path, file))
    for dirFile in dirFileList:
        srcPath = os.path.join(path, file, dirFile)
        desPath = os.path.join(path, resultPathName, dirFile)
        shutil.move(srcPath, desPath)
