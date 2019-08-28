import subprocess
import os
from testfile import file, dst

cmd = 'pycodestyle %s'%file
p = subprocess.Popen('pycodestyle test1.py', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate(0)
p = str(p[0])[2:-1]
#p = str(p)
#p = p[2:-1]
print(p)
dst.close()
os.remove("%s"%file)
print("File Removed!")
