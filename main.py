import tarfile
import os
import sys

def extract(fname):
    if (fname.endswith("tar.gz")):
        tar = tarfile.open(fname, "r:gz")
        tar.extractall()
        return tar
    elif (fname.endswith("tar")):
        tar = tarfile.open(fname, "r:")
        tar.extractall()
        return tar

if __name__ == '__main__':
    filename = "genres.tar.gz"
    directory = os.getcwd()
    if not os.path.exists(filename.split(".")[0]):
        file = extract(filename)
        print("File extracted to", os.getcwd())
    else:
        print("File exists in", os.getcwd())
    genres = os.listdir(os.path.join(os.getcwd(), filename.split(".")[0]))
    print(genres)
    c = int(input("Convert to wav [0:No 1:Yes]: "))
    if not c:
        print("Done")
        sys.exit(0)
    else:
        genre_dirs = [os.path.join(os.path.join(os.getcwd(), filename.split(".")[0], g)) for g in genres]
        # print(genre_dirs)
        for genre in genre_dirs:
            # print(os.path.normpath(genre))
            for file in os.listdir(os.path.normpath(genre)):
                # print(file)
                # print(os.path.exists(os.path.join(os.path.normpath(genre), file)))
                
