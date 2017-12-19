
import os
import shutil

fromdir = "testdir1"
todir = "testdir2"

files = os.listdir(fromdir)

for i in files:
	shutil.move(os.path.join(fromdir, i), todir)
	print("Moved {} from {} to {}".format(i, fromdir, todir))