from pathlib import Path

path = Path("modules/ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

# returns files & directories
for p in path.iterdir():
    print(p)

# alternative shorter list comprehension
# filtered to only show directories
paths = [p for p in path.iterdir() if p.is_dir()]
# recursively returns all files with '.py' in path
py_files = [p for p in path.rglob("*.py")]
print(paths)
print(py_files)
