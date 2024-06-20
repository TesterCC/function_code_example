from pathlib import Path  # after python3.4+
# 从Python 3.4开始，pathlib模块被引入作为处理文件系统路径的现代化方式。它提供了一个面向对象的接口来处理文件和目录。

file_path = Path('./a.txt')
if file_path.exists():
    print("File exist.")
else:
    print("File doesn't exist.")
