# 文件合并器
# 国内的BT资源下载很多都是分不同集的，导致一个电视剧在很多目录里面，现在可以通过这个脚本合并所有代码到一个目录中
# 如果操作nas中的文件，注意需要获取相应目录的读写权限

import os
import shutil
from pathlib import Path

path = '\\\\10.18.50.220\\tvshows'  # 待读取文件的文件夹绝对地址
fileNames = os.listdir(path)  # 获得文件夹中所有文件的名称列表
resultPathName = input("请输入目标目录名：\n")

for fileName in fileNames:
    # 如果不是以目标目录名开头，则退出
    if not fileName.startswith(resultPathName):
        continue
    # 如果目录是目标目录，则退出（不重复复制）
    if fileName == resultPathName:
        continue
    # 返回目录
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
    # 重新获取目录中的文件列表，如果为空，才进行清理
    if len(dirFileList) == 0:
        os.removedirs(filePath)
