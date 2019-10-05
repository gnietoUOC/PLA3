#ifndef reader_h
#define reader_h

#include <stdio.h>
#include <stdlib.h>

class Reader {
	char *name;

	public:
		Reader(char *name);
		int dump(void);

};

#endif

