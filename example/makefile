NAME=example

.PHONY: all build run clean

all: build run

build: $(NAME)

clean:
	rm -f example

run:
	./example

$(NAME): example.c
	gcc $? -o $@

