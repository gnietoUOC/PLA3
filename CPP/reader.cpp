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
		return(2);
	}

	while(fgets(line,sizeof(line),file)) {
		printf("%s",line);
	}

	fclose(file);

	return 0;
}


