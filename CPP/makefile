
obj = main.o reader.o 

*.o: 		*.cpp
#	g++ -o reader.o -c reader.c
	g++ -o $@ -c $<

reader: 	$(obj)
	g++ -o $@ $(obj)

clean: 
	rm reader *.o
