CC = gcc
TARGET = bin/hello

all : $(TARGET)
.PHONY : all

$(TARGET):
	$(CC) -o $@ src/main.c

clean :
	rm -rf src/*.o $(TARGET)
.PHONY : clean

test : all
	file $(TARGET)
	$(TARGET)
.PHONY : test
