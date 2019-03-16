import subprocess


print("Linux!")

subprocess.Popen(['docker', 'version']).communicate()
