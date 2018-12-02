import os
import sys
from shutil import copyfile
path=os.path.abspath('./')
path1=path+os.path.sep+sys.argv[1]
path2=path+os.path.sep+sys.argv[2]
copyfile(path1,path2)
