#include "reader.hpp"

int main(int argc, char **argv) {

	// Verifico si me han pasado el nombre de un fichero
	if (argc!=2) {
		printf("Sintaxis: reader <fichero>\n\n");
		return(1);
	}

	// Creo una instancia del objecto
	Reader *r = new Reader(argv[1]);
	// Vuelco el contenido del fichero
	int rc = r->dump();
	delete r;

	return rc;
}



