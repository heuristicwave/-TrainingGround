#include <cstdio>

int digit_sum(int x){
	int tmp, sum=0;
	while(x>0){
		tmp = x%10;
		sum += tmp;
		x = x/10;
	}
	return sum;
}

int main() {
	freopen("input.txt", "rt", stdin);
	
	int n, num;
	int sum;
	int max=-2147483648, res;
	scanf("%d", &n);
	
	for(int i=1; i<=n; i++){
		scanf("%d", &num);
		sum = digit_sum(num);
		if(sum > max){
			max = sum;
			res = num;
		}
		else if (sum == max){
			if(num > res) res=num;
			
		}
	}

	printf("%d\n", res);
	return 0;
}
