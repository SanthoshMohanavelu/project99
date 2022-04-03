import time
import os
import shutil

days = time.time()
path = '/usr/local/bin'
ctime = os.stat(path).st_ctime


isExist = os.path.exists(path)
os.walk(path)
os.path.join()
os.remove(path)
