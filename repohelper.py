import argparse
from maps import Maps

def buildPromptString(Keyword, x, y):
    return "{0} {1} to {2}?(y/n) : ".format(Keyword, x, y)

def buildPrompt (Keyword):
    return lambda x,y: raw_input(buildPromptString(Keyword, x, y)) == "y"

DEFAULT_SETTINGS_FILE = 'settings.xml'

#Some comments about main
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-x')
    xFilename = vars(parser.parse_args())['x'] or DEFAULT_SETTINGS_FILE
    mymaps = Maps(xFilename)

    proceed = True
    while proceed:
        mymaps.printMenu()
        usrin = raw_input(" > ").split()
        if len(usrin) == 0:
            print "Enter a command"
        elif len(usrin) == 1:
            if usrin[0] == "x":
                print "Exiting"
                proceed = False
            else:
                print "Please input a valid command"
        elif len(usrin) == 2:
            if usrin[0] == "revert" or usrin[0] == "r":
                if usrin[1] == "all":
                    mymaps.revertAll(buildPrompt("Revert"))
                elif mymaps.hasKey(usrin[1]):
                    mymaps.revert(usrin[1], buildPrompt("Revert"))
                else:
                    print "Could not find {0}".format(usrin[1])
            elif usrin[0] == "preserve" or usrin[0] == "p":
                if usrin[1] == "all":
                    mymaps.preserveAll(buildPrompt("Preserve"))
                elif mymaps.hasKey(usrin[1]):
                    mymaps.preserve(usrin[1], buildPrompt("Preserve"))
                else:
                    print "Could not find {0}".format(usrin[1])
            elif usrin[0] == "update" or usrin[0] == "u":
                if usrin[1] == "all":
                    mymaps.updateAll()
                elif mymaps.hasKey(usrin[1]):
                    mymaps.update(usrin[1])
                else:
                    print "Could not find {0}".format(usrin[1])
            else:
                print "Please input a valid command"
        else:
            print "Too many arguments"
        raw_input()

main()

#proceed = True
#while proceed:
#    print "--------------------"
#    print "The following mappings are defined in {0}:".format(xFilename)
#    for k, v in mappingDict.items():
#        print "{0:>20} : {1:20} {3} {2}".format(k, v.reponame, v.destination, v.getArrow())
#        (rtime, dtime) = v.times()
#        print "                       {0:20}    {1}" .format( \
#            time.strftime("%b %d %Y %H:%M:%S", time.gmtime(rtime)), \
#            time.strftime("%b %d %Y %H:%M:%S", time.gmtime(dtime)))
#        print "                       --------------------------------------------------------"
#    print "Input a tagname to perform the operation, or e(x)it, (a)ll, (p)ush"
#    usercmd = raw_input('>> ')
#    if usercmd == 'x':
#        proceed = False
#    elif usercmd == 'a':
#        for _, v in mappingDict.items():
#            v.update()
#    elif usercmd == 'p':
#        print 'Do p here'
#    elif usercmd == '':
#        print 'Please input a command'
#    else:
#        #Set the stuff
#        if len(usercmd.split()) == 1:
#            settingname = usercmd
#            revert = False
#        elif len(usercmd.split()) == 2:
#            if usercmd.split()[0] == 'revert' or usercmd.split()[0] == 'r':
#                settingname = usercmd.split()[1]
#                revert = True
#            else:
#                print 'invalid command'
#        #Do the stuff
#        if settingname in mappingDict.keys():
#            mappingDict[settingname].update(revert=revert)
#        else:
#            print 'invalid command'
#                
#    if usercmd != 'x':
#        raw_input()
#
