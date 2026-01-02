#include "kernel/types.h"
#include "user/user.h"
#include "kernel/fcntl.h"

//dont need malloc or anything, we are only using buf as space.

/* Print the prompt ">>> " and read a line of characters
   from stdin. */
   //copy n buf number of characters into a memory location buf.
int getcmd(char *buf, int nbuf) {

  // ##### Place your code here
  //issue: the read is just overwriting so if a command is shorter, theres leftovers, causing issues.
  //to fix im going to set everything to an empty point in buffer before reading it in. 

  for (int i=0; i<nbuf; i++){
    buf[i] = '\0';
  }
  pause(10);
  write(2, ">>>", 3);
  read(0, buf, nbuf);

  return 0;
}

/*
  A recursive function which parses the command
  at *buf and executes it.
*/
__attribute__((noreturn))
void run_command(char *buf, int nbuf, int *pcp) {

  /* Useful data structures and flags. */
  char *arguments[10] = {0};  //space for 10 strings, so 10 pointers.
  int numargs = 0;  //this will be increased
  /* Flags to mark word start/end */
  int ws = 1; 
  //int we = 0;

  /* Flags to mark redirection direction to read from a file and write into a file*/
  int redirection_left = 0;  //for special characters??
  int redirection_right = 0;
  int redirection_symbol_r = 0;
  int redirection_symbol_l = 0;

  /* File names supplied in the command */
  char *file_name_l = 0;  //if using multiple files? 
  char *file_name_r = 0;

  int p[2];
  int pipe_cmd = 0;
  int pipe_pos = 0;

  /* Flag to mark sequence command */
  int sequence_cmd = 0;
  int i = 0;
  /* Parse the command character by character. */
  for (; i < nbuf; i++) {  //loop through characters, so i is the number character in buf.
    //so buf[i] will return the character
    /* Parse the current character and set-up various flags:
       sequence_cmd, redirection, pipe_cmd and similar. */

    /* ##### Place your code here. */
    //should also trim the buffer before doing this, so if theres a space. at start, get rid.
    switch(buf[i]){ //checks for each character
      case '>': //redirection program > output.txt
        buf[i] = '\0'; //ensures it works without spaces.
        redirection_right = 1; 
        redirection_symbol_r = i+1;
        for (int k=i; i<nbuf; k++){
          if (buf[redirection_symbol_r] == ' ' || buf[redirection_symbol_r] ==  '\n'){
            redirection_symbol_r++;
          }
          else {
            break;
          }
        }   
        break;
      case '<': //redirection program < input.txt
        buf[i] = '\0';
        redirection_left = 1;
        redirection_symbol_l = i + 1;
        for(int k=i; k<nbuf; k++) {
          if (buf[redirection_symbol_l] == ' ' || buf[redirection_symbol_l] ==  '\n'){
            redirection_symbol_l++;
          }
          else {
            break;
          }
        }
        break;
      case ';': //sequence - more than one command
        sequence_cmd = 1;
        buf[i] = '\0'; //so command doesn't execute a semi colon as well and stops there. 
        break;
      case '|':
        pipe_cmd = 1;
        buf[i] = '\0';
        pipe_pos = numargs;
        ws=1;
        break;
      default:
        break; 
    } //this is just setting flags. Goes through all of the characters and check for these symbols. 
    if(sequence_cmd){
      break;
    }

    if (ws == 1 && !(buf[i]==' ' || buf[i] == '\n' || buf[i] == '\0')) { //start of the word. 
      ws = 0;
      if (!(redirection_left || redirection_right)) {
        /* No redirection, continue parsing command. */
        // Place your code here.
        arguments[numargs] = &buf[i]; //save start of word in array
        numargs++;
      } 
      // ##### Place your code here.
      //if the character is equal to an  > or < then the next thing must be a file name?
      else { //redirection
        if (redirection_left) {  //< input
          file_name_l = buf + redirection_symbol_l; //pointer to the first character of files. 
        }
        if (redirection_right) {
          file_name_r = buf + redirection_symbol_r; //same again.
        }
      }
    } else if ((ws == 0) && (buf[i] == ' ' || buf[i] == '\n')) { //mark end of word with end of string
        buf[i] = '\0';
        ws = 1;
      }
    } 
  
  /*Whole for loop:  
  1. iterate through every letter in buffer
    a. check letters and assign the correct flags
    b. if no redirection - seperate each word into argument array. 
      if redirection - set file name pointers to the filenames.*/

  /*
    Sequence command. Continue this command in a new process.
    Wait for it to complete and execute the command following ';'.
  */
  if (sequence_cmd) {
    sequence_cmd = 0;
    if (fork() != 0) { //if the parent.
      wait(0);
      // ##### Place your code here.
      // Call run_command recursively
      /*if ; then we need to execute the first part of the commnad. And then 
      pass whats left of the buffer into run command again. also, maybe i should set
      the semi colon into a end of string so it doesnt include the semi colon. do that in my case. */
      buf += i+1;
      nbuf -= i;
      run_command(buf, nbuf, pcp);
    } else {
      exec(arguments[0], arguments);
      fprintf(2, "leftside sequence failed");

    }
  }

  /*
    If this is a redirection command,
    tie the specified files to std in/out.
  */
  
  if (redirection_left) {
    // ##### Place your code here.
    // then the file should be read into. so reading program < input.txt 
    // read input.txt and put it into the last command, so i guess store in array where < is stored
    close(0);  //change file descriptor, exec - stand out, fd.
    open(file_name_l, O_RDONLY);
  }
  if (redirection_right) {
    // ##### Place your code here.
    // file should be written.  so writing program > output.txt
    
    close(1); //standard out
    open(file_name_r, O_CREATE|O_WRONLY); //echo hello > output.txt
  }

  /* Parsing done. Execute the command. */

  /*
    If this command is a CD command, write the arguments to the pcp pipe
    and exit with '2' to tell the parent process about this.
  */
 //cd doesnt exist, so needs special treatment. we want to change the parents
 //directory, not just the childs. 
  if (strcmp(arguments[0], "cd") == 0) {
    // ##### Place your code here.
    write(pcp[1], arguments[1], strlen(arguments[1] + 3));
    close(pcp[1]);
    exit(2);
  } else {
    /*
      Pipe command: fork twice. Execute the left hand side directly.
      Call run_command recursion for the right side of the pipe.
    */
    if (pipe_cmd) {
      // ##### Place your code here.
      // fork then fork. exec. destroy fork2. then exec again destory fork1. then exits in this. 
      pipe(p);
      int array_size = sizeof(arguments)/sizeof(arguments[0]);
      if (fork() == 0) {
        if (fork() == 0) {
          close(1);
          dup(p[1]);
          //need to contain left hand side, arguments up to pipe position. 
          for (int i = pipe_pos; i < array_size; i++) {
            arguments[i] = '\0'; //replace arguments after pipe to null so not executed. 
          }
          
          exec(arguments[0], arguments); //executes left hand side.  //then should exit child to other fork.
          fprintf(2, "failed to execute pipe left");
          exit(0);
          fprintf(2, "first child\n");
    
        } 
        pause(5);
        close(0);
        dup(p[0]); //replace standard in with read end of pipe
        //need arguments from pipe until end
        for (int i=0; i < (array_size - pipe_pos); i++){
          arguments[i] = arguments[i + pipe_pos];
        }
        exec(arguments[0], arguments);
        fprintf(2, "Failed to execute the rest");
      }
    } else {
      // ##### Place your code here.
      // Simple command; call exec()
      //fork
      if (fork() == 0){
        exec(arguments[0], arguments);
        fprintf(2, "FAILED");
        exit(0);
      }
    }
  }
  exit(0);
}

int main(void) {

  //buf is declared. Commands no longer than 100 characters
  static char buf[100];
  char dir[100];

  //pipe is declared
  int pcp[2];
  pipe(pcp);


  /* Read and run input commands. 
  While get command returns a value larger than 0, keep */
  while(getcmd(buf, sizeof(buf)) >= 0){
    if(fork() == 0) {//child process
    //whats been read is being put into run_command. 
      run_command(buf, 100, pcp);
    }
    /*
      Check if run_command found this is
      a CD command and run it if required.
    */
    int child_status = 0;
    // ##### Place your code here
    wait(&child_status);
    if (child_status == 2) {  
      close(pcp[1]);
      pause(10);
      read(pcp[0], dir, 100);
      close(pcp[0]);
      chdir(dir);
       //okay so cd "works" but when u ls after its stil the og stuff?
    }

    
  }
  exit(0);
}
