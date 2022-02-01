from stat import ST_CTIME
import time
import os
import shutil

path = input("Enter the designated path: ")
days = int(input("Enter the number of days: "))
days = time.time()

os.path.exists(path)
if(os.path.exists(path)==True):
    for filename in os.walk(path):

        os.path.join(path)
        ctime = os.stat(path).st_ctime
        os.remove(path)
        shutil.rmtree(path)