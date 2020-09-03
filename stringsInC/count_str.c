#include <stdio.h>

int compare_strings(char a[], char b[])
//https://www.programmingsimplified.com/c-program-compare-two-strings
{
   int c = 0;
 
   while (a[c] == b[c]) {
      if (a[c] == '\0' || b[c] == '\0')
         break;
      c++;
   }
   
   if (a[c] == '\0' && b[c] == '\0')
      return 0;
   else
      return -1;
}

void main() {
  char filename[200];
  printf("enter filename:\n");
  scanf("%s", filename);
  FILE *f_in;
  f_in = fopen(filename, "r");

  char keyword[200];
  printf("enter word to count (case sensitive):\n");
  scanf("%s", keyword);

  //loop over file and count keyword
  char word[200];
  int count = 0;
  while (fscanf(f_in, "%s", word) == 1) {
    if(!compare_strings(word, keyword)) ++count;
  }
  printf("Number of word '%s' in file are %d\n", keyword, count);
  return;
}
