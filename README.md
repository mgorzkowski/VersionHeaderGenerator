## It's a simple version header generator for C/C++ projects

### Why?
Because sometimes you need to know which version of the code you are working with.

### How to use?
1) Edit config.xml
2) Run: 
	> ./VersionHeaderGenerator.py <path to config file> 

3) The generated file waiting in a proper place (look to the config file)

### Build in variables:
1) GUARD-DEF (eg. \_EXAMPLE_VERSION_H_)
2) NAME
3) GIT_REVISION_HASH
4) GIT_SHORT_REVISION_HASH
5) GIT_BRANCH

### You can try using attached example:
1) Run it:
	> cd example
	> make
