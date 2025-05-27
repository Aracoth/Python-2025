from pathlib import Path
from time import ctime

path = Path("modules/ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
# print(ctime(path.stat().st_ctime))
# print(path.stat())
print(path.read_bytes())

with open("__init__.py", "r") as file:
    ...

print(path.read_text())
path.write_text("....")
path.write_bytes()
