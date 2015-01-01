# build script

import subprocess, shutil, os

# delete everything above
entries = os.listdir("..")
entries = list(set(entries) ^ {"src"}) # do not delete ourselves
for entry in entries:
    if os.path.isfile(entry):
        os.remove("../" + entry)
    else:
        shutil.rmtree("../" + entry)
        
# copy all files upwards
entries = os.listdir()
for entry in entries:
    if os.path.isfile(entry):
        shutil.copy(entry, "..")
    else:
        shutil.copytree(entry, "../" + entry)
        
# file-replace
os.chdir("..")
subprocess.call(["python" ,"file-replace.py", "buildReplace"])

print("Build finisished: " + os.getcwd())