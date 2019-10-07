
OBJ = reader.o 

*.o: 	*.c
	gcc -o $@ -c $<

reader: 	$(OBJ)
	gcc -o $@ $(OBJ)

clean: 
	rm reader $(OBJ)
