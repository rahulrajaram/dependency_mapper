import subprocess


print("windows!")

subprocess.Popen(['docker', 'version']).communicate()
