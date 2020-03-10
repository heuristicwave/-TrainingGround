#include <cstdio>

int main(){
	//freopen("input.txt", "rt", stdin);
	
	char str[100];
	int numA[53] = { 0, }; // for local var
	int numB[53] = { 0, }; // In global, init 0 auto
	
	scanf("%s", &str);
	
	for(int i=0; str[i] != '\0'; i++){
		if (str[i] < 91 && str[i] > 64)
			numA[str[i] - 64]++;
		else
			numA[str[i] - 70]++;
	}
	
	scanf("%s", &str);
	
	for(int i=0; str[i] != '\0'; i++){
		if (str[i] < 91 && str[i] > 64)
			numB[str[i] - 64]++;
		else
			numB[str[i] - 70]++;
	}
			
	for(int i=1; i<=52; i++){
		if(numA[i] != numB[i]){
			printf("NO\n");
			return 0;
		}
	}
	
	printf("YES\n");
	
	return 0;
}

