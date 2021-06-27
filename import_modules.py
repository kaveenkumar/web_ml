echo $PATH  # on a terminal, returns the paths that the os looks at for programs
export PATH='/User/bin/dir:$PATH'  # add your own path to os path environment
source .bashrc | restart terminal

# python3 from path specified, instead of checking the PATH
/usr/local/bin/python3  # running this manually always runs the program specified instead of checking the path
anaconda/bin/python  # runs anaconda python irrespective of what base python is, irrespective of anaconda in environment PATH or not

# to add your own directory path to the python module environment paths
# this allows us to have our modules in a seperate directoy and let python know to check this directory while importing modules
nano ~/.bash_profile   # on mac
nano ~/.bashrc  # on linux
export PYTHONPATH='/Users/my_modules'

import sys
print(sys.path)  # these paths are where python checks for modules
print(sys.executable)  # current python executable location

sys.path.append('drive:/modules/')  # add your own path
import myfuncs as f
f.somefunc()

import my_module
print(my_module.__file__)  # returns the path / location of the module
print(dir(my_module))  # returns all attributes and methods within this module

"""
LEGB rule for functions and variables
Local, Enclosing, Global, Built-in
"""
import builtins
print(dir(builtins))  # built-in methods and attributes
