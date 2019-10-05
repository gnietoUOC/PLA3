#include <stdio.h>
#include <stdlib.h>

#include "reader.h"

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

int main(int argc, char **argv) {

	if (argc!=2) {
		printf("Sintaxis: reader <fichero>\n\n");
		return(1);
	}

	Reader *r = new Reader(argv[1]);
	r->dump();
	delete r;

	return 0;
}



