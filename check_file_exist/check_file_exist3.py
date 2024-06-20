import os

"""
os.access方法可以检查当前用户是否有访问指定路径的权限，在此也可以用来检查文件是否存在。
使用os.F_OK作为模式参数时，它可以检查文件的存在性.
请注意，os.access在某些情况下可能会因为权限问题（比如当前用户没有足够的权限访问目标文件，即使文件存在）而不准确。
"""
file_path = "./a.txt"
if os.access(file_path, os.F_OK):
    print("File exist.")
else:
    print("File doesn't exist.")
