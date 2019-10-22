## C/CPP 
**C** y **CPP** son en realidad dos versiones del mismo código. Una en C y la otra en C++. Una pequeña (minúscula) aplicación que acepta el nombre de un fichero y, si lo encuentra, lo vuelca por pantalla. Nada más.

La gracia, para mí, de este ejercicio no era tanto escribir el código como la creación de un fichero makefile que no lo había hecho nunca (o hace tanto tiempo que ni me acuerdo). Bueno, y desoxidar el C++.

  ```cpp

    #include "reader.hpp"

    Reader::Reader(char *name) {
	    this->name = name;
    }

    int Reader::dump(void) {
    	FILE *file;
      char line[256];

      printf("Leyendo: %s\n\n",name);

      if (!(file = fopen(name,"r"))) {
        printf("No puedo abrir el fichero.\n\n");
        return 2;
      }

      while(fgets(line,sizeof(line),file)) {
        printf("%s",line);
      }

      fclose(file);

      return 0;
    }
```
