import subprocess

try:
    completed = subprocess.run(
        ["python3", "other.py"], capture_output=True, text=True, check=True
    )
    print("args", completed.args)
    print("returncode", completed.returncode)
    # stderr: standard error
    print("stderr", completed.stderr)
    print("stdout", completed.stdout)
except subprocess.CalledProcessError as ex:
    print(ex)
