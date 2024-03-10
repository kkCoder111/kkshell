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

def getfiles(wd):
    files = os.listdir(wd)

    files = [f for f in files if os.path.isfile(wd+'/'+f)]
    return files

def getdirs(wd):
    dirs = os.listdir(wd)

    dirs = [f for f in dirs if os.path.isdir(wd+'/'+f)]
    return dirs

def cd(dir):
    global cwd_files
    global cwd_dirs
    global winualias
    global cwd
    global nix_path
    if dir != " ":
        if dir in winualias.keys():
            cwd = winualias[dir]
        elif dir[0] == "/" and ostype == "win":
            olddrive = dir[0:3]
            newdrive = dir[1] + ":\\"
            dir = dir.replace(olddrive, newdrive)
            cwd = dir
        else:
            cwd = dir
        cwd_files = getfiles(cwd)
        cwd_dirs = getdirs(cwd)

        nix_path = cwd

        if ":\\" in cwd:
            drive = cwd[0]
            olddrive = drive + ":\\"
            newdrive = "/" + drive + "/"
            nix_path = nix_path.replace(olddrive, newdrive)
        if "\\" in cwd:
            nix_path = nix_path.replace("\\", "/")
    else:
        print("cd - no directory was specified")

def ld(dummy):
    print("Files in", cwd + ":")
    print(cwd_files)
    print(" ")
    print("Directories in", cwd + ":")
    print(cwd_dirs)
    print(" ")
    if dummy != " ":
        print("note: ld takes no arguments; at least one was specified by user")

def interpret(command):
    cmd = command[0].lower()
    args = command[1:]
    args = "".join(args)

    if cmd in commands.keys():
        if len(command) != 1:
            toexec = cmd + "('" + args + "')"
            exec(toexec)
        else:
            toexec = cmd + "(" + "' '" + ")"
            exec(toexec)
    else:
        print("Command not found: " + cmd)

cd(cwd)

commands = {
    "cd": cd,
    "ld": ld
}

command = input(nix_path + " $ ")
command = command.split(" ")
while command[0].lower() != "exit":
    interpret(command)
    command = input(nix_path + " $ ")
    command = command.split(" ")