import os

version = "0.0.1"
print("kkShell", version)

uname = os.getlogin()

print(uname + " @ " + "kkShell")

cwd = "/usr/"

if os.name == "nt":
    ostype = "win"
elif os.name == "posix":
    ostype = "nix"

winud = "C:\\Users\\" + uname
winualias = {
    "/usr/": winud,
    "/etc/": "C:\\Windows",
    "/bin/": "C:\\Program Files"
}

print(ostype)

def getfiles(wd):
    files = os.listdir(wd)

    files = [f for f in files if os.path.isfile(wd+'/'+f)]
    return files

def getdirs(wd):
    dirs = os.listdir(wd)

    dirs = [f for f in dirs if os.path.isdir(wd+'/'+f)]
    return dirs

def cd(dir):
    global winualias
    global cwd
    if dir in winualias.keys():
        cwd = winualias[dir]
    else:
        cwd = dir