# Week Manager
An opinionated tool for managing weekly Java assignments for CT60A2411 Object Oriented Programming.
## Usage
### New week
```sh
# Example of creating week 2, where App.java and Hedgehog.java are required
$ python wm.py create 2 -a -c Hedgehog
# Example of creating fictional week 3, where App.java, Cat.java and Dog.java are required.
$ python wm.py create 3 -a -c Cat Dog

# Note that the -c flag is greedy and and the following order will cause an error, as 3 is interpreted as a class name:
$ python wm.py create -a -c Cat Dog 3  
usage: wm.py create [-h] [-f] [-a] [-c [CLASSES ...]] week
wm.py create: error: the following arguments are required: week
```
### Compile (and run) week
```sh
# Example of compiling week 2
$ python wm.py compile 2
Compiled Java files to run/week2
# Example of compiling week 1, along with running it
$ python wm.py compile 1 -e
Compiled Java files to run/week1
Hello World!

# Note that compiling a week will place it in the run/ directory, which is generally located in the same folder as wm.py
```
### Compress/Zip week
```sh
# Example of compressing week 2
$ python wm.py zip 2
# Example of compressing week 1, replacing any existing zip file
$ python wm.py zip 1 -f

# Note that the zip file produced will be located in the same folder as wm.py
# It has been tested to work with the structure required by CodeGrade as of 17.1.2024
```