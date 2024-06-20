#include <stdio.h>
#include <unistd.h>

// Linux C, 在C语言中，我们使用access()函数来判断文件是否存在。这需要包含unistd.h头文件
// gcc -o cfe check_file_exist.c && ./cfe
int main() {
    char *file_path = "./a.txt";
    
    if (access(file_path, F_OK) != -1) {
        printf("File exist.\n");
    } else {
        printf("File doesn't exist.\n");
    }
    
    return 0;
}
