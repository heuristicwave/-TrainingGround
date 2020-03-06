#include<cstdio>

int a[52][52] = { 0, };
int dx[4] = {-1, 0, 1, 0};
int dy[4] = {0, 1, 0, -1};

int main() {
	freopen("input.txt", "rt", stdin);
	
	int n;
	int flag; // search, recommand bool type
	int cnt = 0;
	
	scanf("%d", &n);
	
	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			scanf("%d", &a[i][j]);
		}
	}

	for(int i=1; i<=n; i++){
		for(int j=1; j<=n; j++){
			flag = 0;
			
			for(int k=0; k<4; k++){
				if(a[i][j]<= a[i+dx[k]][j+dy[k]]){
					flag = 1;
					break;
				}
			}
			if(flag == 0) cnt++;
		}

	}
	
	printf("%d\n", cnt);
	
	return 0;
}
