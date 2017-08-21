import os.path
import shutil

class FileMapping:
    def __init__(self, reponame, destination):
        self.reponame = reponame
        self.destination = destination

    def times(self):
        #returns a pair (repotime, desttime) 
        #    with the last updated times of each file.
        repotime = os.path.getmtime(self.reponame) or 0.0
        desttime = os.path.getmtime(self.destination) or 0.0
        return (repotime, desttime)

    def revert(self, prompt=lambda x,y: True):
        if prompt(self.reponame, self.destination):
            shutil.copyfile(self.reponame, self.destination)

    def preserve(self, prompt=lambda x,y: True):
        if prompt(self.destination, self.reponame):
            shutil.copyfile(self.destination, self.reponame)

    def update(
            self, 
            revertPrompt=lambda x,y: True,
            preservePrompt=lambda x,y: True,
            error=lambda: None):
        (rtime, dtime) = self.times()
        if (rtime, dtime) == (0.0, 0.0):
            error()
        elif dtime < rtime:
            self.revert(revertPrompt)
        elif rtime > dtime:
            self.preserve(preservePrompt)

    def which(self):
        (r, d) = self.times()
        if d < r:
            return "revert"
        elif r < d:
            return "preserve"
        else:
            return ""
