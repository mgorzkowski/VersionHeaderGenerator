## It's a simple version header generator for C/C++ projects

### Why?
###### Because sometimes you need to know which version of the code you are working with.

### How to use?
1) Edit your_config_file.xml
2) Run:

	> ./VersionHeaderGenerator.py your_config_file.xml

3) The generated file is placed in a proper place (look to the config file to check the place)

### Buildin variables*:
1) NAME
2) GIT_REVISION_HASH
3) GIT_SHORT_REVISION_HASH
4) GIT_BRANCH
5) GENERATION_TIME
6) GENERATION_DATE
7) GUARD_DEF (eg. \_EXAMPLE_VERSION_H_)

### Your own variables*:
Insert proper entry in your your_config_file.xml.
E.g:

    <your_important_variable>(0xDEADBEEF)</your_important_variable>

### You can try using attached example:
1) Run it:

	> cd example
	> make

*) Of course, they aren't variables from the point of view C/C++ language and its compilation. They are variables from point of view of project management.