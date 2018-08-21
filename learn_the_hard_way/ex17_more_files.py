from sys import argv
from os.path import exists
# exists() check path

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# combining open and read into 1 line
with open(from_file) as f:
    indata = f.read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit Return to continue, CTRL-C to abort.")
input("> ")

out_file = open(to_file, 'w')  # 'w' erases old one. 'a' writes from the end.
out_file.write(indata)

print("Alright, all done.")

out_file.close()

# try 1 line
open("try_1_line_"+to_file, 'w').write(open(from_file).read())
