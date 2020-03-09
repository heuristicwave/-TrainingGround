#include<cstdio>

int count[10];

int main() {
	freopen("input.txt", "rt", stdin);

	int digit, res;
	int max = -2147483648;	
	char arr[100];
	
	scanf("%s", &arr);
	
	// !!! using ASCII !!!
	for(int i=0; arr[i]!='\0'; i++){
		digit = arr[i]-48;
		count[digit]++;
	}
	
	printf("%d\n", res);
		
	return 0;
}
