CC = g++
debug_flags = -Wall -std=c++23 -g -lm
compile_flags = -Wall -std=c++23 -g -lm

SOURCE = src/*.cpp

# COMPILE SERVER -> Compiles udp + tcp server and all its dependencies
c: src/main.cpp
	$(CC) $(compile_flags) -o ./bin/main $(SOURCE)
