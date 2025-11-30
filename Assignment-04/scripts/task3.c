/* Task 3 (C): IPC using pipe(), fork(), wait() */
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <sys/wait.h>

int main() {
    int fd[2];
    if(pipe(fd) == -1) {
        perror("pipe");
        return 1;
    }

    pid_t pid = fork();
    if(pid < 0) {
        perror("fork");
        return 1;
    } else if(pid > 0) {
        // parent
        close(fd[0]);
        const char *msg = "Hello from parent (C)";
        write(fd[1], msg, strlen(msg)+1);
        close(fd[1]);
        wait(NULL);
        printf("Parent: message sent and child waited\n");
    } else {
        // child
        close(fd[1]);
        char buf[128];
        read(fd[0], buf, sizeof(buf));
        printf("Child received: %s\n", buf);
        close(fd[0]);
    }
    return 0;
}
