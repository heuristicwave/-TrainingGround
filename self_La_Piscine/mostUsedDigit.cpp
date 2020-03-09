#include <cstdio>

int count[10];
int main(){
	freopen("input.txt", "rt", stdin);
	
	char num[100];
	int digit, res;
	int max = -2147000000;
	
	scanf("%s", &num); // array! %s!!
	
	for(int i=0; num[i]!= '\0'; i++){
		digit = num[i] - 48;
		count[digit]++;
	}
	
	for(int i=0; i < 10; i++){
		if(count[i] >= max){
			max = count[i];
			res = i;
		}
	}
	
	printf("%d\n", res);
	
	return 0;
}
