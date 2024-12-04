#include <unistd.h>

int main(){
	write(STDOUT_FILENO, "Hello World! Hello OpenDay!\n", 29);

return 0;
}
