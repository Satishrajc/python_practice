import os

print(os.getcwd())
os.chdir(r"D:\Python_work\youtube")
print(os.getcwd())

os.rmdir("test_folder")
os.mkdir("test_folder")

print(os.listdir())

print(os.path.isdir("test_folder"))
print(os.path.isfile("../builtin_functions_for_all_data_types.txt"))
print(os.path.exists(r"D:\Python_work\youtube"))

print(os.path.basename(r"D:\Python_work\youtube\__init__.py"))
print(os.path.dirname(r"D:\Python_work\youtube\__init__.py"))
print(os.path.splitext(r"D:\Python_work\youtube\__init__.py"))
print(os.path.split(r"D:\Python_work\youtube\__init__.py"))
print(os.path.abspath(r"D:\Python_work\youtube\__init__.py"))
print(os.path.getsize(r"D:\Python_work\youtube\__init__.py"))
