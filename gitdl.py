# gitdl command - to download gists/repos
# ©️ Ong Yong Xin/jsbain, 2014-2019
# Under the Unlicense.

# Original code (from GitHubGet) machine-translated to Python 3.7 using pythonconverter.com.

import urllib.request, urllib.parse, urllib.error, zipfile, sys, functools, re, os, tempfile, json, requests

# Define split function.
def split(strng, sep, pos):
    strng = strng.split(sep)
    return sep.join(strng[:pos]), sep.join(strng[pos:])

# Check if url is a gist (copied from ywangd: https://github.com/ywangd/psiclient/blob/master/psiclient.py)
def is_gist(url):
    match = re.match('http(s?)://gist.github.com/([0-9a-zA-Z]*)/([0-9a-f]*)', url)
    return match

# Actual downloading
def dl_gist():
    if is_gist(sys.argv[2]):
        print("\nOK: URL is a gist.")
        # Download gist using /raw at end of url
        print("\nGetting gist name...")
        gistfile = requests.get(sys.argv[2] + "/raw")
        if gistfile:
            gist_id = split(sys.argv[2], "/", 4)
            # Get gist filename from json
            gistfile_info = requests.get("https://api.github.com/gists/" + gist_id[-1]).content
            # Load json list into dict
            gistfile_d = json.loads(gistfile_info)
            filelist = []
            # Get filename from dict
            for key in gistfile_d["files"]:
                filelist.append(key)
            # Get user name for foler to store gists
            username = gistfile_d["owner"]["login"]
            # Make folder to store gists according to user.
            if os.path.isdir(username):
                print("\nN: Username dir already exists.")
            else:
                os.mkdir(username)
            # Check if gist contains muitiple files.
            if len(filelist) == 1:
                # Download the gist.
                print("\nDownloading gist...")
                gistfile_p = os.path.expanduser("./" + username + "/" + filelist[0])
                with open(gistfile_p, "wb") as f:
                    gist_r = requests.get(sys.argv[2] + "/raw")
                    f.write(gist_r.content)
                print("Done.")
            else:
                print("\nN: Gist contains muitiple files.\nDownloading gist (muitiple files)...")
                for key in gistfile_d["files"]:
                    url_tmp = gistfile_d["files"][key]["raw_url"]
                    gistfile_p = os.path.expanduser("./" + username + "/" + key)
                    with open(gistfile_p, "wb") as f:
                        gist_r = requests.get(url_tmp)
                        f.write(gist_r.content)
                print("\nDone.")
    else:
        print("\nE: URL is not a gist!")
# jsbain's orginal code starts from here.
def extract_git_id(git):
    print(git)
    m = re.match((r'^http(s?)://([\w-]*\.)?github\.com/(?P<user>[\w-]+)/(?P<repo>[\w-]*)'
                 '((/tree|/blob)/(?P<branch>[\w-]*))?'), git)
#    print m.groupdict()
    return m
    
def git_download_from_args(args):
    if len(args) == 3:
        url = args[2]
        git_download(url)


def dlProgress(filename, count, blockSize, totalSize):
    if count*blockSize > totalSize:
        percent=100
    else:
        percent = max(min(int(count*blockSize*100/totalSize),100),0)
    sys.stdout.write("\r" + filename + "...%d%%" % percent)
    sys.stdout.flush()

def git_download(url):
    base='https://codeload.github.com'
    archive='zip'
    m=extract_git_id(url)
    if m:
        g=m.groupdict()
        if not g['branch']:
            g['branch']='master'

        u=   '/'.join((base,g['user'],g['repo'],archive, g['branch']))
        #print u
        try:
            with tempfile.NamedTemporaryFile(mode='w+b',suffix='.zip') as f:
                urllib.request.urlretrieve(u,f.name,reporthook=functools.partial(dlProgress,u))
                z=zipfile.ZipFile(f)
                z.extractall()
                print(z.namelist())
        except:
            print('E: git url did not return zip file')
    else:
        print('E: could not determine repo url from argv')
        
# Define main function.
def main():
    if len(sys.argv) == 3:
        if sys.argv[1] == "-repo":
            git_download_from_args(sys.argv)
        elif sys.argv[1] == "-gist":
            dl_gist()
        else:
            pass
    elif len(sys.argv) == 2:
        print("\nE: No repo/gist url provided.\nusage: gitdl -[repo/gist] [repourl/gisturl]")
    elif len(sys.argv) == 1:
        print("\ngitdl: the easy way to download stuff from github.\nusage: gitdl -[repo/gist] [repourl/gisturl]\n")

if __name__=='__main__':
    main()