from pathlib import Path

path = Path("modules/ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
print(path.stat())
