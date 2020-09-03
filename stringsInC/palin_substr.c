#include <stdio.h>

void find_palindrome(char *str) {
   int i, k, l, j, max =0, index = -1, check = 0, count = 0;
   for(i=0; i<sizeof(str); i++) {
      max = 0;
      k = i;
      j = i+1;
      while(str[j]!=' ' && str[j]!='\0'){
         j++;
      }
      l = j-1;
      if(str[k]!=' ' && str[k]!='\0') {
         while(k<=l) {
            if (str[k]==str[l]) {
               max++;
               if(count<=max) {
                  index = i;
                  count = max;
               }
            } else {
               max = 0;
               count = -1;
               break;
            }
            k++;
            l--;
         }
      }
      i = j;
   }
   printf("longest palin drome is :\n");
   for (i = index; i!=-1 && str[i]!=' ' && str[i]!='\0'; i++) {
      printf("%c", str[i]);
   }
   printf("\n");
   return;
//reference
//https://www.tutorialspoint.com/print-longest-palindrome-word-in-a-sentence-in-c-program
}

void count_substr(char *str, char *substr) {
  int temp, count = 0;
 
  for(int i=0; str[i]!='\0'; ++i) {
    int j=0;
    if(str[i] == substr[j]) {
      temp=i+1;
      while((str[i] == substr[j])&&(str[i]!='\0')) {
        i++;
        j++;
      }
      if(substr[j] == '\0') {
        ++count;
      }
      else {
        i = temp;
        temp = 0;
      }
    }
  }
  printf("The substring '%s' is present in given string '%s' %d times\n", substr,
          str, count);
  return;
//reference
//https://www.thecrazyprogrammer.com/2014/12/find-substring-in-string.html
}

int main() {
  char palin_str[] = {"wow"};
  find_palindrome(palin_str);
  char str[100] = {"haystack"};
  char substr[20] = {"needle"};
  count_substr(str, substr);
  return 0;
}
