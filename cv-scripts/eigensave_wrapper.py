import os, sys

def schedule_jobs(path):
    dirList = os.listdir(path)
    for i in dirList:
        cmd = 'python eigensave.py detected'+os.sep+i
        os.system(cmd)
        print 'done: ' + i
    pass

if __name__ == "__main__":

    if len(sys.argv) < 2:
        print 'ERR: Please provide the images directory.'
        sys.exit()

    # get full path
    directory = os.path.abspath(sys.argv[1])

    # run jobs
    schedule_jobs(directory)

    # notify me here...
    
