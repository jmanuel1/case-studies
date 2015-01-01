# local build script

import subprocess, shutil, os, sys

# delete everything in localbuild
if os.path.isdir("localbuild"): # if it exists and is a directory
    shutil.rmtree("localbuild")
elif os.path.isfile("localbuild"):
    os.remove("localbuild")    

# copy all files to localbuild
shutil.copytree(".", "localbuild")
        
# file-replace
os.chdir("localbuild")
subprocess.call(["python", "file-replace.py", "localReplace"], stdout=sys.stdout)

print("Local build finisished: " + os.getcwd())

startServer = input("Start a new server to test? (y/n, default yes) ")
if startServer.lower().startswith("y"):
    subprocess.call(["python", "-m", "http.server"])