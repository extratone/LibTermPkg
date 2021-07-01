import sys
import zipfile
import os

try:
    if os.path.isfile(sys.argv[1]):
        try:
            with zipfile.ZipFile(sys.argv[1], 'r') as zip_ref:
                zip_ref.extractall(sys.argv[1][:-4])
        except Exception as e:
            print("Terminated with exception " + str(e))
    else:
        print("File wasn't found!")
except IndexError:
    print("Usage: unzip <zip_file>")
