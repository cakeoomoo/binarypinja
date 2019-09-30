#include <stdio.h> 
#include <stdlib.h> 
#include <string.h>

int main(int argc, char *argv[]) { 
   char text[1024]; 
   static int test_val = -72;

   if(argc < 2) {
      printf("使用方法： %s <出力するテキスト>\n", argv[0]);
      exit(0);
   }
   strcpy(text, argv[1]);

   printf("ユーザによって入力されたテキストを出力する正しい方法：\n");
   printf("%s", text);

   printf("\nユーザによって入力されたテキストを出力する誤った方法：\n");
   printf(text);

   printf("\n");

   // Debug output
   printf("[*] test_val @ 0x%08x = %d 0x%08x\n", &test_val, test_val, test_val);

   exit(0);
}
