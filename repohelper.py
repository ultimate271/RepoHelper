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

