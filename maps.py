import xml.etree.ElementTree as ET
from filemapping import FileMapping

def buildDict (root, repodir=""):
    #creates a dictionary based on the children of root with tag "setting"
    retVal = {}
    for child in root:
        if child.tag == "setting":
            key = child.find('name').text
            newfm = FileMapping(
                repodir + "/" + child.find('reponame').text,
                child.find('destination').text)
            if key in retVal:
                retVal[key].append(newfm)
            else:
                retVal[key] = [newfm]
    return retVal

class Maps:
    def __init__(self, settingsFilename):
        root = ET.parse(settingsFilename).getroot()
        self.repodir = root.find("repodir").text or ""
        self.fileMappings = buildDict(root, repodir=self.repodir)

    def revert(self, key, prompt=lambda x,y: True):
        for fm in self.fileMappings[key]:
            fm.revert(prompt=prompt)

    def preserve(self, key, prompt=lambda x,y: True):
        for fm in self.fileMappings[key]:
            fm.preserve(prompt=prompt)

    def update(
            self,
            key,
            revertPrompt   = lambda x, y: True,
            preservePrompt = lambda x, y: True,
            error          = lambda: None
        ):
        for fm in self.fileMappings[key]:
            fm.update(
                revertPrompt   = revertPrompt,
                preservePrompt = preservePrompt,
                error          = error
            )

    def revertAll(self, prompt=lambda x,y: True):
        for k in self.fileMappings:
            fileMappings[k].revert(prompt)

    def preserveAll(self, prompt=lambda x,y: True):
        for k in self.fileMappings:
            fileMappings[k].revert(prompt)
            
    def updateAll(
            self,
            revertPrompt   = lambda x, y: True,
            preservePrompt = lambda x, y: True,
            error          = lambda: None
        ):
        for k in self.fileMappings:
            self.fileMappings[k].update(
                revertPrompt   = revertPrompt,
                preservePrompt = preservePrompt,
                error          = error
            )

    def printOption(self, key):
        print "{0}".format(key)
        for fm in self.fileMappings[key]:
            print "\tRepo : {0}".format(fm.reponame)
            print "\tDest : {0}".format(fm.destination)
            print ''

    def printMenu(self):
        for k in self.fileMappings:
            self.printOption(k)

    def hasKey(self, key):
        for k in self.fileMappings:
            if key == k:
                return True
        return False
