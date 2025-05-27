from pathlib import Path

path = Path("modules/ecommerce/__init__.py")
# check if path exists - VERY USEFUL
print(path.exists())
path.is_file()
path.is_dir()
print(path.name)
print(path.stem)
print(path.suffix)
print(path.parent)
print(path)
path = path.with_name("file.txt")
path = path.with_suffix(".txt")
print(path)
print(path.absolute())
