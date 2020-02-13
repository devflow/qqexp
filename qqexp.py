from os import listdir, path, rename
from os.path import isfile, join, splitext
from sys import argv, exit

original_header = [71, 72, 70, 57, 57, 96]
fixed_header = [71, 73, 70, 56, 57, 97]

if len(argv) < 2:
    exit("please set target dir path.")

path = argv[1]

print("starting convert... target dir : {}".format(path))

lst = []

for f in listdir(path):
    filename, file_extension = splitext(f)
    if isfile(join(path, f)) and file_extension == "":
        lst.append(f)

print("collected {} files".format(len(lst)))

for f in lst:
    fn = join(path, f)
    fdn = f
    f = open(fn, 'r+b')
    header = list(bytes(f.read(6)))

    if header == original_header:
        f.seek(0)
        f.write(bytes(fixed_header))
        f.close()

        rename(fn, fn + ".gif")

        print("{} : Done.".format(fdn))
    else:
        print("{} : Invalid Header.".format(fdn))
        f.close()
    
print("finished.")
