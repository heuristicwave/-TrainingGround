#include <cstdio>

int main() {
	freopen("input.txt", "rt", stdin);
	
	char a[101], b[101];
	int position = 0;
	
	gets(a);
	for(int i=0; a[i]!='\0'; i++){
		if(a[i]!=' ') {
			if(a[i]>=65 && a[i]<=90){
				// add 32 to the uppercase, it becomes lowercase
				b[position++] = a[i]+32; 
			}
			else b[position++] = a[i];		
		}
	}
	b[position]='\0'; // complete string arr

	printf("%s\n", b);
	
	return 0;
}
