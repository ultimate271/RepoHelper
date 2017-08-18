import xml.etree.ElementTree as ET
import argparse
import os.path
import time
import shutil

class FileMapping:
    def __init__(self, reponame, destination):
        self.reponame = reponame
        self.destination = destination
    #returns a pair (repotime, desttime) with the two last updated times of the files. 
    #returns None in the appropiate spot in the file doesn't exist
    def times(self):
        if not os.path.isfile(self.reponame):
            repotime = 0.0
        else:
            repotime = os.path.getmtime(self.reponame)
        if not os.path.isfile(self.destination):
            desttime = 0.0
        else:
            desttime = os.path.getmtime(self.destination)
        return (repotime, desttime)

    def update(self):
        (rtime, dtime) = self.times()
        if (rtime, dtime) == (0.0, 0.0):
            return
        if rtime > dtime:
            confirm = raw_input("Copy {0} to {1}? (y/n) ".format(self.reponame, self.destination))
            if confirm == 'y':
                shutil.copyfile(self.reponame, self.destination)
                print "Copied"
        if dtime > rtime:
            confirm = raw_input("Copy {1} to {0}? (y/n) ".format(self.reponame, self.destination))
            if confirm == 'y':
                shutil.copyfile(self.destination, self.reponame)
                print "Copied"

    def getArrow(self):
        (rtime, dtime) = self.times()
        if (rtime, dtime) == (0.0, 0.0):
            return "=="
        if rtime > dtime:
            return "->"
        if dtime > rtime:
            return "<-"


        
DEFAULT_SETTINGS_FILE = 'settings.xml'
parser = argparse.ArgumentParser()
parser.add_argument('-x')
xFilename = vars(parser.parse_args())['x'] or DEFAULT_SETTINGS_FILE

tree = ET.parse(xFilename)
root = tree.getroot()

mappingDict = {}
for child in root:
    mappingDict[child.find('name').text] = FileMapping(child.find('reponame').text, child.find('destination').text)

print "Repo Helper 0.0.1.0"

proceed = True
while proceed:
    print "--------------------"
    print "The following mappings are defined in {0}:".format(xFilename)
    for k, v in mappingDict.items():
        print "{0:>20} : {1:20} {3} {2}".format(k, v.reponame, v.destination, v.getArrow())
        (rtime, dtime) = v.times()
        print "                       {0:20}    {1}" .format( \
                time.strftime("%b %d %Y %H:%M:%S", time.gmtime(rtime)), \
                time.strftime("%b %d %Y %H:%M:%S", time.gmtime(dtime)))
        print "                       --------------------------------------------------------"
    print "Input a tagname to perform the operation, or e(x)it, (a)ll, (p)ush"
    usercmd = raw_input('>> ')
    if usercmd == 'x':
        proceed = False
    elif usercmd == 'a':
        print 'Do a here'
    elif usercmd == 'p':
        print 'Do p here'
    elif usercmd == '':
        print 'Please input a command'
    else:
        if usercmd in mappingDict.keys():
            mappingDict[usercmd].update()
        else:
            print 'invalid command'
    if usercmd != 'x':
        raw_input()

   # print child.tag
   # print child.attrib
   # print child.text
   # for child2 in child:
   #     print child2.tag
   #     print child2.attrib
   #     print child2.text
