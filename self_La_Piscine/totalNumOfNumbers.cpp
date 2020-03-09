#include<cstdio>

int main() {
	freopen("input.txt", "rt", stdin);

	int num, sum = 0;
	int c=1, d=9;
	int res = 0;
	
	scanf("%d", &num);
	
	while(sum+d<num){
		res = res+(c*d);
		sum += d;
		
		c++;
		d = d*10;
	}
	res = res + ((num-sum)*c);
//	for(int i=1; i<=num; i++){
//		tmp = i;
//		while(tmp>0){
//			tmp = tmp / 10;
//			cnt++;
//		}
//	}
	
	printf("%d\n", res);
		
	return 0;
}
