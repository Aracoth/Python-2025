import subprocess

# cmd opens the cmd prompt: /c executes the command
completed = subprocess.run(["cmd", "/c", "dir"], capture_output=True, text=True)
print(type(completed))
print("args", completed.args)
print("returncode", completed.returncode)
# stderr: standard error
print("stderr", completed.stderr)
print("stdout", completed.stdout)
