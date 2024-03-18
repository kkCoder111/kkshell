import requests
import sys
import urllib.request as request
import socket
import os
import sys

version = float(open("version.txt").read())

def internet_on():
    try:
        request.urlopen('http://github.com', timeout=1)
        return True
    except request.URLError or requests.exceptions.NewConnectionError or requests.exceptions.ConnectionError or socket.gaierror: 
        return False

def get(file, headers):
    return requests.get(file, headers=headers).text
if not internet_on():
    print("Not connected to the internet")
else:
    server_version = requests.get("https://raw.githubusercontent.com/kkCoder111/kkshell/main/version.txt")

    server_version = float(server_version.text)

    if server_version > version:
        print("Update available: " + str(server_version))
        print("Current version is: " + str(version))
        yes = input("Update now? [Y/N]:")
        if yes == "Y":
            print("Updating to version " + str(server_version))
            print("1/3: Removing existing files")
            os.remove("kkshell.py")
            os.remove("help.py")
            os.remove("version.txt")
            print("2/3: Getting updated files")
            headers = { 'User-Agent': 'Mozilla/5.0 (Windows NT 6.0; WOW64; rv:24.0) Gecko/20100101 Firefox/24.0' }
            new_main = get("https://raw.githubusercontent.com/kkCoder111/kkshell/main/kkshell.py", headers=headers)
            new_help = get("https://raw.githubusercontent.com/kkCoder111/kkshell/main/help.py", headers=headers)
            new_ver = get("https://raw.githubusercontent.com/kkCoder111/kkshell/main/version.txt", headers=headers)
            print("3/3: Apply changes")
            open("kkshell.py", mode="w").write(str(new_main))
            open("help.py", mode="w").write(str(new_help))
            open("version.txt", mode="w").write(str(new_ver))
            print("Done. Restart kkShell to see the changes. Press ENTER to continue")
            input(" ")
            sys.exit()
        else:
            pass

    else:
        print("No updates available")