#include<stdio.h>
 
int main() {
  char str[100] = {"haystack"};
  char substr[20] = {"needle"};
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
  return 0;
}
//reference
//https://www.thecrazyprogrammer.com/2014/12/find-substring-in-string.html
