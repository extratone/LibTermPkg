"""
usage: sleep seconds
"""

from sys import argv
from time import sleep

if len(argv) == 1:
    print("usage: sleep seconds")
else:
    sleep(float(argv[1]))
