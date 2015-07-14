import os, sys

def sortFiles(img_dir, chunks):
    for root, dirs, files in os.walk(img_dir):
        folderDict={}
        for i in range(len(files)):
            try:
                folderDict[files[i].split("_")[0]].append(files[i])
            except:
                folderDict[files[i].split("_")[0]] = [files[i]]

        #
        chunk_sequencer = 0

        # organize the files
        for i, key in enumerate(folderDict):

            chunk_sequencer += (i%chunks == 0) and 1 or 0

            path = os.path.join(img_dir, str(chunk_sequencer) + os.sep + key)

            os.makedirs(path)

            for subfile in folderDict[key]:
                oldPath = os.path.join(img_dir, subfile)
                newPath = os.path.join(path, subfile)
                try:
                    os.rename(oldPath, newPath)
                except:
                    pass
                    print; print oldPath
                    print newPath




if __name__ == "__main__":

    if len(sys.argv) < 2:
        print 'ERR: Please provide the images directory.'
        sys.exit()

    # get full path
    directory = os.path.abspath(sys.argv[1])

    #
    sortFiles(directory, 10)
