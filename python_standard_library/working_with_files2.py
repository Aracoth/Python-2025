from pathlib import Path
from time import ctime
import shutil

source = path = Path("modules/ecommerce/__init__.py")
target = Path() / "__init__.py"

shutil.copy(source, target)
target.write_text(source.read_text())
