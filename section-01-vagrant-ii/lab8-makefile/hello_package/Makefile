# Makefile for hello program

CC = gcc
CFLAGS = -Wall -g
OUTPUT = hello

all: $(OUTPUT)

$(OUTPUT): hello.c
	gcc $(CFLAGS) hello.c -o hello

clean:
	rm -f hello

test: $(OUTPUT)
	./hello

install: $(OUTPUT)
	sudo cp hello /usr/local/bin/
