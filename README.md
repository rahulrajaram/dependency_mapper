## 1. Description

---------

Simple tool to draw the header-file dependency map of your C/C++ project
  - output will include only header specifications delimited by '`"`'
  - i.e. header files delimited by '`<`|`>`' will be eliminated as they are not core parts of your project. 

-------

## 2. Installation

------------------

```
git clone https://github.com/rahulrajaram/dependency_mapper.git
cd dependency_mapper
pip install .
```

------------------

## 3. Usage

-------

```
cd <path/to/project/source>
dependency_mapper
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
