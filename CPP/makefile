
obj = main.o reader.o 

*.o: 		*.cpp
	g++ -o $@ -c $<

reader: 	$(obj)
	g++ -o $@ $(obj)

clean: 
	rm reader *.o
