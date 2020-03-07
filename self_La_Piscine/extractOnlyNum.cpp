#include <cstdio>

int main() {
	freopen("input.txt", "rt", stdin);
	
	char a[50];
	int res = 0, divisior = 0;
	
	scanf("%s", &a);
	for(int i=0; a[i]!='\0'; i++){
		if(a[i]>=48 && a[i]<=57) { // In python, 48 <= a[i] <= 57
			res = res*10 + (a[i]-48);
		}
	}

	printf("%d\n", res);
	
	for(int i=1; i<=res; i++){
		if(res%i==0) divisior++;
	}
	printf("%d\n", divisior);
	return 0;
}
