# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import os
import shutil
from pathlib import Path

path = '\\\\10.18.50.220\\tvshows'  # 待读取文件的文件夹绝对地址
fileNames = os.listdir(path)  # 获得文件夹中所有文件的名称列表
resultPathName = 'Nothing.But.Thirty'

for fileName in fileNames:
    # 如果不是以目标目录名开头，则退出
    if not fileName.startswith(resultPathName):
        continue
    # 如果目录是目标目录，则退出（不重复复制）
    if fileName == resultPathName:
        continue

    resultPath = os.path.join(path, resultPathName)
    # 如果不存在目录，则创建
    if not Path(resultPath).exists():
        os.mkdir(resultPath)
    # 移动目录中文件到resultPath
    filePath = os.path.join(path, fileName)
    dirFileList = os.listdir(filePath)
    for dirFile in dirFileList:
        srcPath = os.path.join(path, fileName, dirFile)
        desPath = os.path.join(path, resultPathName, dirFile)
        shutil.move(srcPath, desPath)
    print(fileName + ' has moved!')
    # 清理目录
    dirFileList = os.listdir(filePath)
    if len(dirFileList) == 0:
        os.removedirs(filePath)
