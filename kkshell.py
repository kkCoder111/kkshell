import os
import json

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

alias_file_name = "aliases.json"

alias = open("aliases.json", mode="r")
alias_w = open("aliases.json", mode="w")

aliases = json.dumps(alias.read())

del aliases["dummy"]

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
    global path_snapshot
    try:
        if dir != " " and dir != "..":
            if dir in winualias.keys():
                cwd = winualias[dir]
            elif dir[0] == "/" and ostype == "win":
                olddrive = dir[0:3]
                newdrive = dir[1] + ":\\"
                dir = dir.replace(olddrive, newdrive)
                dir = dir.replace("/", "\\")
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
                nix_path = nix_path.replace("//", "/")
            if "\\" in cwd:
                nix_path = nix_path.replace("\\", "/")
            path_snapshot = cwd
        elif dir == "..":
            path_split = nix_path.split("/")
            path_split.remove(path_split[len(path_split)-1])
            path_split = "/" + "/".join(path_split)
        elif dir == "-d":
            pwd(dir)
        else:
            print("error - no directory was specified")
    except FileNotFoundError:
        try:
            if ostype == "win":
                dir = dir.replace("/", "")
                dir = dir.replace("\\", "")
                todir = path_snapshot + "\\" + dir
            elif ostype == "nix":
                dir = dir.replace("/", "")
                dir = dir.replace("\\", "")
                todir = path_snapshot + "/" + dir
            cd(todir)
        except OSError:
            print("cd - cannot find path '" + dir + "'")
    finally:
        nix_path = nix_path.replace("//", "/")

def ld(arg):
    if arg == " ":
        print("Files in", nix_path + ":")
        print(cwd_files)
        print(" ")
        print("Directories in", nix_path + ":")
        print(cwd_dirs)
        print(" ")
    elif arg.lower() == "-f":
        print("Files in", nix_path + ":")
        print(cwd_files)
        print(" ")
    elif arg.lower() == "-d":
        print("Directories in", nix_path + ":")
        print(cwd_dirs)
        print(" ")
    else:
        print("Invalid option:", arg)
def s(arg):
    if ostype == "nix":
        print("s is not currently available on Linux")
    else:
        tostart = "start " + arg
        os.system(tostart)

def install(arg):
    if ostype == "nix":
        print("install is only available on Windows")
    else:
        todo = "winget install " + arg
        os.system(todo)
def uninstall(arg):
    if ostype == "nix":
        print("uninstall is only available on Windows")
    else:
        todo = "winget uninstall " + arg

def dci(arg):
    if arg != " " or arg != "":
        os.system(arg)
    else:
        print("dci: no command was specified")
def pwd(dummy):
    print("True working directory:", cwd)
    print("Unix-like working directory (Windows only):", nix_path)
    if dummy != " " or dummy != "":
        print("Note: this command takes no attributes")

def d(path):
    cd(path)

def al(alias):
    alias.split("=")
    alias_name = alias[0]
    alias_contents = alias[1]
    aliases[alias_name] = alias_contents


def interpret(command):
    cmd = command[0].lower()
    args = command[1:]
    args = " ".join(args)

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
    "ld": ld,
    "s": s,
    "install": install,
    "uninstall": uninstall,
    "dci": dci,
    "pwd": pwd,
    "d": d
}

command = input(nix_path + " $ ")
command = command.split(" ")
while command[0].lower() != "exit":
    interpret(command)
    command = input(nix_path + " $ ")
    command = command.split(" ")