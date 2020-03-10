#include <cstdio>

int main(){
	freopen("input.txt", "rt", stdin);
	
	int n, num, flag;
	int cnt = 0;
	
	scanf("%d", &n);
	
	for(int i=2; i<=n; i++){
		flag = 1;
		for(int j=2; j*j<=i; j++){
			if(i%j==0){
				flag = 0;
				break;
			}
		}
		if (flag==1) cnt++;
	}
	
	printf("%d\n", cnt);
	return 0;
}

