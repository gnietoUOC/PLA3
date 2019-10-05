#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {

	FILE *file;
	char line[256];

	printf("Genaro es el mejor\n");

	if (argc!=2) {
		printf("Sintaxis: reader <fichero>\n\n");
		return(1);
	}

	printf("Leyendo: %s\n\n",argv[1]);

	if (!(file = fopen(argv[1],"r"))) {
		printf("No puedo abrir el fichero.\n\n");
		return(2);
	}

	while(fgets(line,sizeof(line),file)) {
		printf("%s",line);
	}

	fclose(file);

	return 0;
}



