CC=gcc
CFLAGS=-Wall -DNLOG -DNDEBUG -O3
LFLAGS=
bloqqer: bloqqer.o bloqqer.h blqrcfg.o makefile
	$(CC) $(CFLAGS) -o $@ bloqqer.o blqrcfg.o $(LFLAGS)
qrat_checker: qrat_checker.o makefile
	$(CC) $(CFLAGS) -o $@ qrat_checker.o $(LFLAGS)
pp: pp.o makefile
	$(CC) $(CFLAGS) -o $@ pp.o $(LFLAGS)
pp.o: pp.c makefile
	$(CC) $(CFLAGS) -c pp.c $(LFLAGS)
qrat_checker.o: qrat_checker.c makefile
	$(CC) $(CFLAGS) -c qrat_checker.c $(LFLAGS)
bloqqer.o: bloqqer.c bloqqer.h makefile
	$(CC) $(CFLAGS) -c bloqqer.c $(LFLAGS)
libbloqqer.o: bloqqer.c bloqqer.h makefile
	$(CC) -DLIBBLOQQER $(CFLAGS) -o libbloqqer.o -c bloqqer.c $(LFLAGS)
blqrcfg.o: blqrcfg.c blqrcfg.h makefile
	$(CC) $(CLFAGS) -c blqrcfg.c
blqrcfg.h: bloqqer.c bloqqer.h mkconfig VERSION makefile
	rm -f $@; ./mkconfig > $@
libbloqqer.a: libbloqqer.o
	ar rc $@ libbloqqer.o
	ranlib $@
analyze:
	clang --analyze $(CFLAGS) $(shell ls *.c *.h)
clean:
	rm -f `cat .gitignore`
