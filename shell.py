from subprocess import Popen, PIPE
from os import chdir


class Commander():
    def __init__(self,cmd):
        self.to_exec = cmd.split()
        self.stderr = PIPE 
        self.stdout = PIPE     
    def chdir(self):
        if len(self.to_exec) > 2:
            self.stderr = "to manny args"
        elif len(self.to_exec):
            pass
        else:
            os.chdir(self.to_exec[1])
    def out(self):
        if self.to_exec[0] == 'cd':
            self.chdir()
        else:
            try:
                process = Popen(self.to_exec,stdout=PIPE, stderr=PIPE)
                self.stdout, self.stderr = process.communicate()
            except FileNotFoundError:
                self.stdout = None
                self.stderr = "no such file or directory"
        return (self.stderr, self.stderr)

