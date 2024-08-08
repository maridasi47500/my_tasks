import subprocess
import os
from fichier import Fichier
class Scriptpython:
    def __init__(self,name):
        self.name=name
    def lancer(self):
        x=subprocess.check_output(["sh","./uploads/lancer_"+self.name.replace(".","")+".sh"])
        return x
    def lancer1(self):
        matermin=self.name.split(".")[-1]
        myprogram=""
        if matermin == "rb":
            myprogram="ruby"
        if matermin == "php":
            myprogram="php"
        if matermin == "py":
            myprogram="python3"
        wow=self.name.rfind("/")
        monfichier=Fichier("./uploads","lancer_"+self.name.replace("/","").replace(".","")+".sh").ecrire("""xterm -l -hold -e "cd {myroot}{myname} && echo \\\"c'est  mon script\\\" && bash -l -c \\\"{program} ./{name}\\\""
                """.format(myroot=os.getcwd(),myname=self.name[0:(wow)].replace(".",""), name=self.name[(wow+1):],program=myprogram))
        x=subprocess.check_output(["sh","./uploads/lancer_"+self.name.replace("/","").replace(".","")+".sh"])

        return x

