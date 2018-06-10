## 1. Description

---------

Simple tool to draw the header-file dependency map of your C/C++ project
  - output will include only header specifications delimited by '`"`'
  - i.e. header files delimited by '`<`|`>`' will be eliminated as they are not core parts of your project. 

-------

## 2. Installation

------------------

```
git clone https://github.com/rahulrajaram/dependency_mapper.git && cd dependency_mapper && pip install . && cd ..
```

------------------

## 3. Usage

-------

```sh
# view help/usage text
dependency_mapper --help

# find all mappings of all source files within the directory;
# might include unwanted output like iles/om  test/ directory
cd <path/to/project/source>
dependency_mapper

# find all mappings within a specific directories, say, 'src/' and 'include/'
dependency_mapper -p src include

# additionally extract directives specified in the '</>' format
dependency_mapper -p src -s

# find all mappings within a specific directory, say, 'src/'
dependency_mapper -p src

# find all mappings within a specific directory, say, 'src/'
# AND highlight a set of files, say, 'main.cpp', and 'utils.h'
dependency_mapper -p src -hl main.cpp utils.h

# find all mappings within a specific directory, say, 'src/'
# AND highlight a set of files, say, 'main.cpp', and 'utils.h'
# AND strip out output that does not contain 'main.cpp' and 'utils.h'
dependency_mapper -p src -hl main.cpp utils.h -c
```

-------

## 4. Sample Output

--------------
```
+-------------+--------------------+
| bar.h       | foo.h              | 
+-------------+--------------------+
| baz.h       | bar.h              |
|             | foo.h              |
+-------------+--------------------+
| main.cpp    | baz.h              | 
+-------------+--------------------+
```
