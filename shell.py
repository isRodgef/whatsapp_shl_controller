from subprocess import Popen, PIPE
import os



class Commander():
    def __init__(self,cmd):
        self.to_exec = cmd.split()
        self.stderr = PIPE 
        self.stdout = PIPE
        self.pwd = os.getcwd()
        self.oldpwd = None
    def chdir(self):
        if len(self.to_exec) > 2:
            self.stderr = "to manny args"
        elif len(self.to_exec) == 1:
            return
        else:
            if self.to_exec == os.getcwd():
                return
            if self.to_exec[1] == '-':
                os.chdir(self.oldpwd)
                return  
            os.chdir(self.to_exec[1])
            if self.pwd != os.getcwd():
                self.oldpwd = self.pwd
                self.pwd = os.getcwd
    def out(self):
        if self.to_exec[0] == 'cd':
            self.chdir()
        elif self.to_exec[0] != 'cd':
            try:
                process = Popen(self.to_exec,stdout=PIPE, stderr=PIPE)
                self.stdout, self.stderr = process.communicate()
            except FileNotFoundError:
                self.stdout = None
                self.stderr = "no such file or directory"
        return (self.stdout, self.stderr)

