"""
No code here, just take it slow and review a bit:

what I have highlighted in PDF:

1. Escape Sequences (ex10)
\v vertical tab
\t horizontal tab


2. In terminal, type this:
python3 -m pydoc "Some_Function_Name" --> Get manual

echo "String to the new file" > new_file.txt --> Create txt file
cat new_file.txt --> peek on a file
man cat --> Help on the keyword "cat"


3. File functions (ex16)
truncate (maybe not that useful)
seek(0)
tell()


4. Check whether file exist (ex17)
from os.path import exists
exists(file_name) --> return boolean, True/False


5. Do I need close file? (ex17)
open(from_file).read() --> no need to drop
# python already drop once this line runs! Cool stuff.


6. Func variable and global variable has same name? (ex19)
It's BAD!!! try to avoid


7. Limit function input into 5 arguments! (At least try to)

"""