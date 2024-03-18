import os
import json
import help
import sys
try:
    import requests
except:
    if os.name == "nt":
        print("installing dependency")
        os.system("pip install requests")
        print("Done, restart kkShell to see changes. Press ENTER to continue.")
        input(" ")
        sys.exit()
        
    else:
        print("installing dependency")
        os.system("pip3 install requests")
        print("Done, restart kkShell to see changes. Press ENTER to continue.")
        input(" ")
        sys.exit()
import socket
import urllib.request as request

version = float(open("version.txt").read())

#Prints version
print("kkShell", str(version))

def internet_on():
    try:
        request.urlopen('http://github.com', timeout=1)
        return True
    except request.URLError: 
        return False

"""if internet_on():
    server_version = requests.get("https://raw.githubusercontent.com/kkCoder111/kkshell/main/version.txt")
    server_version = float(server_version.text)
    if server_version > version:
        print("Update available! Run 'update' to update.")
else:
    print("Not connected to the internet, so not checking for updates.")"""

#Gets username
uname = os.getlogin()

print(uname + " @ " + "kkShell")

#Sets current working directory
cwd = "/usr/"

#Finds OS, nt for Windows and posix for Unix-like
if os.name == "nt":
    ostype = "win"
elif os.name == "posix":
    ostype = "nix"

winud = "C:\\Users\\" + uname

winualias = {
    "/usr/": winud,
    "~": winud,
    "/etc/": "C:\\Windows",
    "/bin/": "C:\\Program Files"
}

alias_file_name = "aliases.json"

alias = open("aliases.json", mode="r")

aliases = json.loads(alias.read())
alias.close()

try:
    del aliases["dummy"]
except KeyError:
    pass

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
        old_nx = nix_path
    except NameError:
        nix_path = " "
        old_nx = nix_path

    try:
        if dir != " " and dir != ".." and dir != "-d" and dir != "/d":
            if dir in winualias.keys():
                cwd = winualias[dir]
            elif dir[0] == "/" and ostype == "win" and dir[2] == "/":
                olddrive = dir[0:3]
                newdrive = dir[1] + ":\\"
                dir = dir.replace(olddrive, newdrive)
                dir = dir.replace("/", "\\")
                cwd = dir
            else:
                dir = dir.replace("/", "\\")
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

            paths = nix_path.split("/")

            if len(paths[0]) != 1 and len(paths[1]) != 1:
                nix_path = old_nx[0:3] + nix_path

        elif dir == "..":
            path_split = nix_path.split("/")
            path_split.remove(path_split[len(path_split)-1])
            path_split = "/" + "/".join(path_split)
        elif dir == "-d" or "/d":
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
    if arg == " " or arg == "":
        print("Files in", nix_path + ":")
        print(cwd_files)
        print(" ")
        print("Directories in", nix_path + ":")
        print(cwd_dirs)
        print(" ")
    elif arg.lower() == "-f" or arg.lower() == "/f":
        print("Files in", nix_path + ":")
        print(cwd_files)
        print(" ")
    elif arg.lower() == "-d" or arg.lower() == "/d":
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

def d(path):
    cd(path)

def al(alias):
    alias = alias.split("=")
    alias_name = alias[0]
    alias_contents = alias[1]
    aliases[alias_name] = alias_contents
    alias = open("aliases.json", mode="w")
    to_write = json.dumps(aliases)
    alias.write(to_write)
    print("Alias saved.", alias_name, "will trigger", alias_contents, "from now on.")

def cs(dummy):
    if ostype == "win":
        os.system("cls")
    else:
        os.system("clear")

def pyrun(file):
    if ostype == "win":
        torun = "python " + file
        os.system(torun)
    elif ostype == "nix":
        torun = "python3 " + file

def hlp(args):
    if args == " ":
        pyrun("help.py")
    else:
        try:
            todo = "help." + args.lower() + "()"
            exec(todo)
        except SyntaxError:
            help.start()

def update(args):
    pyrun("update.py")

def interpret(command):
    alias_list = list(aliases.keys())
    if len(alias_list) != 0:
        command = " ".join(command)
        for i in alias_list:
            to = aliases[i]
            fr = i
            command = command.replace(fr, to)
        command = command.split(" ")
    cmd = command[0].lower()
    args = command[1:]
    args = " ".join(args)

    if cmd in commands.keys():
        if len(command) != 1:
            if cmd != "help":
                try:
                    toexec = cmd + "('" + args + "')"
                    exec(toexec)
                except SyntaxError as e:
                    print("An error occured while changing paths:")
                    print("ERROR 01: Backslash character")
                    print("This occured because you seperated paths by backslashes. This is not your fault though.")
                    print("Unfortunately, there's not anything that can be done about this code-wise.")
                    print("If you need to use a backslash, please replace it with a double slash ('//'). Thank you.")
            elif cmd == "help":
                toexec = "hlp" + "('" + args + "')"
                exec(toexec)
        else:
            if cmd != "help":
                toexec = cmd + "('" + args + "')"
                exec(toexec)
            elif cmd == "help":
                toexec = "hlp" + "('" + args + "')"
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
    "d": d,
    "al": al,
    "cs": cs,
    "help": hlp,
    #"update": update
}

command = input(nix_path + " $ ")
command = command.split(" ")
while command[0].lower() != "exit":
    interpret(command)
    command = input(nix_path + " $ ")
    command = command.split(" ")