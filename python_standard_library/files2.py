from pathlib import Path
from time import ctime

# good module for copying files
import shutil

# the file to be copied
source = path = Path("modules/ecommerce/__init__.py")
# new target location: current directory
target = Path() / "__init__.py"

# cleaner way to copy file
shutil.copy(source, target)
# messier way to copy file
target.write_text(source.read_text())
