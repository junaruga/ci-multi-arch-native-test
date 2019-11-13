CC ?= gcc
CFLAGS ?=
TARGET = bin/hello

all : $(TARGET)
.PHONY : all

$(TARGET):
	$(CC) $(CFLAGS) -o $@ src/main.c

clean :
	rm -rf src/*.o $(TARGET)
.PHONY : clean

test : all
	file $(TARGET)
	ls -l $(TARGET)
	$(TARGET)
.PHONY : test
