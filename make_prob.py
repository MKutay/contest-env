#!/usr/bin/env python3

from docopt import docopt
from datetime import datetime
import os
import sys
import http.server
import json
from pathlib import Path
import subprocess
import re

args = sys.argv

today = datetime.today()

print(args)

for i in range(1, len(args)):
    os.system("mkdir " + str(args[i]))
    os.system("cp ~/CP/new_template/* " + str(args[i]) + "/.")
    os.system("rm -rf " + str(args[i]) + "/a.cpp")
    templatef = open("/Users/kty/CP/new_template/a.cpp", 'r')
    template = templatef.read()
    templatef.close()
    date = today.strftime("%d.%m.%Y %H:%M:%S")
    file = """/**
 *  author: MKutayBozkurt
 *  created: """ + date + """
**/
"""
    file += str(template)
    f = open(str(args[i]) + "/a.cpp", "w")
    f.write(file)
    f.close()
