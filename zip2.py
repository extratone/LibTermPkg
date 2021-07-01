# importing required modules 
import os, sys, zipfile, zlib

# Set global vars and feedback text
helptxt = '\nusage: zip2 -[e/c] [zipfile/file to compress]\n-e, [zipfile]:\n\tExtracts files from a existing zipfile.\n-c, [/path/to/file]:\n\tCompresses specified file/folder into zipfile. The new zip is stored in the current directory.'

# Check for correct options
def getParameters(args):
    if len(args) == 1:
        print(helptxt)
    else:
        arg1_raw = (sys.argv[1])
        return(arg1_raw)

# Get first arguement from params
arg1 = getParameters(sys.argv)
argall = sys.argv
compress_mode = zipfile.ZIP_DEFLATED

# Define function to get filepath of specific directory
def retrieve_file_paths(dirName):
    # setup file paths variable
    filePaths = []
    # Read all directory, subdirectories and file lists
    for root, directories, files in os.walk(dirName):
        for filename in files:
        # Create the full filepath by using os module.
            filePath = os.path.join(root, filename)
            filePaths.append(filePath)
    # return all paths
    return filePaths

# Define compressfile function
def compressfile(filepath):
    # Check if path given is valid
    if os.path.exists(filepath) == True:
        # Check if it is a file or directory
        if os.path.isfile(filepath) == True:
            print("\nN: Path given is a file.")
            print("\nCompressing...")
            # Get filename and use that as a archive name for compressed stuff.
            filename = os.path.basename(filepath) + ".zip"
            if os.path.exists(filepath + ".zip"):
                print("\nW: Archive of file specified already exists.\nOverwriting...")
            with zipfile.ZipFile(filename, 'w') as f:
                f.write(filepath, compress_type=zipfile.ZIP_DEFLATED)
                f.close()
            print("\nDone.")
        else:
            print("\nN: Path given is a directory.")
            print("\nCompressing...")
            # Get filename and use that as a archive name for compressed stuff.
            filename = os.path.basename(filepath) + ".zip"
            if os.path.exists(filepath + ".zip"):
                print("\nW: Archive of file specified already exists.\nOverwriting...")
            # Get filepath of all files in dir
            allfilepaths = retrieve_file_paths(filepath)
            with zipfile.ZipFile(filename, 'w') as f:
                for file in allfilepaths:
                    f.write(file, compress_type=zipfile.ZIP_DEFLATED)
            print("\nDone.")
    else:
        print("\nE: The file/folder does not exist. Try again.")

# Define extractfile function
def extractfile(filepath):
    # Check if path given is valid
    if os.path.exists(filepath) == True:
        # Check if it is a file or directory
        if zipfile.is_zipfile(filepath) == True:
            print("\nOK: Path given is a zipfile.")
            print("\nExtracting...")
            # Get filename and use that as a folder name for extracted stuff.
            filename_r = os.path.basename(filepath)
            # Take only the name.
            filename = filename_r.replace('.zip', '')
            if os.path.exists(filename):
                print("\nN: Temp folder already exists.")
            else:
                os.mkdir(filename)
            with zipfile.ZipFile(filepath, 'r') as zip:
                try:
                    zip.extractall(path=filename)
                except zipfile.BadZipfile:
                    print("\nE: Zip file is bad (corrupted?)\nAbort.")
                except zipfile.BigZipfile:
                    print("\nE: Zip file is too big (Zip64 is not supported.)\nAbort.")
            print("\nSucessfully extracted to folder " + filename + ".\n")
        elif (os.path.isfile(filepath) == True and filepath.endswith(".zip") == False):
            print("\nE: File is not a zipfile \n(It must have extention .zip).\nAbort.")
        else:
            print("\nE: Path given is a directory. Cannot extract.\nAbort.")
    else:
        print("\nE: The file does not exist. Try again.")
       

# Define main func.
def main():
    if len(sys.argv) == 2:
        print("E: No filepath provided.\nUsage: zip2 -[e/c] [/path/to/file]")
    elif len(sys.argv) == 3:
        if sys.argv[1] == "-e":
            extractfile(sys.argv[2])
        elif sys.argv[1] == "-c":
            compressfile(sys.argv[2])
    else:
        print("")


if __name__ == "__main__":
    main()