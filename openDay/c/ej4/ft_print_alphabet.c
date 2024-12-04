#include <unistd.h>

int main(){
	write(STDOUT_FILENO,"ABCDEFGHIJKLMNOPQRSTUVWXYZ\n", 28);
}
