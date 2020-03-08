import os
import shutil
import datetime
import time

for (dirpath, dirnames, filenames) in os.walk('/Users/andrea/Downloads/'):
    oggi= datetime.datetime.now()
    diff = oggi - datetime.datetime.fromtimestamp(os.path.getatime(dirpath))
    if(diff > datetime.timedelta(days=7)):
        shutil.rmtree(dirpath)
        print("file eliminato :",filenames)
    else:
        print("*")


