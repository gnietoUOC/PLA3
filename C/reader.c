#include <stdio.h>
#include <stdlib.h>

int dump(char *name) {
	FILE *file;
	char line[256];

	printf("Leyendo: %s\n\n",name);

	// Si no puedo abrir el fichero (o no existe) devuelvo un error
	if (!(file = fopen(name,"r"))) {
		printf("No puedo abrir el fichero.\n\n");
		return 2;
	}

	// Leo el fichero línea a a línea
	while(fgets(line,sizeof(line),file)) {
		printf("%s",line);
	}

	// Cierro el fichero
	fclose(file);

	return 0;

}

int main(int argc, char **argv) {


	// Verifico si me han pasado el nombre de un fichero
	if (argc!=2) {
		printf("Sintaxis: reader <fichero>\n\n");
		return 1;
	}
	
	int rc = dump(argv[1]);

	return rc;
}



