import subprocess

java_v = subprocess.check_output("python --version")
print("Opa")
print(java_v)