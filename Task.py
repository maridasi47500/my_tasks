
from script import Script
from fichier import Fichier
dbScript=Script()
# import required module
import os
# assign directory
directory1 = './answers'
directory2 = './examples'
directory3 = './exercises'
 
# iterate over files in
welcome="<h1>Become 1 network engineer</h1>"
welcome+="<div class=\"home\">"
welcome+="<h2>"+directory1+"</h2>"
# that directory
for filename in os.listdir(directory1+'/'):
    f = os.path.join(directory1, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
    else:
        print(f)
        welcome+="\n<h3>"+f.split("/")[-1]+"</h3>"
        g = os.path.join(f, "/")
        for fname in os.listdir(f+'/'):
            h = os.path.join(f, fname.split("/")[-1])
            # checking if it is a file
            if os.path.isfile(h) and h.endswith(".py"):
                print(h)
                x=h.rfind("/") + 1
                name=h[x:(len(h) - 3)]
                k=dbScript.create({"name":name,"file":h})
                welcome+="\n<a id=\"monscript"+str(k["script_id"])+"\" href=\"/script/"+str(k["script_id"])+"\">"+name+"</a>"
                
            else:
                print(h)
welcome+="<h2>"+directory2+"</h2>"
for filename in os.listdir(directory2+'/'):
    f = os.path.join(directory2, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
    else:
        print(f)
        welcome+="\n<h3>"+f.split("/")[-1]+"</h3>"
        g = os.path.join(f, "/")
        for fname in os.listdir(f+'/'):
            h = os.path.join(f, fname.split("/")[-1])
            # checking if it is a file
            if os.path.isfile(h) and h.endswith(".py"):
                print(h)
                x=h.rfind("/") + 1
                name=h[x:(len(h) - 3)]
                k=dbScript.create({"name":name,"file":h})
                welcome+="\n<a id=\"monscript"+str(k["script_id"])+"\" href=\"/script/"+str(k["script_id"])+"\">"+name+"</a>"
                
            else:
                print(h)
welcome+="<h2>"+directory3+"</h2>"
for filename in os.listdir(directory3+'/'):
    f = os.path.join(directory3, filename)
    # checking if it is a file
    if os.path.isfile(f):
        print(f)
    else:
        print(f)
        welcome+="\n<h3>"+f.split("/")[-1]+"</h3>"
        g = os.path.join(f, "/")
        for fname in os.listdir(f+'/'):
            h = os.path.join(f, fname.split("/")[-1])
            # checking if it is a file
            if os.path.isfile(h) and h.endswith(".py"):
                print(h)
                x=h.rfind("/") + 1
                name=h[x:(len(h) - 3)]
                k=dbScript.create({"name":name,"file":h})
                welcome+="\n<a id=\"monscript"+str(k["script_id"])+"\" href=\"/script/"+str(k["script_id"])+"\">"+name+"</a>"
                
            else:
                print(h)

welcome+="</div>"
print(welcome)
Fichier("./welcome","home.html").ecrire(welcome)
