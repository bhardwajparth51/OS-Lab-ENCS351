import subprocess
import os

base = "/home/bhardwajparth/OS/Assignment-01/Assignment-04/scripts"

scripts = ["script1.py", "script2.py", "script3.py"]

for s in scripts:
    full_path = os.path.join(base, s)
    print(f"Executing {full_path}...")
    subprocess.call(['python3', full_path])
