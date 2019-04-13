NAME=example
SOURCE_FILE=example.c
LIB=../version.h

.PHONY: all build run clean

all: build run

build: $(NAME)

clean:
	rm -f example

run:
	./$(NAME)

remove-header:
	rm -f $(LIB)

$(NAME): $(SOURCE_FILE) $(LIB)
	gcc $(SOURCE_FILE) -o $@

$(LIB):
	cd ..; ./generate.sh
