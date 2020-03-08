#include<cstdio>
#include<algorithm>
int a[9][9];

int main() {
	freopen("input.txt", "rt", stdin);

	int sum, ave;
	int min, tmp, res;
	
	for(int i=0; i<9; i++){
		sum = 0;
		for(int j=0; j<9; j++){
			scanf("%d", &a[i][j]);			
			sum += a[i][j];
		}
		ave=(sum/9.0)+0.5;	// round(total/9.0), cmath
		printf("%d ", ave);
		min=2147000000;
		for(int j=0; j<9; j++){
			tmp = abs(a[i][j]-ave);			
			if(tmp<min){
				min = tmp;
				res = a[i][j];
			} else if(tmp==min) {
				if(a[i][j]>res)
					res = a[i][j];
			}			
		}
		printf("%d\n", res);
	}	
	return 0;
}
