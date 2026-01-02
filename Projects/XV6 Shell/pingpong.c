#include "kernel/types.h"
#include "user/user.h"

int main() {
    // Declare integers for holding write/read addresses to two pipes.
    int p2c[2];   //p2c[0] read end p2c[1] write end parent to child
    int c2p[2];   //child to parent, 0 is read, 1 is write. 

    //Declare a byte to exchange between processes
    char our_byte = 'P';

    // Call pipe() pipe twice to open two pipes
    pipe(p2c);
    pipe(c2p);

    int pid = fork();
    if (pid > 0) {
        //parent 
        //send byte (P) to child
        write(p2c[1], &our_byte, 1);
        
        //read modified byte from child (this waits until the child has
        // written something) so will read after child sends R
        read(c2p[0], &our_byte, 1);
        //be like yuh i read that. and print R
        printf("<%d> received pong, %c\n", pid, our_byte);
        exit(0);
    }
    else if (pid == 0){
        //child

        //place your code here to reveive a byte
        //reads P from the parents. 
        read(p2c[0], &our_byte, 1);
        printf("<%d> received ping, %c\n", pid, our_byte);

        //change byte value to R to be like yuh i read that.
        our_byte = 'R';

        //send back to parent. so now sending (R)
        write(c2p[1], &our_byte, 1);

        exit(0);

    }


    exit(0);
}