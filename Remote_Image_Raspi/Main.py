import platform
import os

def path_to_file(file):
    for r,d,f in os.walk(os.getcwd()):
        for files in f:
             if files == file:
                 print(f"Found file {file} in path {os.path.join(r,files)}")
                 return os.path.join(r,files)

if __name__ == '__main__':

    if platform.system() == "Linux":
        exec(open(path_to_file('raspi_main.py')).read())

    elif platform.system() == 'Windows':
        exec(open(path_to_file('remote_main.py')).read())

    else:
        print(f"Can't run files on the system {platform.system()}")