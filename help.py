import os

def all():
    print("NOTE: Some commands may only be available on Windows.")
    print("al - create an alias")
    print("cd - change directory")
    print("cs - clear screen")
    print("d - equivalent of cd")
    print("dci - run command with default command interpreter")
    print("exit - exit kkShell")
    print("help - run this help command, or, get info about a specific command")
    print("install - install an app using WinGet")
    print("ld - list directory")
    print("pwd - print working directory")
    print("s - start an app using Windows CMD")
    print("uninstall - uninstalls an app using WinGet")

def al():
    print("alias [name]=[toexecute]")
    print("This command creates an alias")
    print("name - the name of the alias")
    print("toexecute - what to execute")

def cd():
    print("cd [/d] [path]")
    print("This command changes directory, or if using option /d, prints working directory")
    print("/d - prints working directory")
    print("path - the path to change to, only if not using /d")

def cs():
    print("cs (no options)")
    print("Clears the screen")

def d():
    cd()

def dci():
    print("dci [command]")
    print("Runs a command using the default command interpreter")
    print("command - the command or command(s) to execute using the default command interpreter")

def exit():
    print("exit (no parameters)")
    print("Exits kkShell")

def help():
    print("help [command]")
    print("Runs this interactive help program if no command specified")
    print("command - the command to receive information about. Bypasses interactive help program if no command specified. If equal to 'all', the command will print information about all commands")

def install():
    print("install [app]")
    print("Installs an app using WinGet")
    print("app - the app to install")

def ld():
    print("ld [-d] [-f]")
    print("Lists all subdirectories in directory if using -d")
    print("Lists all files in directory if using -f")
    print("If neither option is used, lists all subdirectories AND files in directory")

def pwd():
    print("pwd (no options)")
    print("Prints working directory")

def s():
    print("s [app]")
    print("Starts an app using Windows CMD")
    print("app - the app to start")

def uninstall():
    print("uninstall [app]")
    print("Uninstalls an app using WinGet")
    print("app - the app to uninstall")
    
def s():
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    print("Welcome to the interactive help program!")

    print("Type 'all' for a list of commands, or, enter a command's name to receive help on that command.")
    print("To exit, type 'x'")
    inp = input("help>")

    while inp.lower() != "x":
        print("\n")
        todo = inp.lower()
        todo = todo + "()"
        try:
            exec(todo)
        except NameError:
            print("That wasn't a valid command")
            print("Type 'all' for a list of commands, or, enter a command's name to receive help on that command.")
            print("To exit, type 'x'")
        inp = input("help>")
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")