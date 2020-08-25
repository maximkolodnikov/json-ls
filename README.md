# json-ls

Test tool for recursive directory representation in JSON format.

Leaf nodes - files of type 'txt' or 'bin' with name and size printed. 
Txt-typed files have size as number of lines, bin-typed files have size parameter as the size of the file in bytes.

Intermediate nodes are simply directory names.

``dir1`` contains test file structure.

## Usage
``rootDir`` - root directory for representation. Used current location if none specified.
```
python json_ls.py <rootDir>
```
