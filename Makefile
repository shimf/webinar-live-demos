CPP=g++

dist/a.out: main.o dist
	$(CPP) main.o -o dist/a.out

dist:
	mkdir -p dist

%.o: %.c
	$(CPP) -c -o $@

clean:
	rm *.o

version:
	python inc_version.py version.h
