# Script to copy whole tree to a test directory
#
# This is done to check that the site can work under a directory. This also
# allows people to work on the site while they have a working copy somewhere
# else.

import subprocess, shutil, os, sys

DIR = "test-directory"

# delete DIR
if os.path.isdir(DIR): # if it exists and is a directory
    shutil.rmtree(DIR)
elif os.path.isfile(DIR):
    os.remove(DIR)    

# copy all files to DIR
shutil.copytree(".", DIR, ignore=shutil.ignore_patterns(".git"))

print("Local build finisished: " + os.getcwd())

startServer = input("Start a new server to test? (y/n, default yes) ") or "y"
if startServer.lower().startswith("y"):
    print("Navigate to localhost:<port>/" + DIR)
    subprocess.call(["python", "-m", "http.server"])