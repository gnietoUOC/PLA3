#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <iconv.h>

#include <iconv.h>

int checkEncoding(char *name) {
	FILE *file;
	int rc = -1;

	if (file = fopen(name,"rb")) {
		int c = fgetc(file);
		printf("Found: %d\n",c);
		switch (c) {
			case 239:
				rc = 1;
				break;
			case 254:
			case 255:	// UTF-8
				rc = 3;
				break;
			default: 	// ANSI
				rc = 2;	
		}
		fclose(file);
	}
	return rc;	

}

int dump(char *name) {
	FILE *file;
	char line[256];
	char line2[256];
	iconv_t cd; 
	size_t size;
	size_t size2 = 256;

	char *pline = line; 
	char *pline2 = line2; 

	printf("Leyendo: %s\n",name);

	int type = checkEncoding(name);
	printf("Enconding: %d\n\n",type);

	// Si no puedo abrir el fichero (o no existe) devuelvo un error
	if (!(file = fopen(name,"r"))) {
		printf("No puedo abrir el fichero.\n\n");
		return 2;
	}

	cd = iconv_open("UTF-8","ISO-8859");

	// Leo el fichero línea a a línea
	while(fgets(line,sizeof(line),file)) {
		size = strlen(line);
		iconv(cd,&pline,&size,&pline2,&size2);

		printf("%s",line);
	}

	iconv_close(cd);

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



