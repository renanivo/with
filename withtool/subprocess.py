import subprocess


def run(command):
    try:
        subprocess.check_call(command, shell=True)
    except:
        pass
