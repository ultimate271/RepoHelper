import os.path
from distutils.dir_util import copy_tree
from distutils.file_util import copy_file

def copy(source, dest):
    #Works like cp -r does, because python doesn't have such a thing
    #Fuck python
    if os.path.isfile(source):
        copy_file(source, dest)
    elif os.path.isdir(source):
        copy_tree(source, dest)
