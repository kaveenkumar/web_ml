import sys

print(sys.path)  # these paths are where python checks for modules

sys.path.append('drive:/modules/')  # add your path
import myfuncs as f

f.somefunc()
