
OBJ = main.o reader.o 

*.o: 		*.cpp
	g++ -o $@ -c $<

reader: 	$(OBJ)
	g++ -o $@ $(OBJ)

clean: 
	rm reader $(OBJ)
